import pytest
from app import app  # assuming your Flask app is in app.py

def test_root_route():
    # Create a test client
    tester = app.test_client()
    response = tester.get('/')
    
    # Check status code
    assert response.status_code == 200
    
    # Check response data
    assert b"Hello from Jenkins CI/CD pipeline!" in response.data

