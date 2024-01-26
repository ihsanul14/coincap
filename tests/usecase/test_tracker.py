import unittest
from unittest.mock import Mock
from usecase.tracker.tracker import TrackerUsecase
from repository.database.tracker.sqllite import TrackerSqllite
from repository.models.tracker import Tracker

class MockTrackerSqllite:
    def get_data(self):
        return []
    
    def upsert_data(self):
        return 
    
    def delete_data(self):
        return {}

    
class TestTrackerUsecase(unittest.TestCase):
    sample_coin = "sample_coin"
    def test_get_data(self):
        mock_repository = Mock(spec=TrackerSqllite)
        mock_repository.get_data.return_value = [
            Tracker()
        ]
        tracker_usecase = TrackerUsecase()
        tracker_usecase.repository = mock_repository
        result = tracker_usecase.get_data()
        self.assertEqual(result['code'], 200)
    
    def test_add_data(self):
        mock_repository = Mock(spec=TrackerSqllite)
        tracker_usecase = TrackerUsecase()
        tracker_usecase.repository = mock_repository
        
        # upsert available coin from source
        request = {
            'name' : '',
            'price': 10
        }
        result = tracker_usecase.add_data(request)
        self.assertEqual(result['code'], 200)
        
        # upsert new coin
        request = {
            'name' : self.sample_coin,
            'price': 10
        }
        result = tracker_usecase.add_data(request)
        self.assertEqual(result['code'], 200)

    def test_delete_data(self):
        mock_repository = Mock(spec=TrackerSqllite)
        tracker_usecase = TrackerUsecase()
        tracker_usecase.repository = mock_repository
        
        request = {'name': self.sample_coin}
        result = tracker_usecase.delete_data(request)
        self.assertEqual(result['code'], 200)
    