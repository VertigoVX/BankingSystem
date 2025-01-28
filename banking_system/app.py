import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from connexion import App
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

flask_app = Flask(__name__)
app = App(__name__, specification_dir="./")
app.add_api("swagger.yml")

# Database config
flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://admin:p@ssw0rd@localhost:5432/banking_system')
flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return jsonify({
        "error": e.name,
        "message": e.description
    }), e.code

# Error handler for 500 
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "message": "An unexpected error occurred."
    }), 500


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
with flask_app.app_context():
    db.create_all()

# Example route test
@flask_app.route("/test-error")
def test_error():
    raise ValueError("This is a test error")

if __name__ == "__main__":
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    app.run(flask_app, debug=debug_mode, host="0.0.0.0")
