import { Layout } from './components/Layout';
import { Routes, Route, Navigate } from 'react-router-dom';
import { MetricCard } from './components/MetricCard';
import { InventoryPage } from './pages/InventoryPage';
import { CustomersPage } from './pages/CustomersPage';
import { SalesPage } from './pages/SalesPage';
import { PurchasesPage } from './pages/PurchasesPage';
import { FinancePage } from './pages/FinancePage';
import { EmployeesPage } from './pages/EmployeesPage';
import { ReportsPage } from './pages/ReportsPage';
import { DollarSign, ShoppingBag, Package, TrendingUp } from 'lucide-react';

function DashboardPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-slate-800">Business Dashboard</h1>
        <p className="text-slate-500 text-sm">Welcome back! Here is your business overview today.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Today's Revenue" value="$1,240.00" trend={{ value: '12%', positive: true }} subtitle="vs yesterday" icon={<DollarSign size={20} />} />
        <MetricCard title="Sales Count" value="18" trend={{ value: '5%', positive: true }} subtitle="transactions" icon={<ShoppingBag size={20} />} />
        <MetricCard title="Low Stock Items" value="3" trend={{ value: '-1', positive: false }} subtitle="items below threshold" icon={<Package size={20} />} />
        <MetricCard title="Gross Margin" value="34.5%" trend={{ value: '2.1%', positive: true }} subtitle="this month" icon={<TrendingUp size={20} />} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
          <h2 className="font-bold text-slate-800 mb-3">Top Products by Stock</h2>
          <div className="space-y-2 text-sm">
            <div className="flex justify-between items-center p-2 bg-slate-50 rounded">
              <span className="font-medium text-slate-700">Wireless Mouse</span>
              <span className="font-bold text-slate-900">40 units</span>
            </div>
            <div className="flex justify-between items-center p-2 bg-slate-50 rounded">
              <span className="font-medium text-slate-700">A4 Paper Ream</span>
              <span className="font-bold text-slate-900">100 units</span>
            </div>
            <div className="flex justify-between items-center p-2 bg-slate-50 rounded">
              <span className="font-medium text-slate-700">Mechanical Keyboard</span>
              <span className="font-bold text-amber-600">5 units (Low Stock)</span>
            </div>
          </div>
        </div>

        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
          <h2 className="font-bold text-slate-800 mb-3">Recent Sales Activity</h2>
          <div className="space-y-2 text-sm">
            <div className="flex justify-between items-center p-2 border-b border-slate-100">
              <div>
                <div className="font-medium text-slate-800">Acme Corp</div>
                <div className="text-xs text-slate-400">2 items • #sale-101</div>
              </div>
              <span className="font-bold text-emerald-600">$125.00</span>
            </div>
            <div className="flex justify-between items-center p-2 border-b border-slate-100">
              <div>
                <div className="font-medium text-slate-800">Guest Customer</div>
                <div className="text-xs text-slate-400">1 item • #sale-102</div>
              </div>
              <span className="font-bold text-emerald-600">$25.00</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function PlaceholderPage({ title }: { title: string }) {
  return (
    <div className="bg-white p-6 rounded-xl border border-slate-200">
      <h1 className="text-xl font-bold mb-2">{title}</h1>
      <p className="text-slate-500 text-sm">Module interface established and will be filled in during the phase progression.</p>
    </div>
  );
}

export default function App() {
  const currentUser = { name: "Demo User", email: "owner@msme360.com", role: "OWNER" };

  return (
    <Layout user={currentUser}>
      <Routes>
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/inventory" element={<InventoryPage />} />
        <Route path="/customers" element={<CustomersPage />} />
        <Route path="/sales" element={<SalesPage />} />
        <Route path="/purchases" element={<PurchasesPage />} />
        <Route path="/finance" element={<FinancePage />} />
        <Route path="/employees" element={<EmployeesPage />} />
        <Route path="/reports" element={<ReportsPage />} />
        <Route path="/settings" element={<PlaceholderPage title="System Settings" />} />
        <Route path="*" element={<Navigate to="/dashboard" replace />} />
      </Routes>
    </Layout>
  );
}
