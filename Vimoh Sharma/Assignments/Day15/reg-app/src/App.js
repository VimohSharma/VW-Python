import React, { useState } from "react";
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
import Registration from "./components/Registration";
import Form from "./components/Form";

function AppWrapper() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  const handleSetUser = (data) => {
    setUser(data);
    navigate("/form");
  };

  const logout = () => {
    setUser(null);
    navigate("/");
  };

  return (
    <Routes>
      <Route path="/" element={<Registration setUser={handleSetUser} />} />
      <Route path="/form" element={<Form user={user} logout={logout} />} />
    </Routes>
  );
}

function App() {
  return (
    <BrowserRouter>
      <AppWrapper />
    </BrowserRouter>
  );
}

export default App;