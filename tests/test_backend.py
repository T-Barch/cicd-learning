"""Unit tests for the Flask backend."""

import pytest
from backend_app import Item, app, db


@pytest.fixture
def client():
    """Create a test client for the Flask application and setup/teardown tables."""
    app.config["TESTING"] = True

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()


def test_health_endpoint(client):
    """Test the /health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_get_items_empty(client):
    """Test fetching items when the database is empty."""
    response = client.get("/api/items")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["count"] == 0
    assert data["items"] == []


def test_create_item(client):
    """Test creating a new item via POST /api/items."""
    response = client.post(
        "/api/items",
        json={"name": "Integration Test Item"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["success"] is True
    assert data["item"]["name"] == "Integration Test Item"
    assert "id" in data["item"]


def test_create_item_missing_name(client):
    """Test POST /api/items error handling when name is missing."""
    response = client.post("/api/items", json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert data["error"] == "name required"


def test_get_specific_item(client):
    """Test fetching a specific item by ID."""
    # Create item directly in db
    with app.app_context():
        item = Item(name="Test Item")
        db.session.add(item)
        db.session.commit()
        item_id = item.id

    response = client.get(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["item"]["id"] == item_id
    assert data["item"]["name"] == "Test Item"


def test_delete_item(client):
    """Test deleting an item by ID."""
    with app.app_context():
        item = Item(name="Item to Delete")
        db.session.add(item)
        db.session.commit()
        item_id = item.id

    response = client.delete(f"/api/items/{item_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["message"] == "Item deleted"