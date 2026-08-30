import { useState } from 'react';
import { MetricCard } from '../components/MetricCard';
import { DollarSign, ArrowUpRight, ArrowDownRight, Percent } from 'lucide-react';

export function FinancePage() {
  const [summary] = useState({
    revenue: 1240.0,
    expenses: 450.0,
    grossProfit: 790.0,
    netProfit: 790.0,
    margin: 63.7,
    receivables: 150.0,
    payables: 300.0
  });

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-slate-800">Financial Overview</h1>
        <p className="text-slate-500 text-sm">Income, expenses, profit margins, receivables, and payables summary.</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Total Revenue" value={`$${summary.revenue.toFixed(2)}`} trend={{ value: '14%', positive: true }} icon={<DollarSign size={20} />} />
        <MetricCard title="Total Expenses" value={`$${summary.expenses.toFixed(2)}`} trend={{ value: '5%', positive: false }} icon={<ArrowDownRight size={20} />} />
        <MetricCard title="Net Profit" value={`$${summary.netProfit.toFixed(2)}`} trend={{ value: '18%', positive: true }} icon={<ArrowUpRight size={20} />} />
        <MetricCard title="Profit Margin" value={`${summary.margin}%`} icon={<Percent size={20} />} />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
          <h2 className="font-bold text-slate-800 mb-3">Accounts Receivable</h2>
          <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-lg text-emerald-900 flex justify-between items-center">
            <div>
              <div className="text-xs uppercase font-bold text-emerald-700">Pending Invoices</div>
              <div className="text-xl font-bold">${summary.receivables.toFixed(2)}</div>
            </div>
            <span className="text-xs font-semibold bg-emerald-200 px-2.5 py-1 rounded-full text-emerald-800">2 Clients</span>
          </div>
        </div>

        <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
          <h2 className="font-bold text-slate-800 mb-3">Accounts Payable</h2>
          <div className="p-4 bg-amber-50 border border-amber-200 rounded-lg text-amber-900 flex justify-between items-center">
            <div>
              <div className="text-xs uppercase font-bold text-amber-700">Vendor Bills Due</div>
              <div className="text-xl font-bold">${summary.payables.toFixed(2)}</div>
            </div>
            <span className="text-xs font-semibold bg-amber-200 px-2.5 py-1 rounded-full text-amber-800">1 Supplier</span>
          </div>
        </div>
      </div>
    </div>
  );
}
