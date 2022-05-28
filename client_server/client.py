import argparse
import json
import logging
import sys
from os.path import exists

import zmq

_BINDING = 'tcp://127.0.0.1:8000'
parser = argparse.ArgumentParser(
    description='Process file paths',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')


class Client:
    def __init__(self, path):
        self.logger = logging.getLogger('CLIENT')
        self.path = path
        self.context = zmq.Context()
        self.socket_client = self.context.socket(zmq.REQ)
        self.socket_client.connect(_BINDING)
        logging.info("Client connected to server")

    def read_json_file(self) -> dict:
        with open(self.path, 'r') as f:
            if not f.readable():
                logging.error("File %s is not readable", self.path)
                sys.exit(1)
            elif f.read() == '':
                logging.error("File %s is empty", self.path)
                sys.exit(1)

            data = json.load(f)

            if data['command_type'] not in ['os', 'compute']:
                logging.error("Command type is not valid")
                sys.exit(1)

            elif data['command_type'] == 'os':
                if not data['command_name'] or not data['parameters']:
                    logging.error("Command name or parameters are empty")
                    sys.exit(1)
            elif data['command_type'] == 'compute':
                if not data['expression']:
                    logging.error("Expression is empty")
                    sys.exit(1)
        return data

    def run(self) -> None:
        message = self.read_json_file()
        self.socket_client.send_json(message)
        received_message = self.socket_client.recv_json()
        logging.info("Received message: %s", received_message)
        self.socket_client.close()


if __name__ == "__main__":
    parser.add_argument(
        "--file",
        help="send file path",
    )
    args = parser.parse_args()
    config = vars(args)
    file_path = config['file']
    try:
        file_exists = exists(file_path)

        client = Client(file_path)
        client.run()
    except FileNotFoundError:
        logging.error("File not found")
        sys.exit(1)