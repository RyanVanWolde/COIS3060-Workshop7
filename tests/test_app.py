"""
Tests for Task Manager API.
NOTE: Only two tests exist. More are needed (see GitHub Issues).
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import app as app_module
from app import app


@pytest.fixture(autouse=True)
def reset_state():
    """Reset in-memory state before each test."""
    app_module.tasks.clear()
    app_module.next_id = 1
    yield


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    """Test creating a task successfully."""
    response = client.post(
        "/tasks",
        json={"title": "Fix the login bug", "description": "Repro in production"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Fix the login bug"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks_empty(client):
    """Test GET /tasks returns empty list when no tasks exist."""
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert data["tasks"] == []


def test_complete_task_toggles_completed_state(client):
    """Test PATCH /tasks/<id>/complete toggles completed on each call."""
    create_response = client.post(
        "/tasks",
        json={"title": "Toggle completion", "description": "Verify toggle behavior"},
    )
    task_id = create_response.get_json()["id"]

    first_response = client.patch(f"/tasks/{task_id}/complete")
    assert first_response.status_code == 200
    assert first_response.get_json()["completed"] is True

    second_response = client.patch(f"/tasks/{task_id}/complete")
    assert second_response.status_code == 200
    assert second_response.get_json()["completed"] is False

    third_response = client.patch(f"/tasks/{task_id}/complete")
    assert third_response.status_code == 200
    assert third_response.get_json()["completed"] is True
