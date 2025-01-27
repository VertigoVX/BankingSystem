# test_models.py
import unittest
from datetime import datetime
from app import create_app, db
from app import db, Transaction

class TestTransactionModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_transaction_creation(self):
        transaction = Transaction(
            id=1,
            amount=100.0,
            date=datetime.now(),
            type="credit",
            description="Test Transaction"
        )
        self.assertEqual(transaction.amount, 100.0)
        self.assertEqual(transaction.type, "credit")
        self.assertEqual(transaction.description, "Test Transaction")

if __name__ == "__main__":
    unittest.main()