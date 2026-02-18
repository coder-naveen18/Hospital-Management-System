// src/types/index.ts
import type { ElementType } from "react";

export interface Service {
  id: number;
  title: string;
  description: string;
  icon: ElementType;
}

export interface HospitalStats {
  occupancy: number;
  avgWaitTime: number;
  erSurgeons: number;
  ambulanceStatus: "available" | "en-route" | "busy";
}
