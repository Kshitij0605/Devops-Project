from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, completed FROM tasks")
    tasks = [{"id": row[0], "task": row[1], "completed": bool(row[2])} for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_text = request.json.get("task")
    if not task_text:
        return jsonify({"error": "Task cannot be empty"}), 400
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task_text,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added successfully"})

@app.route("/delete/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task deleted successfully"})

@app.route("/update/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    completed = request.json.get("completed", False)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task updated successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    # This is a test change to trigger CI/CD
    #My name is kshitij
    #jnvwfnlqk
    #testing
    #
    # vtycr
    


