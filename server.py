from gevent import spawn

import zmq.green as zmq

from practice8 import run_commands

context = zmq.Context()
socket = context.socket(4)
socket.connect("tcp://localhost:5559")

def serve(socket):
    while True:
        message = socket.recv_json()
        print("Received request: ", message)
        socket.send_json(run_commands(message))


server = spawn(serve, socket)
