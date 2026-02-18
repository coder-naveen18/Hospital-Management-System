// src/App.tsx
import React from "react";
import Navbar from "./components/layout/Navbar";
import Hero from "./components/Home/Hero";
import LivePulseBoard from "./components/Home/LivePulseBoard";
import Services from "./components/Home/Services";
import ExperienceCTA from "./components/Home/ExperienceCTA";
import Footer from "./components/layout/Footer";

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-white font-sans text-gray-900 selection:bg-orange-100">
      <Navbar />
      <main>
        <Hero />
        <section className="py-20 bg-white">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <LivePulseBoard />
          </div>
        </section>
        <Services id="services" />
        <ExperienceCTA />
      </main>
      <Footer />
    </div>
  );
};

export default App;
