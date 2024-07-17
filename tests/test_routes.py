import unittest
from app import app, db
from app.models import Train
import json

class TestTrainRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_train(self):
        # Test adding a train via POST request
        response = self.app.post('/admin/trains', json={
            'source': 'Station A',
            'destination': 'Station B',
            'total_seats': 100
        })
        self.assertEqual(response.status_code, 201)

        # Verify train is added to the database
        train = Train.query.filter_by(source='Station A', destination='Station B').first()
        self.assertIsNotNone(train)
        self.assertEqual(train.total_seats, 100)

    def test_get_trains_between_stations(self):
        # Add some trains to the database for testing
        train1 = Train(source='Station A', destination='Station B', total_seats=50)
        train2 = Train(source='Station A', destination='Station C', total_seats=75)
        db.session.add_all([train1, train2])
        db.session.commit()

        # Test getting trains between stations via GET request
        response = self.app.get('/user/trains?source=Station A&destination=Station B')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['source'], 'Station A')
        self.assertEqual(data[0]['destination'], 'Station B')

if __name__ == '__main__':
    unittest.main()
