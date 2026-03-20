# Task Manager API — Agent Instructions

## Project
Python Flask REST API for task management. In-memory storage (no database).

## Stack
- Python 3.11+
- Flask 3.x
- pytest for testing

## Run tests
```
pytest tests/ -v
```

## Run the app
```
python app.py
```

## Non-goals
# The agent should not change the naming scheme of the variables, functions, or tasks. The agent should only chnage code relevant to addressing issues, it should not try to improve anything else except what directed.
# What should the agent NOT do? Think about:
# - Files it must not modify
# - Behaviour it must not change
# - Dependencies it must not add

## Constraints
# The agent should keep the code in memory, it should not try to make a database. The tasks should be stored as global variables for referencing. Must respond in JSON, with the exception of DELETE.
# What rules must always be followed?
# Example: 'All monetary values must be integer cents, never floats'
# What are the rules specific to this codebase?

