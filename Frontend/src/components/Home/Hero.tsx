// src/components/home/Hero.tsx
import React from "react";
import { Activity, ArrowRight, Search, CheckCircle2 } from "lucide-react";

const Hero: React.FC = () => {
  return (
    <section className="relative pt-10 pb-20 lg:pt-20 overflow-hidden bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-20 items-center">
          <div className="space-y-10 z-10">
            <div className="inline-flex items-center gap-3 px-4 py-1.5 bg-orange-50 border border-orange-100 text-orange-700 rounded-full text-sm font-bold">
              <Activity size={16} />
              Top Rated Medical Center 2026
            </div>
            <h1 className="text-6xl lg:text-8xl font-black tracking-tighter text-gray-900 leading-[0.95]">
              Precision <br />
              <span className="text-orange-500">Care</span> for <br />
              Every Life.
            </h1>
            <p className="text-xl text-gray-600 max-w-lg leading-relaxed font-medium">
              Experience a healthcare ecosystem where advanced AI meets human
              empathy. We don't just treat symptoms; we care for people.
            </p>

            <div className="flex flex-col sm:flex-row gap-5">
              <button className="bg-orange-500 text-white px-10 py-5 rounded-[2rem] text-lg font-bold hover:bg-orange-600 transition-all shadow-2xl shadow-orange-500/40 flex items-center justify-center gap-3 active:scale-95">
                Consult Expert <ArrowRight size={22} />
              </button>
              <div className="flex items-center gap-4 px-6 bg-gray-50 rounded-[2rem] border border-gray-100 focus-within:ring-2 focus-within:ring-orange-200 transition-all">
                <Search className="text-gray-400" size={20} />
                <input
                  type="text"
                  placeholder="Search treatments..."
                  className="bg-transparent outline-none focus:ring-0 text-gray-700 font-medium py-4"
                />
              </div>
            </div>

            <div className="flex flex-wrap items-center gap-10 pt-6">
              <div className="space-y-1">
                <div className="text-3xl font-black text-gray-900 italic">
                  25k+
                </div>
                <div className="text-sm font-bold text-gray-500 uppercase tracking-tighter">
                  Happy Patients
                </div>
              </div>
              <div className="h-10 w-px bg-gray-200 hidden sm:block"></div>
              <div className="space-y-1">
                <div className="text-3xl font-black text-gray-900 italic">
                  150+
                </div>
                <div className="text-sm font-bold text-gray-500 uppercase tracking-tighter">
                  Award Wins
                </div>
              </div>
            </div>
          </div>

          <div className="relative lg:h-[700px] flex items-center justify-center">
            {/* Background Orbs */}
            <div className="absolute top-10 right-10 w-72 h-72 bg-orange-500/10 rounded-full blur-[80px]"></div>
            <div className="absolute -bottom-10 -left-10 w-60 h-60 bg-gray-100 rounded-full blur-[60px]"></div>

            <div className="relative w-full max-w-[500px]">
              <div className="aspect-[4/5] bg-gray-200 rounded-[4rem] overflow-hidden shadow-2xl relative z-10 border-[12px] border-white">
                <img
                  src="https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&q=80&w=1000"
                  alt="Modern Healthcare Professional"
                  className="w-full h-full object-cover"
                />
              </div>

              {/* Floating Highlight Card */}
              <div className="absolute top-20 -right-8 md:-right-12 bg-white/90 backdrop-blur-xl p-6 rounded-3xl shadow-2xl border border-white z-20 animate-bounce-slow">
                <div className="flex items-center gap-4">
                  <div className="w-12 h-12 bg-orange-500 rounded-2xl flex items-center justify-center text-white">
                    <CheckCircle2 size={24} />
                  </div>
                  <div>
                    <div className="font-black text-gray-900 uppercase text-[10px] tracking-widest">
                      Verified Facility
                    </div>
                    <div className="font-bold text-gray-700">
                      ISO 9001 Certified
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
