// src/components/home/Services.tsx
import React from "react";
import {
  ArrowRight,
  ChevronRight,
  HeartPulse,
  Brain,
  Baby,
  FlaskConical,
  Stethoscope,
  Zap,
} from "lucide-react";
import type { Service } from "../../types";

interface ServicesProps {
  id?: string;
}

const SERVICES: Service[] = [
  {
    id: 1,
    title: "Cardiology",
    description: "Advanced heart care using robotic-assisted diagnostics.",
    icon: HeartPulse,
  },
  {
    id: 2,
    title: "Neurology",
    description: "Specialized treatment for complex brain disorders.",
    icon: Brain,
  },
  {
    id: 3,
    title: "Maternity",
    description: "Personalized suites and world-class neonatal care.",
    icon: Baby,
  },
  {
    id: 4,
    title: "Diagnostics",
    description: "High-precision AI-driven imaging and lab analysis.",
    icon: FlaskConical,
  },
  {
    id: 5,
    title: "General Surgery",
    description: "Minimally invasive procedures for faster recovery.",
    icon: Stethoscope,
  },
  {
    id: 6,
    title: "Trauma Care",
    description: "24/7 emergency response with dedicated units.",
    icon: Zap,
  },
];

const Services: React.FC<ServicesProps> = ({ id }) => {
  return (
    <section id={id} className="py-32 bg-gray-50 relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col lg:flex-row justify-between items-end gap-10 mb-20">
          <div className="max-w-2xl space-y-6">
            <h2 className="text-5xl lg:text-6xl font-black text-gray-900 leading-[1.1]">
              Expertise Across <br />
              <span className="text-orange-500 italic underline decoration-gray-200 underline-offset-8">
                All Domains
              </span>
            </h2>
            <p className="text-lg text-gray-600 font-medium">
              Our multidisciplinary approach ensures you receive coordinated
              care from the brightest minds in modern medicine.
            </p>
          </div>
          <button className="px-8 py-4 bg-white border-2 border-gray-200 rounded-[2rem] font-bold text-gray-900 hover:border-orange-500 hover:text-orange-500 transition-all flex items-center gap-2 group">
            View All Departments{" "}
            <ChevronRight className="group-hover:translate-x-1 transition-transform" />
          </button>
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {SERVICES.map((service) => (
            <div
              key={service.id}
              className="bg-white p-10 rounded-[3rem] border border-gray-100 shadow-sm hover:shadow-2xl hover:-translate-y-2 transition-all group relative overflow-hidden"
            >
              <div className="absolute top-0 left-0 w-2 h-0 bg-orange-500 group-hover:h-full transition-all duration-500"></div>
              <div className="w-16 h-16 bg-gray-50 rounded-2xl flex items-center justify-center text-gray-400 mb-8 group-hover:bg-orange-500 group-hover:text-white transition-all">
                <service.icon size={32} />
              </div>
              <h3 className="text-2xl font-black mb-4 group-hover:text-orange-500 transition-colors">
                {service.title}
              </h3>
              <p className="text-gray-500 leading-relaxed font-medium mb-8">
                {service.description}
              </p>
              <div className="flex items-center gap-2 text-sm font-black uppercase tracking-widest text-gray-400 group-hover:text-gray-900 transition-colors cursor-pointer">
                Read More <ArrowRight size={16} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
