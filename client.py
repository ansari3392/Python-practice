import zmq

data = input('enter your json file: ')

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:8000")
socket.send_json(data)

msg_in = socket.recv().decode('utf-8')
print(msg_in)




