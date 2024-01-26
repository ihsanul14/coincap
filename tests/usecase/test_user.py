import unittest
from unittest.mock import Mock
from usecase.user.user import UserUsecase
from repository.database.user.sqllite import UserSqllite

class MockUserSqllite:
    def get_data_by_id(self):
        return {
            'email': "",
            'password': ''
        }

    def add_data(self):
        return {}
    
    def delete_data(self):
        return {}

    
class TestUserUsecase(unittest.TestCase):
    sample_email = "sample@mail.com"
    def test_signup(self):
        mock_repository = Mock(spec=UserSqllite)
        mock_repository.add_data.return_value = []
        user_usecase = UserUsecase()
        user_usecase.repository = mock_repository
        
        request = {
            'email': self.sample_email
        }
        result = user_usecase.sign_up(request)
        self.assertEqual(result['code'], 200)
    
    def test_signin(self):
        mock_repository = Mock(spec=UserSqllite)
        mock_repository.get_data_by_id.return_value = {
            'email': self.sample_email,
            'password': ''
        }
        
        mock_repository.sign_in.return_value = {}
        user_usecase = UserUsecase()
        user_usecase.repository = mock_repository
        
        request = {
            'email': self.sample_email
        }
        result = user_usecase.sign_in(request)
        self.assertEqual(result['code'], 200)
  
    def test_delete_data(self):
        mock_repository = Mock(spec=UserSqllite)
        mock_repository.delete_data.return_value = []
        user_usecase = UserUsecase()
        user_usecase.repository = mock_repository
        
        request = {'email': self.sample_email}
        result = user_usecase.delete_data(request)
        self.assertEqual(result['code'], 200)
    