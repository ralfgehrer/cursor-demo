import uuid
from typing import Dict

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.core.config import settings
from app.tests.utils.item import create_random_item


def test_create_item(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"title": "Foo", "description": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/items/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content
    assert "owner_id" in content


def test_read_item(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    response = client.get(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == item.title
    assert content["description"] == item.description
    assert content["id"] == str(item.id)
    assert content["owner_id"] == str(item.owner_id)


def test_read_item_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/items/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Item not found"


def test_read_item_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    response = client.get(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_read_items(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    create_random_item(db)
    create_random_item(db)
    response = client.get(
        f"{settings.API_V1_STR}/items/",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content["data"]) >= 2


def test_update_item(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert content["id"] == str(item.id)
    assert content["owner_id"] == str(item.owner_id)


def test_update_item_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/items/{uuid.uuid4()}",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Item not found"


def test_update_item_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    data = {"title": "Updated title", "description": "Updated description"}
    response = client.put(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=normal_user_token_headers,
        json=data,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_delete_item(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    response = client.delete(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["message"] == "Item deleted successfully"


def test_delete_item_not_found(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.delete(
        f"{settings.API_V1_STR}/items/{uuid.uuid4()}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 404
    content = response.json()
    assert content["detail"] == "Item not found"


def test_delete_item_not_enough_permissions(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session
) -> None:
    item = create_random_item(db)
    response = client.delete(
        f"{settings.API_V1_STR}/items/{item.id}",
        headers=normal_user_token_headers,
    )
    assert response.status_code == 400
    content = response.json()
    assert content["detail"] == "Not enough permissions"


def test_export_items_csv(
    client: TestClient,
    db_session: Session,
    normal_user: User,
    superuser: User,
    normal_user_token_headers: Dict[str, str],
    superuser_token_headers: Dict[str, str]
) -> None:
    """Test CSV export endpoint with various permissions and pagination."""
    # Create test items
    item1 = create_random_item(db_session, owner_id=normal_user.id)
    item2 = create_random_item(db_session, owner_id=normal_user.id)
    item3 = create_random_item(db_session, owner_id=superuser.id)

    # Test unauthorized access
    r = client.get(f"{settings.API_V1_STR}/items/export-csv")
    assert r.status_code == 401

    # Test normal user - should only see their items
    r = client.get(f"{settings.API_V1_STR}/items/export-csv", headers=normal_user_token_headers)
    assert r.status_code == 200
    assert r.headers["Content-Type"] == "text/csv"
    assert r.headers["Content-Disposition"] == "attachment; filename=items.csv"
    
    content = r.content.decode()
    csv_lines = content.strip().split("\n")
    assert len(csv_lines) == 3  # Header + 2 items
    assert csv_lines[0] == "id,title,description,owner_id"
    assert item1.id in content and item2.id in content
    assert item3.id not in content

    # Test superuser - should see all items
    r = client.get(f"{settings.API_V1_STR}/items/export-csv", headers=superuser_token_headers)
    assert r.status_code == 200
    content = r.content.decode()
    csv_lines = content.strip().split("\n")
    assert len(csv_lines) == 4  # Header + 3 items
    assert item1.id in content and item2.id in content and item3.id in content

    # Test pagination
    r = client.get(f"{settings.API_V1_STR}/items/export-csv?skip=1&limit=1", headers=superuser_token_headers)
    assert r.status_code == 200
    content = r.content.decode()
    csv_lines = content.strip().split("\n")
    assert len(csv_lines) == 2  # Header + 1 item

    # Test error cases
    r = client.get(f"{settings.API_V1_STR}/items/export-csv?skip=-1", headers=normal_user_token_headers)
    assert r.status_code == 400
    assert r.json()["detail"] == "Skip must be >= 0"

    r = client.get(f"{settings.API_V1_STR}/items/export-csv?limit=0", headers=normal_user_token_headers) 
    assert r.status_code == 400
    assert r.json()["detail"] == "Limit must be > 0"
