import uuid
import csv
from io import StringIO

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.core.config import settings
from app.tests.utils.item import create_random_item
from app.models.user import User


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


def test_export_csv_items_superuser(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create test items
    item1 = create_random_item(db)
    item2 = create_random_item(db)
    
    response = client.get(
        f"{settings.API_V1_STR}/items/export-csv",
        headers=superuser_token_headers,
    )
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/csv"
    assert response.headers["Content-Disposition"] == "attachment; filename=items.csv"
    
    content = response.content.decode()
    reader = csv.reader(StringIO(content))
    rows = list(reader)
    
    # Check headers
    assert rows[0] == ["id", "title", "description", "owner_id", "created_at"]
    
    # Check data
    assert len(rows) == 3  # Header + 2 items
    assert any(str(item1.id) in row for row in rows)
    assert any(str(item2.id) in row for row in rows)


def test_export_csv_items_normal_user(
    client: TestClient, normal_user_token_headers: dict[str, str], db: Session, normal_user: User
) -> None:
    # Create items for different users
    user_item = create_random_item(db, owner_id=normal_user.id)
    other_item = create_random_item(db)  # Different owner
    
    response = client.get(
        f"{settings.API_V1_STR}/items/export-csv",
        headers=normal_user_token_headers,
    )
    
    assert response.status_code == 200
    content = response.content.decode()
    reader = csv.reader(StringIO(content))
    rows = list(reader)
    
    # Should only see own items
    assert len(rows) == 2  # Header + 1 item
    assert any(str(user_item.id) in row for row in rows)
    assert not any(str(other_item.id) in row for row in rows)


def test_export_csv_items_pagination(
    client: TestClient, superuser_token_headers: dict[str, str], db: Session
) -> None:
    # Create 3 items
    items = [create_random_item(db) for _ in range(3)]
    
    # Test with limit=2
    response = client.get(
        f"{settings.API_V1_STR}/items/export-csv?skip=0&limit=2",
        headers=superuser_token_headers,
    )
    
    content = response.content.decode()
    reader = csv.reader(StringIO(content))
    rows = list(reader)
    
    assert len(rows) == 3  # Header + 2 items


def test_export_csv_items_invalid_pagination(
    client: TestClient, superuser_token_headers: dict[str, str]
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/items/export-csv?skip=-1",
        headers=superuser_token_headers,
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid pagination parameters. Skip must be >= 0 and limit must be > 0"

    response = client.get(
        f"{settings.API_V1_STR}/items/export-csv?limit=0",
        headers=superuser_token_headers,
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid pagination parameters. Skip must be >= 0 and limit must be > 0"
