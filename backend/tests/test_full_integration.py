from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def get_auth_headers():
    login_res = client.post("/api/auth/login", json={"username": "owner", "password": "admin123"})
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_full_system_integration():
    headers = get_auth_headers()

    me_res = client.get("/api/auth/me", headers=headers)
    assert me_res.status_code == 200
    assert me_res.json()["role"] == "OWNER"

    dash_res = client.get("/api/dashboard/summary", headers=headers)
    assert dash_res.status_code == 200
    assert "todays_sales" in dash_res.json()

    fin_res = client.get("/api/finance/summary", headers=headers)
    assert fin_res.status_code == 200
    assert "net_profit" in fin_res.json()

    sa_res = client.get("/api/analytics/sales", headers=headers)
    assert sa_res.status_code == 200
    ia_res = client.get("/api/analytics/inventory", headers=headers)
    assert ia_res.status_code == 200

    alt_res = client.get("/api/alerts", headers=headers)
    assert alt_res.status_code == 200
    assert isinstance(alt_res.json(), list)

    rep_res = client.post("/api/reports/sales", json={"start_date": "2026-08-01"}, headers=headers)
    assert rep_res.status_code == 200
    assert "rows" in rep_res.json()
