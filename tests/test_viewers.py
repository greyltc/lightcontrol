import unittest
from LightServer.gtk4 import Interface
import sys

class Gtk4TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.interface = Interface
        return super().setUp()

    def test_init(self):
        iface = self.interface()
        self.assertIsInstance(iface, self.interface)

    def test_full_interface(self):
        iface = self.interface()
        iface.run()
