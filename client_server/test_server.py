import unittest
from client_server.client import Client
from unittest.mock import patch
import zmq
from client_server.server import Server

class ServerTest(unittest.TestCase):
    def setUp(self):
        self._BINDING = 'tcp://127.0.0.1:4006'
        self.context = zmq.Context()

        self.socket_client = self.context.socket(zmq.REQ)
        self.socket_client.connect(self._BINDING)

        self.socket_server = self.context.socket(zmq.REP)
        self.socket_server.bind(self._BINDING)

    def test_os_result(self):
        obj = {
            "command_type": "os",
            "command_name": "ping",
            "parameters": []
        }

        self.socket_client.send_json(obj)
        received_message = self.socket_server.recv_json()
        self.assertEqual(received_message, {
            "command_type": "os",
            "command_name": "ping",
            "parameters": []
        })

        result = get_result(received_message)

        self.assertEqual(result, {
                         "given_os_command": "ping",
                         "result": "PONG"
                         })

    # def test_os_compute(self):
    #     obj = {
    #         "command_type": "compute",
    #         "expression": "1+1"
    #     }
    #
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_math_expression": "1+1",
    #         "result": 2
    #     })
    #
    # def test_get_result(self):
    #     obj = {
    #         "command_type": "os",
    #         "command_name": "ping",
    #         "parameters": []
    #     }
    #
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_os_command": "ping",
    #         "result": "PONG"
    #     })
    #
    #     obj = {
    #         "command_type": "compute",
    #         "expression": "1+1"
    #     }
    #
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_math_expression": "1+1",
    #         "result": 2
    #     })
    #
    # def test_os_result_and_compute_with_concurrency(self):
    #     obj = {
    #         "command_type": "os",
    #         "command_name": "ping",
    #         "parameters": []
    #     }
    #
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_os_command": "ping",
    #         "result": "PONG"
    #     })
    #
    #     obj = {
    #         "command_type": "compute",
    #         "expression": "1+1"
    #     }
    #
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_math_expression": "1+1",
    #         "result": 2
    #     })
    #
    #     obj = {
    #         "command_type": "os",
    #         "command_name": "ping",
    #         "parameters": []
    #     }
    #     self.socket_client.send_json(obj)
    #     received_message = self.socket_server.recv_json()
    #     self.assertEqual(received_message, {
    #         "given_os_command": "ping",
    #         "result": "PONG"
    #     })















