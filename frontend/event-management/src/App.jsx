import { BrowserRouter, Routes, Route } from "react-router-dom";
import Events from "./pages/Events";
import EditEvent from "./pages/EditEvent";
import CreateEvent from "./pages/CreateEvent";
import Login from "./pages/Login";
import Signup from "./pages/Signup";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/events" element={<Events />} />
        <Route path="/events/edit/:id" element={<EditEvent />} />
        <Route path="/events/create" element={<CreateEvent />} />
      </Routes>
    </BrowserRouter>
  );
}
