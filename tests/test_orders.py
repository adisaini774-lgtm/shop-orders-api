from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_order_with_welcome10():
    response = client.post("/orders", json={"product_id": "p1", "quantity": 2, "coupon": "WELCOME10"})
    assert response.status_code == 201

