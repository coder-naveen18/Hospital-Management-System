// src/pages/Signup.tsx
import React, { useState } from "react";
import AuthLayout from "../auth/AuthLayout";
import { AuthInput } from "../auth/AuthForm";
import { User, Mail, Lock, Briefcase } from "lucide-react";

const Signup: React.FC = () => {
  const [role, setRole] = useState<"staff" | "doctor">("doctor");

  return (
    <AuthLayout
      title="Join the Medical Team"
      subtitle="Create your professional profile to begin providing care."
    >
      <div className="space-y-6">
        {/* Role Selector */}
        <div className="flex p-1 bg-gray-100 rounded-2xl">
          {(["staff", "doctor"] as const).map((r) => (
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
          <div className="grid grid-cols-1 gap-4">
            <AuthInput
              label="Full Name"
              type="text"
              placeholder="Dr. John Doe"
              icon={User}
            />
            {/* <AuthInput
              label="Employee ID"
              type="text"
              placeholder="AH-9920"
              icon={Building2}
            /> */}
          </div>

          <AuthInput
            label="Official Email"
            type="email"
            placeholder="name@aurahealth.com"
            icon={Mail}
          />

          <div className="space-y-2">
            <label className="text-sm font-bold text-gray-700 ml-1">
              Specialization / Department
            </label>
            <div className="relative group">
              <Briefcase
                className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-orange-500 transition-colors"
                size={20}
              />
              <select className="w-full pl-12 pr-4 py-4 bg-gray-50 border-none outline-none rounded-2xl focus:ring-2 focus:ring-orange-200 transition-all font-medium text-gray-700 appearance-none">
                <option>Cardiology</option>
                <option>Neurology</option>
                <option>Emergency Medicine</option>
                <option>Pediatrics</option>
              </select>
            </div>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <AuthInput
              label="Create Password"
              type="password"
              placeholder="••••••••"
              icon={Lock}
            />
            <AuthInput
              label="Create Password"
              type="password"
              placeholder="••••••••"
              icon={Lock}
            />
          </div>

          <button className="w-full bg-orange-500 text-white py-4 rounded-2xl font-bold text-lg hover:bg-orange-600 transition-all shadow-xl shadow-orange-500/20 active:scale-[0.98] mt-6">
            Register for Approval
          </button>
        </form>

        <p className="text-center text-gray-500 font-medium">
          Already part of the team?{" "}
          <a href="/login" className="text-orange-500 font-bold">
            Sign In
          </a>
        </p>
      </div>
    </AuthLayout>
  );
};

export default Signup;
