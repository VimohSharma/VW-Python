import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {

  const [tasks, setTasks] = useState([]);
  const [priority, setPriority] = useState("");
  const [completed, setCompleted] = useState(false);

  const fetchTasks = async () => {

    let url = "http://127.0.0.1:5000/tasks";

    let params = [];

    if (priority) {
      params.push(`priority=${priority}`);
    }

    if (completed) {
      params.push(`completed=true`);
    }

    if (params.length > 0) {
      url += "?" + params.join("&");
    }

    const response = await axios.get(url);

    setTasks(response.data);
  };

  useEffect(() => {
    fetchTasks();
  }, [priority, completed]);

  return (
    <div style={{ padding: "40px" }}>

      <h2>Task Manager</h2>

      {/* Filters */}

      <div style={{ marginBottom: "20px" }}>

        <label>Priority: </label>

        <select
          value={priority}
          onChange={(e) => setPriority(e.target.value)}
        >
          <option value="">All</option>
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>

        <label style={{ marginLeft: "20px" }}>
          <input
            type="checkbox"
            checked={completed}
            onChange={(e) => setCompleted(e.target.checked)}
          />
          Completed
        </label>

      </div>

      {/* Table */}

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Priority</th>
            <th>Completed</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>

          {tasks.map((task) => (
            <tr key={task.id}>

              <td>{task.id}</td>
              <td>{task.title}</td>
              <td>{task.priority}</td>
              <td>{task.completed ? "Yes" : "No"}</td>

              <td>

                <button
                  onClick={async () => {
                    await axios.put(
                      `http://127.0.0.1:5000/tasks/${task.id}/toggle`
                    );
                    fetchTasks();
                  }}
                >
                  Toggle
                </button>

                <button
                  onClick={async () => {
                    await axios.delete(
                      `http://127.0.0.1:5000/tasks/${task.id}`
                    );
                    fetchTasks();
                  }}
                  style={{ marginLeft: "10px" }}
                >
                  Delete
                </button>

              </td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default App;