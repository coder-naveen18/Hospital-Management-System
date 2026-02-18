// src/components/home/ExperienceCTA.tsx
import React from "react";
import { Phone } from "lucide-react";

const ExperienceCTA: React.FC = () => {
  const steps = [
    { t: "Fast Booking", d: "Confirm your visit in under 60 seconds." },
    { t: "Live Tracking", d: "Track your queue position from your phone." },
    { t: "Direct Access", d: "Chat with your care team anytime." },
  ];

  return (
    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="bg-orange-500 rounded-[4rem] p-10 md:p-20 relative overflow-hidden text-white shadow-2xl shadow-orange-500/20">
          <div className="relative z-10 grid lg:grid-cols-2 gap-20 items-center">
            <div className="space-y-8">
              <h2 className="text-5xl lg:text-7xl font-black leading-[1.05]">
                The Patient Journey, <br />
                <span className="text-orange-200 italic">Simplified.</span>
              </h2>
              <p className="text-orange-50 text-xl font-medium leading-relaxed">
                We've eliminated the friction in healthcare. From digital
                check-ins to AI-powered follow-ups, your health is our priority.
              </p>
              <div className="flex flex-wrap gap-5">
                <button className="bg-white text-orange-600 px-10 py-5 rounded-[2rem] font-black text-lg hover:bg-orange-50 transition-all shadow-xl active:scale-95">
                  Get Started Today
                </button>
                <button className="px-10 py-5 rounded-[2rem] font-bold text-lg border-2 border-white/40 hover:bg-white/10 transition-all flex items-center gap-3">
                  <Phone size={20} /> Emergency Line
                </button>
              </div>
            </div>

            <div className="bg-white/10 backdrop-blur-2xl rounded-[3rem] p-10 border border-white/20 space-y-8 relative">
              {steps.map((item, idx) => (
                <div key={idx} className="flex gap-6 group/item">
                  <div className="w-12 h-12 shrink-0 bg-white rounded-2xl text-orange-500 flex items-center justify-center font-black text-xl shadow-lg group-hover/item:rotate-6 transition-transform">
                    {idx + 1}
                  </div>
                  <div>
                    <div className="font-black text-xl mb-1">{item.t}</div>
                    <div className="text-orange-100 font-medium">{item.d}</div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ExperienceCTA;
