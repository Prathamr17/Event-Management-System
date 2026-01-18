import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../api/api";

export default function EditEvent() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState({
    title: "",
    description: "",
    location: "",
    date: ""
  });

  useEffect(() => {
    api.get("/events")
      .then(res => {
        const event = res.data.find(e => e.id === Number(id));
        if (event) setForm(event);
      });
  }, [id]);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    await api.put(`/events/${id}`, form);
    navigate("/events");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit Event</h2>

      <input name="title" value={form.title} onChange={handleChange} />
      <input name="location" value={form.location} onChange={handleChange} />
      <input name="date" type="date" value={form.date} onChange={handleChange} />
      <textarea name="description" value={form.description} onChange={handleChange} />

      <button type="submit">Update</button>
    </form>
  );
}
