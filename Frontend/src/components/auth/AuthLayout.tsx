// src/components/auth/AuthLayout.tsx
import React from "react";
import { Activity } from "lucide-react";

interface AuthLayoutProps {
  children: React.ReactNode;
  title: string;
  subtitle: string;
}

const AuthLayout: React.FC<AuthLayoutProps> = ({
  children,
  title,
  subtitle,
}) => {
  return (
    <div className="min-h-screen grid lg:grid-cols-2 font-sans">
      {/* Left Side: Form */}
      <div className="flex items-center justify-center p-8 bg-white">
        <div className="w-full max-w-md space-y-8">
          <div className="flex items-center gap-2 mb-10">
            {/* <div className="bg-orange-500 p-2 rounded-xl">
              <Activity className="text-white w-6 h-6" />
            </div> */}
            {/* <span className="text-2xl font-bold text-gray-900 tracking-tight">
              Aura<span className="text-orange-500">Health</span>
            </span> */}
          </div>
          <div>
            <h2 className="text-4xl font-black text-gray-900">{title}</h2>
            <p className="text-gray-500 mt-2 font-medium">{subtitle}</p>
          </div>
          {children}
        </div>
      </div>

      {/* Right Side: Visual (Hidden on mobile) */}
      <div className="hidden lg:flex bg-gray-50 items-center justify-center p-12 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-orange-500/10 rounded-full blur-[100px] -mr-48 -mt-48"></div>
        <div className="relative z-10 text-center space-y-6">
          <div className="bg-white p-8 rounded-[3rem] shadow-2xl border border-gray-100 max-w-sm mx-auto">
            <div className="w-20 h-20 bg-orange-100 rounded-3xl flex items-center justify-center text-orange-500 mx-auto mb-6">
              <Activity size={40} />
            </div>
            <p className="text-gray-800 font-bold text-xl">
              "The best way to find yourself is to lose yourself in the service
              of others."
            </p>
            <p className="text-orange-500 font-bold mt-4 tracking-widest uppercase text-xs">
              Medical Portal v2.0
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AuthLayout;
