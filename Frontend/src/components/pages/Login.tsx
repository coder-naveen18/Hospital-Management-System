// src/pages/Login.tsx
import React, { useState } from "react";
import AuthLayout from "../auth/AuthLayout";
import { Mail, Lock } from "lucide-react";

const Login: React.FC = () => {
  const [role, setRole] = useState<"staff" | "doctor" | "admin">("doctor");

  return (
    <AuthLayout
      title="Welcome Back"
      subtitle="Enter your credentials to access the medical portal."
    >
      <div className="space-y-6">
        {/* Role Selector */}
        <div className="flex p-1 bg-gray-100 rounded-2xl">
          {(["staff", "doctor", "admin"] as const).map((r) => (
            <button
              key={r}
              onClick={() => setRole(r)}
              className={`flex-1 py-2 text-sm font-bold rounded-xl transition-all capitalize ${
                role === r
                  ? "bg-white text-orange-500 shadow-sm"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              {r}
            </button>
          ))}
        </div>

        <form className="space-y-4" onSubmit={(e) => e.preventDefault()}>
          <div className="space-y-2">
            <label className="text-sm font-bold text-gray-700 ml-1">
              Email Address
            </label>
            <div className="relative group">
              <Mail
                className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-orange-500 transition-colors"
                size={20}
              />
              <input
                type="email"
                placeholder="doctor@aurahealth.com"
                className="w-full pl-12 pr-4 py-4 bg-gray-50 border-none outline-none rounded-2xl focus:ring-2 focus:ring-orange-200 transition-all font-medium"
              />
            </div>
          </div>

          <div className="space-y-2">
            <label className="text-sm font-bold text-gray-700 ml-1">
              Password
            </label>
            <div className="relative group">
              <Lock
                className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-orange-500 transition-colors"
                size={20}
              />
              <input
                type="password"
                placeholder="••••••••"
                className="w-full pl-12 pr-4 py-4 bg-gray-50 border-none outline-none rounded-2xl focus:ring-2 focus:ring-orange-200 transition-all font-medium"
              />
            </div>
          </div>

          <div className="flex justify-end">
            <a
              href="#"
              className="text-sm font-bold text-orange-500 hover:text-orange-600"
            >
              Forgot Password?
            </a>
          </div>

          <button className="w-full bg-orange-500 text-white py-4 rounded-2xl font-bold text-lg hover:bg-orange-600 transition-all shadow-xl shadow-orange-500/20 active:scale-[0.98] mt-4">
            Sign In as {role.charAt(0).toUpperCase() + role.slice(1)}
          </button>
        </form>

        <p className="text-center text-gray-500 font-medium">
          Don't have an account?{" "}
          <a href="#" className="text-orange-500 font-bold">
            Request Access
          </a>
        </p>
      </div>
    </AuthLayout>
  );
};

export default Login;
