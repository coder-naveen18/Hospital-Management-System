// src/components/Stats.tsx
import React from "react";

const Stats: React.FC = () => {
  const data = [
    { label: "Successful Surgeries", value: "15k+" },
    { label: "Expert Doctors", value: "250+" },
    { label: "Emergency Beds", value: "100" },
    { label: "Years of Trust", value: "45" },
  ];

  return (
    <section className="bg-orange-500 py-16 px-6">
      <div className="max-w-6xl mx-auto grid grid-cols-2 lg:grid-cols-4 gap-8">
        {data.map((stat, index) => (
          <div key={index} className="text-center text-white">
            <h4 className="text-4xl font-black mb-2">{stat.value}</h4>
            <p className="text-orange-100 font-medium uppercase tracking-wider text-sm">
              {stat.label}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Stats;
