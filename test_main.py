from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

data = {
    "name": "Purvi-Thakkar",
    "expiry_date": "Now",
    "description": "My try on FirstAPI",
    "price": "Price"

}

def test_create_supermarket():
    response = client.post("/supermarket/", json=data)
    assert response.status_code == 200
    assert response.json() == data

def test_get_all_supermarket():
    response = client.get("/supermarket/", json=data)
    assert response.status_code == 200
    assert data in response.json()

def test_get_supermarket():
    response = client.get("/supermarket/0")
    assert response.status_code == 200
    assert response.json() == data

def test_update_supermarket():
    response = client.put("/supermarket/0", json = {
        "name": "Test",
        "expiry_date": "Now",
        "description": "Python",
        "price": "Price"
    })
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test",
        "expiry_date": "Now",
        "description": "Python",
        "price": "Price"
    }

def test_delete_supermarket():
    response = client.delete("/supermarket/0")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Test",
        "expiry_date": "Now",
        "description": "Python",
        "price": "Price"
    }