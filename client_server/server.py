import json
import time
from multiprocessing import Process

import zmq
from gevent import subprocess
_BINDING = 'tcp://127.0.0.1:8000'

class Server:
    def __init__(self):
        self.context = zmq.Context()
        self.server_socket = self.context.socket(zmq.REP)
        self.server_socket.bind(_BINDING)
        print('Running server on: ', _BINDING)

    def os_result(self, obj: dict) -> dict:
        command_name = obj['command_name']
        parameters = obj['parameters']
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
        time.sleep(20)
        return data

    def os_compute(self, obj: dict) -> dict:
        expression = obj['expression']
        result = eval(expression)
        data = {
            "given_math_expression": expression,
            "result": result
        }
        time.sleep(20)
        return data

    def get_result(self, json_string: str) -> dict:
        obj = json.loads(json_string)
        command_type = obj['command_type']
        if command_type == "os":
            return self.os_result(obj)
        if command_type == "compute":
            return self.os_compute(obj)

    def run_server(self) -> None:
        received_message = self.server_socket.recv_json()
        # print(type(received_message))
        print("Received:\n %s" % received_message)
        self.server_socket.send_json(self.get_result(received_message))
        # self.server_socket.close()

    def __call__(self, *args, **kwargs):
        while True:
            self.run_server()


if __name__ == "__main__":
    server = Server()
    p = Process(target=server,)
    p.start()
    p.join()
