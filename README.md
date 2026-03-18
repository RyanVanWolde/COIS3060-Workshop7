# COIS 3060-Workshop#7

A simple Task Manager REST API built with Python and Flask.
Used in COIS-3060H Lecture 9 Agentic SE Workshop.

## Endpoints

| Method | Path                    | Description              |
|--------|-------------------------|--------------------------|
| GET    | /tasks                  | List all tasks           |
| POST   | /tasks                  | Create a task            |
| GET    | /tasks/<id>             | Get a task by ID         |
| PATCH  | /tasks/<id>/complete    | Toggle task completion   |
| DELETE | /tasks/<id>             | Delete a task            |

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Running Tests

```bash
pytest tests/ -v
```

## Known Issues

See the GitHub Issues tab. Three issues are documented:
- Issue #1: Missing input validation (bug)
- Issue #2: Complete toggle always sets True (bug)
- Issue #3: No pagination on GET /tasks (missing feature)
