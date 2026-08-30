from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.repositories.in_memory import db

client = TestClient(app)

def test_login_success():
    response = client.post("/api/auth/login", json={"username": "owner", "password": "admin123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["role"] == "OWNER"

def test_inventory_flow():
    login_res = client.post("/api/auth/login", json={"username": "manager", "password": "admin123"})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    prod_res = client.get("/api/inventory/products", headers=headers)
    assert prod_res.status_code == 200
    products = prod_res.json()
    assert len(products) > 0

    new_prod = {
        "name": "USB Flash Drive 64GB",
        "sku": "ELE-003",
        "category_id": "cat-1",
        "cost_price": 6.5,
        "selling_price": 12.0,
        "stock_quantity": 25,
        "min_stock_level": 5
    }
    create_res = client.post("/api/inventory/products", json=new_prod, headers=headers)
    assert create_res.status_code == 201
    created = create_res.json()
    assert created["sku"] == "ELE-003"
    assert created["stock_status"] == "IN_STOCK"

    adj_res = client.post(f"/api/inventory/products/{created['id']}/adjust-stock", json={
        "quantity_change": -22,
        "type": "SALE",
        "reason": "Direct store sale"
    }, headers=headers)
    assert adj_res.status_code == 200
    adjusted = adj_res.json()
    assert adjusted["stock_quantity"] == 3
    assert adjusted["stock_status"] == "LOW_STOCK"
