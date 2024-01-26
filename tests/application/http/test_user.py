import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
import unittest
from fastapi import FastAPI
from application.middleware import JwtMiddleware
from application.http.user.user import UserHttp
from framework.infra import Infra


app = FastAPI()
mock_usecase = MagicMock()
tracker_http = UserHttp(infra=Infra())
tracker_http.serve_router(app)
    
class TestTrackerHttp(unittest.TestCase):
    client = TestClient(app)
    def get_data():
        return {"message": "mocked data"}
    
    def generate_header(self):
        token = JwtMiddleware().generate_token({'email': 'sample'})
        headers = {'Authorization': f'Bearer {token}'}
        return headers

    def test_signup(self):
        url = "/api/signup"
        mock_usecase = MagicMock()
        tracker_http.usecase = mock_usecase

        res = self.client.post(url, headers=self.generate_header(),json={'email': 'test', 'password': 'sample', 'password_confirmation': ''})
        self.assertEqual(res.status_code, 422)
        
        mock_usecase.sign_up.return_value = {"code": 200}
        res = self.client.post(url, headers=self.generate_header(),json={'email': 'test', 'password': 'sample', 'password_confirmation': 'sample'})
        self.assertEqual(res.status_code, 200)
        
    def test_signin(self):
        url = "/api/signin"
        mock_usecase = MagicMock()
        tracker_http.usecase = mock_usecase

        res = self.client.post(url, headers=self.generate_header(),json={'email': 'test', 'password': ''})
        self.assertEqual(res.status_code, 422)

        mock_usecase.sign_in.return_value = Exception('error')
        res = self.client.post(url, headers=self.generate_header(),json={'email': 'test', 'password': 'sample'})
        self.assertEqual(res.status_code, 500)
        
        mock_usecase.sign_in.return_value = {"code": 200}
        res = self.client.post(url, headers=self.generate_header(),json={'email': 'test', 'password': 'sample'})
        self.assertEqual(res.status_code, 200)
        
    def test_logout(self):
        url = "/api/logout"
        mock_usecase = MagicMock()
        tracker_http.usecase = mock_usecase

        res = self.client.post(url)
        self.assertEqual(res.status_code, 401)
        
        mock_usecase.logout.return_value = {'code': 200}
        res = self.client.post(url, headers=self.generate_header())
        self.assertEqual(res.status_code, 200)
 