"""
Simple Flask API for CI/CD Learning
Usage: python backend_app.py
"""

import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, OperationalError, ProgrammingError

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Fetch credentials from environment
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")

# Network defaults (not secrets)
DB_HOST = os.getenv("DB_HOST", "database")
DB_PORT = os.getenv("DB_PORT", "5432")

# Fail fast if required database credentials are missing
if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError(
        "Database credentials (POSTGRES_USER, "
        "POSTGRES_PASSWORD, POSTGRES_DB) "
        "must be fully configured in the environment!"
    )

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
    """Database model for items."""

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert model to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
        }


# CRITICAL FIX: Ensure tables are created safely when Gunicorn initializes multiple workers
with app.app_context():
    try:
        db.create_all()
        print("Database tables initialized successfully!")
    except (ProgrammingError, OperationalError, IntegrityError) as e:
        # Ignore duplicate table/type errors from concurrent Gunicorn workers
        print("Tables already created or being created by another worker.")


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "instance": os.getenv("INSTANCE", "default"),
        }
    ), 200


@app.route("/api/items", methods=["GET"])
def get_items():
    """Return all items."""
    items = Item.query.all()

    return jsonify(
        {
            "success": True,
            "items": [item.to_dict() for item in items],
            "count": len(items),
        }
    ), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    """Create a new item."""
    try:
        payload = request.get_json()

        if not payload or "name" not in payload:
            return jsonify(
                {
                    "success": False,
                    "error": "name required",
                }
            ), 400

        new_item = Item(name=payload["name"])

        db.session.add(new_item)
        db.session.commit()

        return jsonify({"success": True, "item": new_item.to_dict()}), 201

    except Exception as exc:
        return jsonify({"success": False, "error": str(exc)}), 500


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """Return a specific item."""
    item = Item.query.get(item_id)

    if not item:
        return jsonify({"success": False, "error": "Item not found"}), 404

    return jsonify({"success": True, "item": item.to_dict()}), 200


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete a specific item."""
    item = Item.query.get(item_id)

    if not item:
        return jsonify({"success": False, "error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"success": True, "message": "Item deleted"}), 200


@app.route("/metrics", methods=["GET"])
def metrics():
    """Prometheus metrics endpoint."""
    items_count = Item.query.count()

    return f"""# HELP items_total Total number of items
# TYPE items_total gauge
items_total {items_count}
"""


# This block is only used if running locally with `python backend_app.py`
if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)