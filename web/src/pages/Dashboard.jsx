// src/pages/Dashboard.jsx
import { useEffect, useState } from "react";
import api from "../api/client.js";
import { Link } from "react-router-dom";

export default function Dashboard() {
   console.log("IN DASHBOARD");
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    api.get("/projects")
      .then(res => setProjects(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Projects</h2>

      {projects.map(p => (
        <div key={p.id}>
          <Link to={`/project/${p.id}`}>{p.name}</Link>
        </div>
      ))}
    </div>
  );
}