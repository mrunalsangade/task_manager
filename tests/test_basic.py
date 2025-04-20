# tests/test_basic.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_index_status_code(client):
    """
    Simply verify that GET / returns HTTP 200.
    """
    response = client.get('/')
    assert response.status_code == 200
