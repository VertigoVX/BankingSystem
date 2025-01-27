from datetime import datetime
from typing import Optional

class Transaction:
    def __init__(self, id: int, amount: float, date: str, type: str, description: str):
        self.id = id
        self.amount = amount
        self.date = date
        self.type = type
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "date": self.date,
            "type": self.type,
            "description": self.description
        }