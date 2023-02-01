import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

# Function to add a task
def get_cursor():
    con = sqlite3.connect('todolist1.db')
    cursor = con.cursor()
    return cursor

def add_task(task, description):
    cursor = get_cursor()
    cursor.execute("""
    INSERT INTO tasks (task, description)
    VALUES (?, ?)
    """, (task, description))
    cursor.connection.commit()

# Function to retrieve all tasks
def get_all_tasks():
    cursor = get_cursor()
    cursor.execute("""
    SELECT * FROM tasks
    """)
    return cursor.fetchall()

# Function to update a task
def update_task(task_id, completed):
    cursor = get_cursor()
    cursor.execute("""
    UPDATE tasks
    SET completed = ?
    WHERE id = ?
    """, (completed, task_id))
    cursor.connection.commit()

# Function to delete a task
def delete_task(task_id):
    cursor = get_cursor()
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = ?
    """, (task_id,))
    cursor.connection.commit()

# Flask app
app = Flask(__name__)
CORS(app)

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks), 200

# Add a task
@app.route("/tasks", methods=["POST"])
def add_new_task():
    task = request.json["task"]
    description = request.json["description"]
    add_task(task, description)
    return jsonify({"message": "Task added successfully"}), 201

# Update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_existing_task(task_id):
    completed = request.json["completed"]
    update_task(task_id, completed)
    return jsonify({"message": "Task updated successfully"}), 200

# Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_existing_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
