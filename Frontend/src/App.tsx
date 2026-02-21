// src/App.tsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";

// Import your Pages
import Home from "./components/pages/Home";
import Login from "./components/pages/Login";
import Signup from "./components/pages/Signup";

const App: React.FC = () => {
  return (
    <Router>
      <div className="min-h-screen bg-white font-sans text-gray-900 selection:bg-orange-100">
        <Navbar />

        <main>
          <Routes>
            {/* When path is "/", show the Home content */}
            <Route path="/" element={<Home />} />

            {/* When path is "/login", show the Login page */}
            <Route path="/login" element={<Login />} />

            {/* When path is "/signup", show the Signup page */}
            <Route path="/signup" element={<Signup />} />
          </Routes>
        </main>

        <Footer />
      </div>
    </Router>
  );
};

export default App;
