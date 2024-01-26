import unittest
from framework.infra.logger import Logger
    
class TestLogger(unittest.TestCase):
    def test_logger(self):
        l = Logger()
        self.assertIsNone(l.Info("info"))
        self.assertIsNone(l.Warning("warning"))
        self.assertIsNone(l.Error("error"))