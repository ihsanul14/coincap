import unittest
from unittest.mock import MagicMock, patch
from repository.database.user.sqllite import UserSqllite
from repository.models.user import User
from framework.database.database import Database

class MockSqllite:
    def get_data(self):
        return []
    
    def upsert_data(self):
        return 
    
    def delete_data(self):
        return {}

    
class TestTrackerRepository(unittest.TestCase):
    def test_get_data(self):
        mock_engine = MagicMock()
        mock_sessionmaker = MagicMock()
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.one.return_value = [User(email="test")]
        mock_sessionmaker.return_value.__enter__.return_value = mock_session

        user_sqllite = UserSqllite()
        user_sqllite.db = mock_engine
        result = user_sqllite.get_data_by_id({'email': 'test', 'password': 'test'})
        self.assertIsNotNone(result)
        
    def test_add_data(self):
        mock_engine = MagicMock()
        mock_sessionmaker = MagicMock()
        mock_session = MagicMock()
        mock_session.add.return_value = {}
        mock_sessionmaker.return_value.__enter__.return_value = mock_session

        user_sqllite = UserSqllite()
        user_sqllite.db = mock_engine
        result = user_sqllite.add_data({'email': 'test', 'password': 'test'})
        self.assertIsNotNone(result)
    
    def test_sign_in(self):
        user_sqllite = UserSqllite()
        res = user_sqllite.sign_in(User(email="test"))
        self.assertIsNotNone(res['token'], 3)
        token_arr = res['token'].split('.')
        self.assertEqual(len(token_arr), 3)
        