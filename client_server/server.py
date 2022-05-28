import argparse
import logging
import sys

import gevent
import zmq
from gevent import subprocess

_BINDING = 'tcp://127.0.0.1:8000'
parser = argparse.ArgumentParser(
    description='Process some integers',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')


class Server:
    def __init__(self):
        self.logger = logging.getLogger('SERVER')
        self.context = zmq.Context()
        self.socket_server = self.context.socket(zmq.REP)
        self.socket_server.bind(_BINDING)
        logging.info("Server started")

    @staticmethod
    def os_result(obj: dict) -> dict:
        command_name = obj['command_name']
        parameters = obj.get('parameters')
        given_os_command = command_name + ' ' + ' '.join(parameters)
        with subprocess.Popen(
                given_os_command,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                shell=True
        ) as proc:
            result = proc.stdout.read()
        data = {
            "given_os_command": given_os_command,
            "result": result
        }
        return data

    @staticmethod
    def os_compute(obj: dict) -> dict:
        expression = obj['expression']
        result = eval(expression)
        data = {
            "given_math_expression": expression,
            "result": result
        }
        return data

    def get_result(self, obj: dict) -> dict:
        command_type = obj['command_type']
        if command_type == "os":
            return self.os_result(obj)
        if command_type == "compute":
            return self.os_compute(obj)

    def run_server(self) -> None:
        while True:
            received_message = self.socket_server.recv_json()
            logging.info("Received message: %s", received_message)
            result = self.get_result(received_message)
            self.socket_server.send_json(result)
            logging.info("Sent result: %s", result)
            # sub = Popen(['sleep 100; uname'], stdout=PIPE, shell=True)
            # sub.communicate()


if __name__ == "__main__":
    parser.add_argument(
        "-c",
        "--concurrency",
        help="run server in concurrency mode",
        default=1,
    )
    args = parser.parse_args()
    config = vars(args)
    try:
        concurrency = int(config['concurrency'])
    except ValueError:
        logging.error("Concurrency must be an integer")
        sys.exit(1)
    server = Server()
    greens = [gevent.spawn(server.run_server) for i in range(concurrency)]
    gevent.joinall(greens)