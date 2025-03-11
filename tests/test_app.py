# tests/test_app.py

import pytest
from app import app  # Ensure this import matches your application's structure

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test if the homepage loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List' in response.data  # Adjust based on your homepage content
