import gevent
import zmq
from practice8 import run_commands

_BINDING = 'tcp://127.0.0.1:8000'

context = zmq.Context()

def server():
    server_socket = context.socket(zmq.REP)
    server_socket.bind(_BINDING)

    while True:
        received = server_socket.recv_json()
        print("Received:\n[%s]" % received)
        print('')
        server_socket.send_json(run_commands(received))


server = gevent.spawn(server)
server.join()

