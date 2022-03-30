import unittest
from lightcontrol.server import LightServer


class LightServerTestCase(unittest.TestCase):
    def test_init(self):
        ls = LightServer()
        self.assertIsInstance(ls, LightServer)

    def test_connect(self):
        ls = LightServer()
        self.assertIsInstance(ls, LightServer)
        ls.connect()

    def test_run(self):
        runtime = 5  # seconds
        ls = LightServer()
        self.assertIsInstance(ls, LightServer)
        ls.connect()
        ls.run(timeout=runtime)
