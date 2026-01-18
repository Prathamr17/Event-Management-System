import { useAuth } from "../auth/AuthContext";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Welcome to Event Management System</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Dashboard;
