from signal import SIGINT, SIGKILL
import argparse
import json
import logging
import shlex
import sys

from os.path import exists
from subprocess import Popen, PIPE
from time import sleep

import zmq

from _json_validators import JsonValidator

_BINDING = 'tcp://127.0.0.1:8000'
parser = argparse.ArgumentParser(
    description='Process file paths',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')


time_to_sleep = 0.15

class Client:
    def __init__(self, path):

        self.server = None
        self.logger = logging.getLogger('CLIENT')
        self.path = path
        self.context = zmq.Context()
        self.start_server_process()

    def read_json_file(self) -> dict:
        with open(self.path, 'r') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                logging.error("File is not valid JSON")
                sys.exit(1)

        if data.get('command_type') not in ['os', 'compute']:
            logging.error("Command type is not valid")
            sys.exit(1)
        for Validator in JsonValidator.__subclasses__():
            if Validator.meet_condition(data):
                try:
                    Validator.validate(data)
                except ValueError as e:
                    logging.error(e)
                    sys.exit(1)
                break
        return data

    def start_server_process(self):
        self.server = Popen('python server.py', shell=True, stdout=PIPE)

        for line in self.server.stdout.readline():
            if 'main loop' in line:
                break

    def end_server_process(self):
        self.server.send_signal(SIGINT)
        sleep(time_to_sleep)
        self.server.send_signal(SIGKILL)
        self.server.wait()

    def run(self):
        socket_client = self.context.socket(zmq.REQ)
        socket_client.connect(_BINDING)
        message = self.read_json_file()
        socket_client.send_json(message)
        sleep(time_to_sleep)
        try:
            received_message = socket_client.recv_json(zmq.NOBLOCK)
            result = json.dumps(received_message, indent=4)
            print(result)
            logging.info("Received message: %s", result)

        except zmq.ZMQError:
            pass


if __name__ == "__main__":
    parser.add_argument(
        "--file",
        help="send file path",
    )
    args = parser.parse_args()
    config = vars(args)
    file_path = config['file']
    if file_path:
        try:
            file_exists = exists(file_path)
            client = Client(file_path)
            client.run()
            client.context.destroy()
            client.end_server_process()
        except FileNotFoundError:
            logging.error("File not found")
            sys.exit(1)
    else:
        logging.error("File path is empty")
        sys.exit(1)

