// src/components/layout/Footer.tsx
import React from "react";
import {
  Activity,
  ArrowRight,
  Facebook,
  Twitter,
  Linkedin,
  Instagram,
} from "lucide-react";

const Footer: React.FC = () => {
  const currentYear = new Date().getFullYear();

  const footerLinks = {
    quickLinks: [
      { name: "Our Doctors", href: "#" },
      { name: "Treatments", href: "#" },
      { name: "Contact", href: "#" },
      { name: "Careers", href: "#" },
    ],
    patientCare: [
      { name: "Check-in Online", href: "#" },
      { name: "Medical Records", href: "#" },
      { name: "Pharmacy", href: "#" },
      { name: "Support", href: "#" },
    ],
  };

  return (
    <footer className="bg-gray-900 text-white pt-24 pb-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-16 mb-20">
          {/* Brand Column */}
          <div className="md:col-span-5 space-y-8">
            <div className="flex items-center gap-3">
              <div className="bg-orange-500 p-2.5 rounded-xl">
                <Activity className="text-white w-6 h-6" />
              </div>
              <span className="text-3xl font-black tracking-tighter uppercase">
                AuraHealth
              </span>
            </div>
            <p className="text-gray-400 text-lg leading-relaxed max-w-md">
              A global leader in medical innovation and patient-centric care. We
              are shaping the future of healthy living across 12 countries.
            </p>
            <div className="flex gap-4">
              {[Facebook, Twitter, Linkedin, Instagram].map((Icon, idx) => (
                <div
                  key={idx}
                  className="w-12 h-12 rounded-2xl bg-gray-800 flex items-center justify-center hover:bg-orange-500 transition-all cursor-pointer group"
                >
                  <Icon
                    size={20}
                    className="text-gray-400 group-hover:text-white transition-colors"
                  />
                </div>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div className="md:col-span-2 space-y-6">
            <h4 className="font-black text-sm uppercase tracking-widest text-orange-500">
              Quick Links
            </h4>
            <ul className="space-y-4 text-gray-400 font-bold">
              {footerLinks.quickLinks.map((link) => (
                <li key={link.name}>
                  <a
                    href={link.href}
                    className="hover:text-white transition-colors"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Patient Care */}
          <div className="md:col-span-2 space-y-6">
            <h4 className="font-black text-sm uppercase tracking-widest text-orange-500">
              Patient Care
            </h4>
            <ul className="space-y-4 text-gray-400 font-bold">
              {footerLinks.patientCare.map((link) => (
                <li key={link.name}>
                  <a
                    href={link.href}
                    className="hover:text-white transition-colors"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Newsletter */}
          <div className="md:col-span-3 space-y-6">
            <h4 className="font-black text-sm uppercase tracking-widest text-orange-500">
              Join the Pulse
            </h4>
            <p className="text-gray-400 font-medium">
              Get the latest medical news and health tips.
            </p>
            <div className="relative">
              <input
                type="email"
                placeholder="name@email.com"
                className="w-full bg-gray-800 border-none rounded-2xl py-4 pl-6 pr-16 text-white placeholder-gray-500 focus:ring-2 focus:ring-orange-500 transition-all"
              />
              <button className="absolute right-2 top-2 bottom-2 bg-orange-500 text-white px-4 rounded-xl hover:bg-orange-600 transition-all active:scale-95">
                <ArrowRight size={20} />
              </button>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-12 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center gap-6 text-gray-500 font-bold text-sm">
          <div className="flex gap-8">
            <a href="#" className="hover:text-white transition-colors">
              Privacy Policy
            </a>
            <a href="#" className="hover:text-white transition-colors">
              Terms of Service
            </a>
          </div>
          <div>© {currentYear} AuraHealth Global. All rights reserved.</div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
