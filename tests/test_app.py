"""
Tests for Task Manager API.
NOTE: Only two tests exist. More are needed (see GitHub Issues).
"""
import os
import sys

import pytest

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


def test_create_task_missing_title_returns_bad_request(client):
    response = client.post("/tasks", json={"description": "Missing title"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "title is required"}


def test_create_task_empty_title_returns_bad_request(client):
    response = client.post("/tasks", json={"title": "", "description": "Empty title"})

    assert response.status_code == 400
    assert response.get_json() == {"error": "title is required"}


def test_get_tasks_empty(client):
    """Test GET /tasks returns empty list when no tasks exist."""
    response = client.get("/tasks")
    assert response.status_code == 200
    data = response.get_json()
    assert data["tasks"] == []
