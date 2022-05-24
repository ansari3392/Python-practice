from gevent import spawn
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

#  Do 10 requests, waiting each time for a response
def client():
    for request in range(1, 10):
        socket.send_json(input('enter your json file: '))
        message = socket.recv_json()
        print("Received reply ", request, "[", message, "]")



