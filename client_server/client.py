import json

import gevent
import zmq

_BINDING = 'tcp://127.0.0.1:8000'


class Client:
    def __init__(self):
        self.context = zmq.Context()
        self.client_socket = self.context.socket(zmq.REQ)
        self.client_socket.connect(_BINDING)
        print("Connecting to server...")

    def read_json_file(self) -> dict:
        with open('file.json', 'r') as f:
            data = json.load(f)
        return data

    def run_client(self) -> None:
        message = self.read_json_file()
        self.client_socket.send_json(message)
        received_message = self.client_socket.recv_json()
        print(received_message)
        self.client_socket.close()

    def __call__(self, *args, **kwargs):
        self.run_client()



if __name__ == "__main__":
    client = Client()
    client()


