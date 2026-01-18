import { useState } from "react";
import api from "../api/api";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post("/auth/signup", form);
    alert("Signup successful");
    navigate("/login");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Signup</h2>
      <input name="username" placeholder="Username" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input
        name="password"
        type="password"
        placeholder="Password"
        onChange={handleChange}
      />
      <button type="submit">Signup</button>
    </form>
  );
};

export default Signup;
