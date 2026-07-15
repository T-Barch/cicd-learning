"""Unit tests for the Flask backend."""

import pytest
from backend_app import app, db


@pytest.fixture
def client():
    """Create a test client for the Flask application and setup/teardown tables."""
    app.config["TESTING"] = True

    # Establish application context to create the database schema in Postgres
    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    # Clean up the database tables after the tests finish
    with app.app_context():
        db.drop_all()


def test_health_endpoint(client):
    """Test the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_get_items_endpoint(client):
    """Test the /api/items endpoint."""
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.get_json()
    assert "items" in data
    assert "count" in data