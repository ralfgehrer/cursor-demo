from typing import Dict
from fastapi.testclient import TestClient

def test_export_items_csv(client: TestClient, superuser_token_headers: Dict[str, str]):
    response = client.get("/api/v1/items/export", headers=superuser_token_headers)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/csv; charset=utf-8" 