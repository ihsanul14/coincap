import unittest
from framework.infra.validator import Validator
from application.http.tracker.tracker import CreateTrackerRequest
    
class TestValidator(unittest.TestCase):
    def test_validator(self):
        v = Validator()
        data = {
            'name': '',
            'price': 0
        }
        res = v.Validate(data,CreateTrackerRequest)
        self.assertIsNone(res)
        
        data = {
            'name': '',
            'price': -1
        }
        res = v.Validate(data,CreateTrackerRequest)
        self.assertIsNotNone(res)