from fastapi.testclient import TestClient
from fastapi import FastAPI
from issues_router import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_create_issue():
    response = client.post("/", json={"title": "Test Issue", "description": "This is a test issue."})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Issue"
    assert data["description"] == "This is a test issue."
    assert "id" in data


def test_read_issue():
    response = client.get("/")
    assert response.status_code == 200
    issues = response.json()
    assert isinstance(issues, list)


def test_update_issue():
    # Create an issue first for the sake of this test
    response = client.post("/", json={"title": "Test Issue", "description": "Update this issue."})
    issue_id = response.json()["id"]

    updated_data = {"title": "Updated Test Issue", "description": "Issue has been updated."}
    response = client.put(f"/{issue_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_data["title"]
    assert data["description"] == updated_data["description"]


def test_delete_issue():
    # Create an issue first for the sake of this test
    response = client.post("/", json={"title": "Test Issue", "description": "Delete this issue."})
    issue_id = response.json()["id"]

    response = client.delete(f"/{issue_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Issue deleted"

    # Try to delete again to get a 404
    response = client.delete(f"/{issue_id}")
    assert response.status_code == 404
