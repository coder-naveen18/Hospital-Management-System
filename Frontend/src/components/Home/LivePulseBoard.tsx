// src/components/home/LivePulseBoard.tsx
import React, { useState, useEffect } from "react";
import { MapPin, Users, Clock, ShieldCheck, Droplets } from "lucide-react";
import { PulseCard } from "./PulseCard";
import type { HospitalStats } from "../../types";

const LivePulseBoard: React.FC = () => {
  const [stats, setStats] = useState<HospitalStats>({
    occupancy: 78,
    avgWaitTime: 12,
    erSurgeons: 14,
    ambulanceStatus: "available",
  });

  useEffect(() => {
    const interval = setInterval(() => {
      setStats((prev) => ({
        ...prev,
        occupancy: Math.min(
          Math.max(prev.occupancy + (Math.random() > 0.5 ? 1 : -1), 70),
          95,
        ),
        avgWaitTime: Math.min(
          Math.max(prev.avgWaitTime + (Math.random() > 0.5 ? 2 : -2), 5),
          45,
        ),
      }));
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="bg-gray-900 rounded-[2.5rem] p-8 md:p-12 relative overflow-hidden">
      <div className="flex flex-col md:flex-row justify-between mb-12 gap-6 relative z-10">
        <div>
          <div className="flex items-center gap-3 mb-2">
            <div className="h-2 w-2 rounded-full bg-orange-500 animate-pulse"></div>
            <span className="text-orange-500 font-bold uppercase tracking-widest text-xs">
              Live System Status
            </span>
          </div>
          <h3 className="text-3xl font-extrabold text-white">
            Facility Dynamic Pulse
          </h3>
        </div>
        <div className="flex items-center gap-3 px-5 py-2.5 bg-white/5 rounded-2xl border border-white/10 text-white">
          <MapPin size={18} className="text-orange-500" />
          <span className="text-sm font-medium">
            Global Medical Hub, Sector 4
          </span>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 relative z-10">
        <PulseCard
          icon={Users}
          value={`${stats.occupancy}%`}
          label="Bed Occupancy"
          subtext="Real-time capacity"
          showProgress
          progress={stats.occupancy}
        />
        <PulseCard
          icon={Clock}
          value={`${stats.avgWaitTime}m`}
          label="Avg. ER Wait"
          subtext="Updated 2m ago"
        />
        <PulseCard
          icon={ShieldCheck}
          value={stats.erSurgeons.toString()}
          label="Active Experts"
          subtext="On-duty specialists"
        />
        <PulseCard
          icon={Droplets}
          value="Safe"
          label="Blood Reserves"
          subtext="All types available"
          isStatus
        />
      </div>
    </div>
  );
};

export default LivePulseBoard;
