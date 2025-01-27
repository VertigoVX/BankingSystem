from datetime import datetime
from typing import List, Optional
from app import db, Transaction
from flask import jsonify

def validate_transaction_data(data: dict) -> Optional[str]:
    if "amount" not in data or not isinstance(data["amount"], (int, float)):
        return "Amount must be a number."
    if "type" not in data or data["type"] not in ["credit", "debit"]:
        return "Type must be 'credit' or 'debit'."
    if "description" not in data or not isinstance(data["description"], str):
        return "Description must be a string."
    return None

def add_transaction(data: dict) -> Transaction:
    transaction = Transaction(
        amount=data["amount"],
        type=data["type"],
        description=data["description"]
    )
    db.session.add(transaction)
    db.session.commit()
    return transaction

def get_transactions() -> List[Transaction]:
    return Transaction.query.all()

def get_transaction(transaction_id: int) -> Optional[Transaction]:
    return Transaction.query.get(transaction_id)

def update_transaction(transaction_id: int, data: dict) -> Optional[Transaction]:
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        transaction.amount = data.get("amount", transaction.amount)
        transaction.type = data.get("type", transaction.type)
        transaction.description = data.get("description", transaction.description)
        db.session.commit()
    return transaction

def delete_transaction(transaction_id: int) -> bool:
    transaction = Transaction.query.get(transaction_id)
    if transaction:
        db.session.delete(transaction)
        db.session.commit()
        return True
    return False

# Error Handling
def add_transaction(data):
    error = validate_transaction_data(data)
    if error:
        return jsonify({"error": "Invalid data", "message": error}), 400

    try:
        transaction = Transaction(
            amount=data["amount"],
            type=data["type"],
            description=data["description"]
        )
        db.session.add(transaction)
        db.session.commit()
        return jsonify(transaction.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500

def get_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Not found", "message": "Transaction not found"}), 404
    return jsonify(transaction.to_dict())

def update_transaction(transaction_id, data):
    error = validate_transaction_data(data)
    if error:
        return jsonify({"error": "Invalid data", "message": error}), 400

    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Not found", "message": "Transaction not found"}), 404

    try:
        transaction.amount = data.get("amount", transaction.amount)
        transaction.type = data.get("type", transaction.type)
        transaction.description = data.get("description", transaction.description)
        db.session.commit()
        return jsonify(transaction.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500

def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({"error": "Not found", "message": "Transaction not found"}), 404

    try:
        db.session.delete(transaction)
        db.session.commit()
        return "", 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error", "message": str(e)}), 500