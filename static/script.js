 document.addEventListener("DOMContentLoaded", loadTasks);

function loadTasks() {
    fetch("/tasks")
    .then(response => response.json())
    .then(tasks => {
        let taskList = document.getElementById("task-list");
        taskList.innerHTML = "";
        tasks.forEach(task => {
            let listItem = document.createElement("li");
            listItem.innerHTML = `<span class="task-details">
                                    <input type="checkbox" ${task.completed ? "checked" : ""} onchange="updateTask(${task.id}, this.checked)">
                                    ${task.task}
                                  </span>
                                  <button class="edit-btn" onclick="editTask(${task.id}, '${task.task}')">Edit</button>
                                  <button class="delete-btn" onclick="removeTask(${task.id})">Delete</button>`;
            taskList.appendChild(listItem);
        });
    });
}

function addTask() {
    let taskInput = document.getElementById("task-input").value;
    if (taskInput === "") {
        alert("Please enter a task");
        return;
    }

    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: taskInput })
    }).then(() => {
        document.getElementById("task-input").value = "";
        loadTasks();
    });
}

function removeTask(taskId) {
    fetch(`/delete/${taskId}`, { method: "DELETE" })
    .then(() => loadTasks());
}

function updateTask(taskId, completed) {
    fetch(`/update/${taskId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed: completed })
    }).then(() => loadTasks());
}

function editTask(taskId, currentText) {
    let newText = prompt("Edit task:", currentText);
    if (newText) {
        fetch(`/update/${taskId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ task: newText })
        }).then(() => loadTasks());
    }
}
