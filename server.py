import time

from practice8 import runCommands
import zmq
context = zmq.Context()
# Define the socket using the "Context"
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:8000")

while True:
    msg = socket.recv_json()
    time.sleep(1)
    print(msg)
    socket.send_json(runCommands(msg))





