import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from connexion import App
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.add_api("swagger.yml")

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        "error": e.name,
        "message": e.description
    }), e.code

# Error handler for 500 Internal Server Error
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }), 500

# Example route to test error handling
@app.route("/test-error")
def test_error():
    raise ValueError("This is a test error")

# Database configuration
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://admin:p@ssw0rd@localhost:5432/banking_system')
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app.app)

# Define the Transaction model
class Transaction(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    date = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)
    type = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "amount": float(self.amount),
            "date": self.date.isoformat(),
            "type": self.type,
            "description": self.description
        }

# Create the database tables
with app.app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")