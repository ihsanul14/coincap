import unittest
from unittest.mock import MagicMock, patch
from repository.database.tracker.sqllite import TrackerSqllite
from repository.models.tracker import Tracker

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
        mock_session.query.return_value.all.return_value = [Tracker(name="test")]
        mock_sessionmaker.return_value.__enter__.return_value = mock_session

        tracker_sqllite = TrackerSqllite()
        tracker_sqllite.db = mock_engine
        result = tracker_sqllite.get_data()
        self.assertIsNotNone(result)
        
    def test_add_data(self):
        mock_engine = MagicMock()
        mock_sessionmaker = MagicMock()
        mock_session = MagicMock()
        mock_session.add.return_value.commit.return_value = {}
        mock_sessionmaker.return_value.__enter__.return_value = mock_session

        tracker_sqllite = TrackerSqllite()
        tracker_sqllite.db = mock_engine
        result = tracker_sqllite.add_data({'name': 'test', 'price': 0, 'usd_price': ''})
        self.assertIsNotNone(result)

    def test_update_data(self):
        mock_engine = MagicMock()
        mock_sessionmaker = MagicMock()
        mock_session = MagicMock()
        mock_session.query.return_value.filter.return_value.one.return_value = {}
        mock_sessionmaker.return_value.__enter__.return_value = mock_session

        tracker_sqllite = TrackerSqllite()
        tracker_sqllite.db = mock_engine
        result = tracker_sqllite.update_data({'name': 'test', 'price': 10, 'usd_price': ''})
        self.assertIsNotNone(result)
        