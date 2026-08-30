import React from 'react';
import { NavLink } from 'react-router-dom';
import {
  LayoutDashboard,
  ShoppingBag,
  ShoppingCart,
  Package,
  Users,
  UserCheck,
  DollarSign,
  BarChart3,
  Settings,
  LogOut
} from 'lucide-react';

interface SidebarProps {
  userRole?: string;
  onLogout?: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ userRole = 'OWNER', onLogout }) => {
  const allNavItems = [
    { name: 'Dashboard', path: '/dashboard', icon: LayoutDashboard, roles: ['ADMIN', 'OWNER', 'MANAGER'] },
    { name: 'Sales', path: '/sales', icon: ShoppingBag, roles: ['ADMIN', 'OWNER', 'MANAGER', 'STAFF'] },
    { name: 'Purchases', path: '/purchases', icon: ShoppingCart, roles: ['ADMIN', 'OWNER', 'MANAGER'] },
    { name: 'Inventory', path: '/inventory', icon: Package, roles: ['ADMIN', 'OWNER', 'MANAGER', 'STAFF'] },
    { name: 'Customers', path: '/customers', icon: Users, roles: ['ADMIN', 'OWNER', 'MANAGER', 'STAFF'] },
    { name: 'Employees', path: '/employees', icon: UserCheck, roles: ['ADMIN', 'OWNER'] },
    { name: 'Finance', path: '/finance', icon: DollarSign, roles: ['ADMIN', 'OWNER'] },
    { name: 'Reports', path: '/reports', icon: BarChart3, roles: ['ADMIN', 'OWNER', 'MANAGER'] },
    { name: 'Settings', path: '/settings', icon: Settings, roles: ['ADMIN', 'OWNER'] },
  ];

  const allowedItems = allNavItems.filter(item => item.roles.includes(userRole));

  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen flex flex-col justify-between p-4 shadow-lg">
      <div>
        <div className="flex items-center space-x-3 mb-8 px-2">
          <div className="w-9 h-9 bg-indigo-600 rounded-lg flex items-center justify-center font-extrabold text-xl tracking-wider text-white">
            360
          </div>
          <div>
            <h1 className="font-bold text-lg leading-tight">MSME360</h1>
            <p className="text-xs text-slate-400">Business Management</p>
          </div>
        </div>

        <nav className="space-y-1">
          {allowedItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink
                key={item.path}
                to={item.path}
                className={({ isActive }) =>
                  `flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors ${
                    isActive
                      ? 'bg-indigo-600 text-white shadow'
                      : 'text-slate-300 hover:bg-slate-800 hover:text-white'
                  }`
                }
              >
                <Icon size={18} />
                <span>{item.name}</span>
              </NavLink>
            );
          })}
        </nav>
      </div>

      <div className="pt-4 border-t border-slate-800">
        <div className="px-3 py-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">
          Role: <span className="text-indigo-400">{userRole}</span>
        </div>
        {onLogout && (
          <button
            onClick={onLogout}
            className="w-full flex items-center space-x-3 px-3 py-2.5 rounded-lg text-sm font-medium text-red-400 hover:bg-slate-800 hover:text-red-300 transition-colors"
          >
            <LogOut size={18} />
            <span>Sign Out</span>
          </button>
        )}
      </div>
    </aside>
  );
};
