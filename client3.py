import gevent

import zmq.green as zmq

_BINDING = 'tcp://127.0.0.1:8000'

context = zmq.Context()

def client():
    client_socket = context.socket(3)
    client_socket.connect(_BINDING)

    client_socket.send_json(input('enter your json file: '))

    response = client_socket.recv_json()
    print("Response:\n[%s]" % response)
    print('')


client = gevent.spawn(client)
client.join()
