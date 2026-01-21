import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health_check():
    """Test the /health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_health_check_returns_json():
    """Test that /health returns JSON content type"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
