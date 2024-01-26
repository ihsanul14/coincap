import unittest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
import unittest
from fastapi import FastAPI
from application.middleware import JwtMiddleware
from application.http.tracker.tracker import TrackerHttp
from framework.infra import Infra


app = FastAPI()
mock_usecase = MagicMock()
tracker_http = TrackerHttp(infra=Infra())
tracker_http.serve_router(app)
    
class TestTrackerHttp(unittest.TestCase):
    client = TestClient(app)
    def get_data():
        return {"message": "mocked data"}
    
    def generate_header(self):
        token = JwtMiddleware().generate_token({'email': 'sample'})
        headers = {'Authorization': f'Bearer {token}'}
        return headers

    def test_get_data(self):
        url = "/api/tracker"
        mock_usecase = MagicMock()
        tracker_http.usecase = mock_usecase
        
        res = self.client.get(url)
        self.assertEqual(res.status_code, 401)
        
        mock_usecase.get_data.return_value = {"code": 200}
        res = self.client.get(url, headers=self.generate_header())
        self.assertEqual(res.status_code, 200)
        
    def test_add_data(self):
        url = "/api/tracker"
        mock_usecase = MagicMock()
        tracker_http.usecase = mock_usecase
        
        res = self.client.post(url)
        self.assertEqual(res.status_code, 401)
        
        res = self.client.post(url, headers=self.generate_header())
        self.assertEqual(res.status_code, 422)
        
        mock_usecase.add_data.return_value = Exception('error')
        res = self.client.post(url, headers=self.generate_header(),json={'name': 'sample', 'price':0})
        self.assertEqual(res.status_code, 500)
        
        mock_usecase.add_data.return_value = {"code": 200}
        res = self.client.post(url, headers=self.generate_header(),json={'name': 'sample', 'price':0, 'usd_price': 0})
        self.assertEqual(res.status_code, 200)