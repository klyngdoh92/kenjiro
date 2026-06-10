// src/pages/Login.jsx
import { useState } from "react";
import api from "../api/client";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  console.log("IN LOGIN");

  const handleLogin = async () => {
    const res = await api.post("/login", {
      username,
      password,
    });

    localStorage.setItem("access", res.data.access);
    localStorage.setItem("refresh", res.data.refresh);

    navigate("/dashboard");
  };

  return (
    <div>
      <h2>Login</h2>
      <input onChange={(e) => setUsername(e.target.value)} placeholder="username" />
      <input type="password" onChange={(e) => setPassword(e.target.value)} placeholder="password" />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}