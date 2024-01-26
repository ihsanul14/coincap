import unittest
from framework.infra.error import Error
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
    
class TestError(unittest.TestCase):
    message = "sample_error"
    def test_logger(self):
        
        e = Error()
        res = e.error(Exception(self.message))
        self.assertEqual(res['code'], 500)
        res = e.error(NoResultFound(self.message))
        self.assertEqual(res['code'], 404)
        res = e.error(IntegrityError(statement=self.message,orig=None,params=None))
        self.assertEqual(res['code'], 400)        
        