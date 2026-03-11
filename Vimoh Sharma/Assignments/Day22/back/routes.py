from flask import Blueprint, request, jsonify
from models import db, Task

task_routes = Blueprint("task_routes", __name__)

@task_routes.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    task = Task(
        title=data["title"],
        priority=data["priority"]
    )

    db.session.add(task)
    db.session.commit()

    return jsonify(task.to_dict()), 201


@task_routes.route("/tasks", methods=["GET"])
def get_tasks():

    priority = request.args.get("priority")
    completed = request.args.get("completed")

    query = Task.query

    if priority:
        query = query.filter(Task.priority == priority)

    if completed:
        completed_bool = completed.lower() == "true"
        query = query.filter(Task.completed == completed_bool)

    tasks = query.order_by(Task.created_at.desc()).all()

    return jsonify([t.to_dict() for t in tasks])

@task_routes.route("/tasks/<int:id>/toggle", methods=["PUT"])
def toggle_task(id):

    task = Task.query.get_or_404(id)

    task.completed = not task.completed

    db.session.commit()

    return jsonify(task.to_dict())

@task_routes.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})
