import sys

path = "/home/shahbazi/Desktop/project"

if path not in sys.path:
    sys.path.insert(0, path)

import unittest
from unittest import mock
from apps import say_hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        result = mock.Mock(return_value = "hello")
        self.assertEqual(result(), say_hello.hello())