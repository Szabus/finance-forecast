from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Finance Forecast App"}

def test_predict_expense():
    payload = {
        "food": 100.0,
        "rent": 500.0,
        "transport": 50.0
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    expected_total = (100.0 + 500.0 + 50.0) * 1.05
    assert response.json() == {"predicted_total": expected_total}
