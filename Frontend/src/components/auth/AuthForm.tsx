// src/components/auth/AuthForm.tsx
import React from "react";
import type { LucideIcon } from "lucide-react";

interface AuthInputProps {
  label: string;
  type: string;
  placeholder: string;
  icon: LucideIcon;
}

export const AuthInput: React.FC<AuthInputProps> = ({
  label,
  type,
  placeholder,
  icon: Icon,
}) => (
  <div className="space-y-2">
    <label className="text-sm font-bold text-gray-700 ml-1">{label}</label>
    <div className="relative group">
      <Icon
        className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-orange-500 transition-colors"
        size={20}
      />
      <input
        type={type}
        placeholder={placeholder}
        className="w-full pl-12 pr-4 py-4 bg-gray-50 border-none outline-none rounded-2xl focus:ring-2 focus:ring-orange-200 transition-all font-medium text-gray-700"
      />
    </div>
  </div>
);
