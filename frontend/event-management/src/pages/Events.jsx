import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/api";

export default function Events() {
  const [events, setEvents] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    try {
      const res = await api.get("/events");
      setEvents(res.data);
    } catch (err) {
      alert("Failed to load events");
      console.error(err);
    }
  };

  const deleteEvent = async (id) => {
    if (!window.confirm("Delete this event?")) return;

    try {
      await api.delete(`/events/${id}`);
      setEvents(events.filter(e => e.id !== id));
    } catch (err) {
      alert("Failed to delete event");
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Events</h2>

      <button onClick={() => navigate("/events/create")}>
        Create Event
      </button>

      {events.map(e => (
        <div key={e.id}>
          <h3>[{e.id}] {e.title}</h3>
          <p>{e.date}</p>

          <button onClick={() => navigate(`/events/edit/${e.id}`)}>
            Edit
          </button>

          <button onClick={() => deleteEvent(e.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}
