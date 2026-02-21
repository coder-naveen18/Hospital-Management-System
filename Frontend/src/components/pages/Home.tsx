// src/pages/Home.tsx
import React from "react";
import Hero from "../Home/Hero";
import LivePulseBoard from "../Home/LivePulseBoard";
import Services from "../Home/Services";
import ExperienceCTA from "../Home/ExperienceCTA";

const Home: React.FC = () => {
  return (
    <>
      <Hero />
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <LivePulseBoard />
        </div>
      </section>
      <Services id="services" />
      <ExperienceCTA />
    </>
  );
};

export default Home;
