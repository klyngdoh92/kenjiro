// src/pages/Project.jsx
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/client";

export default function Project() {
   console.log("IN PROJECT");
  const { id } = useParams();
  const [tasks, setTasks] = useState([]);

  // const [title, setTitle] = useState("");

    // const createTask = async () => {
    // await api.post("/tasks/", {
    //     title,
    //     project: id,
    // });

    // getTasks();
    // };

    const getTasks = async () => {
        api.get(`/tasks?project=${id}`)
      .then(res => setTasks(res.data))
      .catch(err => console.error(err));
    }

  useEffect(() => {
    if (id){
        getTasks();
    }
  }, [id]);

  return (
    <div>
      <h2>Tasks</h2>

      {tasks.map(t => (
        <div key={t.id}>
          {t.title}
        </div>
      ))}
    </div>
  );
}