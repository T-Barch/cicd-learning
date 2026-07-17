"""
<<<<<<< HEAD
Simple Flask API for CI/CD Learning.
=======
Simple Flask API for CI/CD Learning
>>>>>>> latest_branch
Usage: python backend_app.py
"""

import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
=======
# Load environment variables from .env
>>>>>>> latest_branch
load_dotenv()

app = Flask(__name__)

<<<<<<< HEAD
database_url = os.getenv("DATABASE_URL")

if database_url:
    if database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1,
        )
else:
    db_user = os.getenv("POSTGRES_USER")
    db_password = os.getenv("POSTGRES_PASSWORD")
    db_name = os.getenv("POSTGRES_DB")
    db_host = os.getenv("DB_HOST", "database")
    db_port = os.getenv("DB_PORT", "5432")

    if not all([db_user, db_password, db_name]):
        raise ValueError(
            "DATABASE_URL or "
            "(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB) "
            "must be configured."
        )

    database_url = (
        f"postgresql://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
=======
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
>>>>>>> latest_branch
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Item(db.Model):
<<<<<<< HEAD
    """Database model."""
=======
    """Database model for items."""
>>>>>>> latest_branch

    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
<<<<<<< HEAD
        """Convert item to dictionary."""
=======
        """Convert model to dictionary."""
>>>>>>> latest_branch
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
        }


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "instance": os.getenv("INSTANCE", "default"),
        }
    )


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
    )


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

<<<<<<< HEAD
        return jsonify(
            {
                "success": True,
                "item": new_item.to_dict(),
            }
        ), 201

    except Exception as exc:
        db.session.rollback()

        return jsonify(
            {
                "success": False,
                "error": str(exc),
            }
        ), 500
=======
        return (
            jsonify(
                {
                    "success": True,
                    "item": new_item.to_dict(),
                }
            ),
            201,
        )

    except Exception as exc:
        return (
            jsonify(
                {
                    "success": False,
                    "error": str(exc),
                }
            ),
            500,
        )
>>>>>>> latest_branch


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    """Return a specific item."""
<<<<<<< HEAD
    item = db.session.get(Item, item_id)

    if item is None:
        return jsonify(
            {
                "success": False,
                "error": "Item not found",
            }
        ), 404
=======
    item = Item.query.get(item_id)

    if not item:
        return (
            jsonify(
                {
                    "success": False,
                    "error": "Item not found",
                }
            ),
            404,
        )
>>>>>>> latest_branch

    return jsonify(
        {
            "success": True,
            "item": item.to_dict(),
        }
    )


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    """Delete a specific item."""
<<<<<<< HEAD
    item = db.session.get(Item, item_id)

    if item is None:
        return jsonify(
            {
                "success": False,
                "error": "Item not found",
            }
        ), 404
=======
    item = Item.query.get(item_id)

    if not item:
        return (
            jsonify(
                {
                    "success": False,
                    "error": "Item not found",
                }
            ),
            404,
        )
>>>>>>> latest_branch

    db.session.delete(item)
    db.session.commit()

    return jsonify(
        {
            "success": True,
            "message": "Item deleted",
        }
    )


@app.route("/metrics", methods=["GET"])
def metrics():
    """Prometheus metrics endpoint."""
    items_count = Item.query.count()

    return f"""# HELP items_total Total number of items
# TYPE items_total gauge
items_total {items_count}
"""


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.getenv("PORT", "5000"))
<<<<<<< HEAD

    app.run(
        host="0.0.0.0",
        port=port,
    )
=======
    app.run(host="0.0.0.0", port=port, debug=True)
>>>>>>> latest_branch
