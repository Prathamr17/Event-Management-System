import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

export default function CreateEvent() {
  const [form, setForm] = useState({
    title: "",
    description: "",
    location: "",
    date: "",
  });

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    await api.post("/events", form);
    navigate("/events");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        placeholder="Title"
        onChange={(e) => setForm({ ...form, title: e.target.value })}
      />

      <input
        placeholder="Location"
        onChange={(e) => setForm({ ...form, location: e.target.value })}
      />

      <input
        type="date"
        onChange={(e) => setForm({ ...form, date: e.target.value })}
      />

      <textarea
        placeholder="Description"
        onChange={(e) => setForm({ ...form, description: e.target.value })}
      />

      <button type="submit">Create Event</button>
    </form>
  );
}
