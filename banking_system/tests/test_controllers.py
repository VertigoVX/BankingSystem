# test_controllers.py
import unittest
from app import create_app, db
from controllers.transaction_controller import add_transaction, get_transactions

class TestTransactionController(unittest.TestCase):
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

    def test_add_transaction(self):
        with self.app.app_context():
            transaction_data = {
                "amount": 100.0,
                "type": "credit",
                "description": "Test Transaction"
            }
            transaction = add_transaction(transaction_data)
            self.assertEqual(transaction.amount, 100.0)
            self.assertEqual(transaction.type, "credit")

    def test_get_transactions(self):
        with self.app.app_context():
            transaction_data = {
                "amount": 100.0,
                "type": "credit",
                "description": "Test Transaction"
            }
            add_transaction(transaction_data)
            transactions = get_transactions()
            self.assertEqual(len(transactions), 1)
            self.assertEqual(transactions[0].amount, 100.0)

if __name__ == "__main__":
    unittest.main()