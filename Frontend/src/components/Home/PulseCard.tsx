// src/components/home/PulseCard.tsx
import React from "react";
import type { LucideIcon } from "lucide-react";

interface PulseCardProps {
  icon: LucideIcon;
  value: string;
  label: string;
  subtext: string;
  showProgress?: boolean;
  progress?: number;
  isStatus?: boolean;
}

export const PulseCard: React.FC<PulseCardProps> = ({
  icon: Icon,
  value,
  label,
  subtext,
  showProgress,
  progress,
  isStatus,
}) => (
  <div className="bg-white/5 backdrop-blur-sm p-6 rounded-3xl border border-white/10 hover:border-orange-500/40 transition-all group/card">
    <div className="w-12 h-12 bg-orange-500/10 rounded-xl flex items-center justify-center text-orange-500 mb-5 group-hover/card:scale-110 transition-transform">
      <Icon size={24} />
    </div>
    <div className="text-3xl font-bold mb-1 tracking-tight text-white">
      {value}
    </div>
    <div className="text-gray-200 text-sm font-bold mb-1">{label}</div>
    <div className="text-gray-500 text-xs">{subtext}</div>
    {showProgress && (
      <div className="mt-5 w-full bg-gray-800 h-1.5 rounded-full overflow-hidden">
        <div
          className="h-full bg-orange-500 transition-all duration-1000"
          style={{ width: `${progress}%` }}
        ></div>
      </div>
    )}
    {isStatus && (
      <div className="mt-4 flex items-center gap-2">
        <span className="flex h-2 w-2 rounded-full bg-green-500"></span>
        <span className="text-[10px] text-green-500 font-bold uppercase">
          Optimal Level
        </span>
      </div>
    )}
  </div>
);
