"""
Task Manager API
A simple REST API for managing tasks.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task store (no database needed for this workshop)
tasks = []
next_id = 1


# GET /tasks
# BUG: Returns ALL tasks with no limit. Will fail under load.
# MISSING FEATURE: No pagination support (?page=1&limit=10)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})


# POST /tasks
# BUG: No input validation. If 'title' is missing, raises KeyError -> 500 crash.
@app.route("/tasks", methods=["POST"])
def create_task():
    global next_id
    data = request.get_json()
    task = {
        "id": next_id,
        "title": data["title"],           # KeyError if "title" missing -> 500
        "description": data.get("description", ""),
        "completed": False,
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


# GET /tasks/<id>
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


# PATCH /tasks/<id>/complete
# BUG: Always sets completed=True. Never toggles back to False.
@app.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    task["completed"] = True   # BUG: should be  not task["completed"]
    return jsonify(task)


# DELETE /tasks/<id>
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
