import unittest

import zmq

from client_server.client import Client
from unittest.mock import patch
from client_server.server import Server

class ClientTest(unittest.TestCase):
    def setUp(self):
        self._BINDING = 'tcp://127.0.0.1:4006'
        self.context = zmq.Context()

        self.socket_client = self.context.socket(zmq.REQ)
        self.socket_client.connect(self._BINDING)

        self.socket_server = self.context.socket(zmq.REP)
        self.socket_server.bind(self._BINDING)









