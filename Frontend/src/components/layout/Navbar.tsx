// src/components/layout/Navbar.tsx
import React, { useState, useEffect } from "react";
import { Activity, Calendar, Menu, X } from "lucide-react";

const Navbar: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 20);
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

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
          <div className="bg-orange-500 p-2 rounded-xl group-hover:rotate-12 transition-transform">
            <Activity className="text-white w-6 h-6" />
          </div>
          <span className="text-2xl font-bold text-gray-900 tracking-tight">
            Aura<span className="text-orange-500">Health</span>
          </span>
        </div>

        <div className="hidden md:flex items-center gap-8 font-semibold text-gray-600">
          <a
            href="#services"
            className="hover:text-orange-500 transition-colors"
          >
            Services
          </a>
          <a href="#" className="hover:text-orange-500 transition-colors">
            Find a Doctor
          </a>
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

      {isOpen && (
        <div className="md:hidden bg-white border-t p-6 space-y-4 shadow-2xl animate-in fade-in slide-in-from-top-4">
          <a href="#services" className="block text-lg font-medium">
            Services
          </a>
          <button className="w-full bg-orange-500 text-white py-4 rounded-2xl font-bold flex items-center justify-center gap-2">
            <Calendar size={20} /> Book Now
          </button>
        </div>
      )}
    </nav>
  );
};

export default Navbar;
