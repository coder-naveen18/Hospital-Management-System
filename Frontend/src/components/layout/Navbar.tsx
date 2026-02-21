// src/components/layout/Navbar.tsx
import React, { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import { Activity, Calendar, Menu, X } from "lucide-react";

const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const handleHomeClick = () => {
    if (location.pathname === "/") {
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
    setIsOpen(false); // Close mobile menu if open
  };

  return (
    <nav
      className={`sticky top-0 z-50 transition-all duration-300 ${
        isScrolled
          ? "bg-white/95 backdrop-blur-md shadow-sm py-3"
          : "bg-white py-5"
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center">
        <div className="flex items-center gap-2 group cursor-pointer">
          <Link
            to="/"
            onClick={handleHomeClick}
            className="flex items-center gap-2 group cursor-pointer"
          >
            <div className="bg-orange-500 p-2 rounded-xl group-hover:rotate-12 transition-transform">
              <Activity className="text-white w-6 h-6" />
            </div>
            <span className="text-2xl font-bold text-gray-900 tracking-tight">
              Aura<span className="text-orange-500">Health</span>
            </span>
          </Link>
        </div>

        <div className="hidden md:flex items-center gap-8 font-semibold text-gray-600">
          <Link
            to="/"
            onClick={handleHomeClick}
            className="hover:text-orange-500 transition-colors"
          >
            Home
          </Link>
          <a
            href="#services"
            className="hover:text-orange-500 transition-colors"
          >
            Services
          </a>
          <a href="#" className="hover:text-orange-500 transition-colors">
            Find a Doctor
          </a>
          <Link to="/login" className="hover:text-orange-500 transition-colors">
            Login
          </Link>
          <Link
            to="/signup"
            className="hover:text-orange-500 transition-colors"
          >
            Signup
          </Link>
          <button className="bg-orange-500 text-white px-6 py-3 rounded-2xl hover:bg-orange-600 transition-all shadow-lg shadow-orange-500/20 active:scale-95 flex items-center gap-2">
            <Calendar size={18} /> Book Appointment
          </button>
        </div>

        <button
          onClick={() => setIsOpen(!isOpen)}
          className="md:hidden text-gray-600"
        >
          {isOpen ? <X size={28} /> : <Menu size={28} />}
        </button>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-white border-t border-gray-100 absolute w-full left-0 shadow-2xl animate-in fade-in slide-in-from-top-4 duration-300">
          <div className="flex flex-col p-6 space-y-4">
            {/* Primary Links */}
            <Link
              to="/"
              onClick={() => setIsOpen(false)}
              className="text-lg font-bold text-gray-800 hover:text-orange-500 py-2 border-b border-gray-50 transition-colors"
            >
              Home
            </Link>
            <a
              href="#services"
              onClick={() => setIsOpen(false)}
              className="text-lg font-bold text-gray-800 hover:text-orange-500 py-2 border-b border-gray-50 transition-colors"
            >
              Services
            </a>
            <a
              href="#"
              onClick={() => setIsOpen(false)}
              className="text-lg font-bold text-gray-800 hover:text-orange-500 py-2 border-b border-gray-50 transition-colors"
            >
              Find a Doctor
            </a>

            {/* Auth Links - Styled as secondary buttons for mobile */}
            <div className="grid grid-cols-2 gap-4 pt-4">
              <Link
                to="/login"
                onClick={() => setIsOpen(false)}
                className="flex items-center justify-center gap-2 bg-gray-50 text-gray-700 py-3 rounded-xl font-bold hover:bg-gray-100"
              >
                Login
              </Link>
              <Link
                to="/signup"
                onClick={() => setIsOpen(false)}
                className="flex items-center justify-center gap-2 border-2 border-orange-500 text-orange-500 py-3 rounded-xl font-bold hover:bg-orange-50"
              >
                Signup
              </Link>
            </div>

            {/* Primary Call to Action */}
            <Link to="/login" onClick={() => setIsOpen(false)}>
              <button className="w-full bg-orange-500 text-white py-4 rounded-2xl font-black text-lg flex items-center justify-center gap-2 shadow-lg shadow-orange-500/30 active:scale-[0.98] transition-transform">
                <Calendar size={20} /> Book Appointment
              </button>
            </Link>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
