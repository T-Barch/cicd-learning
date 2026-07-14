import pytest
from backend_app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


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