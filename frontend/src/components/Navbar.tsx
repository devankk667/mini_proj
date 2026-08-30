import React from 'react';
import { Bell, User, Search } from 'lucide-react';

interface NavbarProps {
  user?: { name: string; email: string; role: string } | null;
  unreadAlertsCount?: number;
  onOpenAlerts?: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ user, unreadAlertsCount = 0, onOpenAlerts }) => {
  return (
    <header className="bg-white border-b border-gray-200 h-16 flex items-center justify-between px-6 sticky top-0 z-10 shadow-sm">
      <div className="flex items-center space-x-4 w-96">
        <div className="relative w-full">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={18} />
          <input
            type="text"
            placeholder="Search products, orders, customers..."
            className="w-full pl-10 pr-4 py-1.5 text-sm bg-gray-50 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:bg-white transition"
          />
        </div>
      </div>

      <div className="flex items-center space-x-4">
        <button
          onClick={onOpenAlerts}
          className="relative p-2 text-gray-500 hover:text-gray-700 hover:bg-gray-100 rounded-lg transition"
          title="Notifications & Alerts"
        >
          <Bell size={20} />
          {unreadAlertsCount > 0 && (
            <span className="absolute top-1.5 right-1.5 w-4 h-4 bg-red-500 text-white text-[10px] font-bold rounded-full flex items-center justify-center">
              {unreadAlertsCount}
            </span>
          )}
        </button>

        <div className="h-6 w-px bg-gray-200" />

        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 rounded-full bg-indigo-100 text-indigo-700 font-semibold flex items-center justify-center text-sm border border-indigo-200">
            {user?.name ? user.name.charAt(0).toUpperCase() : <User size={16} />}
          </div>
          <div className="hidden sm:block text-left">
            <div className="text-sm font-semibold text-gray-800 leading-tight">
              {user?.name || 'Guest User'}
            </div>
            <div className="text-xs text-gray-500">{user?.role || 'Visitor'}</div>
          </div>
        </div>
      </div>
    </header>
  );
};
