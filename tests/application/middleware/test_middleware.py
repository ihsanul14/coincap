import unittest
from application.middleware import JwtMiddleware
from fastapi import HTTPException

class TestMiddleware(unittest.TestCase):
    secret_key = "sample_secret"
    sample_email = 'sample_email'
    def test_generate_token_validate(self):
        j = JwtMiddleware()
        j.secret_key = self.secret_key
        
        data = {
            'email': self.sample_email
        }
        res = j.generate_token(data)
        res_arr = res.split('.')
        self.assertIsNotNone(res)
        self.assertEqual(len(res_arr),3)
        
        res = j.validate_token(res)
        self.assertIsNone(res)
        
        data = {
            'name': self.sample_email
        }
        res = j.generate_token(data)
        res_arr = res.split('.')
        self.assertIsNotNone(res)
        self.assertEqual(len(res_arr),3)
        
        try:
            j.validate_token(res)
        except HTTPException as e:
            self.assertEqual(e.status_code, 401)
            
        try:
            j.validate_token("")
        except HTTPException as e:
            self.assertEqual(e.status_code, 401)
            
            
