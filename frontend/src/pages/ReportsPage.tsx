import { useState } from 'react';
import { FileText, Download, Calendar, Filter } from 'lucide-react';

export function ReportsPage() {
  const [reportType, setReportType] = useState('sales');
  const [dateRange, setDateRange] = useState('month');

  const reportData = [
    { id: 'REP-001', name: 'August 2026 Sales & Revenue Summary', category: 'Sales', format: 'JSON / CSV', generated: '2026-08-30' },
    { id: 'REP-002', name: 'Q3 Inventory Valuation & Low Stock Report', category: 'Inventory', format: 'JSON / CSV', generated: '2026-08-28' },
    { id: 'REP-003', name: 'Supplier Purchase Order History', category: 'Purchases', format: 'JSON / CSV', generated: '2026-08-25' },
  ];

  const handleExport = (name: string) => {
    alert(`Exporting report "${name}" as CSV file...`);
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Business Reports</h1>
          <p className="text-slate-500 text-sm">Generate and export sales, purchase, inventory, and financial reports.</p>
        </div>
      </div>

      <div className="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex flex-wrap gap-4 items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-2 text-slate-600 font-medium text-sm">
            <Filter size={18} />
            <span>Type:</span>
          </div>
          <select value={reportType} onChange={e => setReportType(e.target.value)} className="px-3 py-1.5 border border-slate-300 rounded-lg text-sm">
            <option value="sales">Sales Report</option>
            <option value="purchases">Purchase Report</option>
            <option value="inventory">Inventory Report</option>
            <option value="finance">Financial Statement</option>
          </select>
        </div>

        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-2 text-slate-600 font-medium text-sm">
            <Calendar size={18} />
            <span>Range:</span>
          </div>
          <select value={dateRange} onChange={e => setDateRange(e.target.value)} className="px-3 py-1.5 border border-slate-300 rounded-lg text-sm">
            <option value="today">Today</option>
            <option value="week">This Week</option>
            <option value="month">This Month</option>
            <option value="year">This Year</option>
          </select>

          <button onClick={() => alert('Report generated successfully!')} className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-1.5 rounded-lg text-sm transition flex items-center space-x-2">
            <FileText size={16} />
            <span>Generate Report</span>
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
        <div className="p-4 border-b border-slate-200 font-bold text-slate-800">
          Generated Reports History
        </div>
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold">
              <th className="p-3.5">Report ID</th>
              <th className="p-3.5">Report Title</th>
              <th className="p-3.5">Category</th>
              <th className="p-3.5">Generated Date</th>
              <th className="p-3.5 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {reportData.map(rep => (
              <tr key={rep.id} className="hover:bg-slate-50">
                <td className="p-3.5 font-mono text-xs font-semibold text-indigo-600">{rep.id}</td>
                <td className="p-3.5 font-medium text-slate-800">{rep.name}</td>
                <td className="p-3.5 text-slate-600">{rep.category}</td>
                <td className="p-3.5 text-slate-500">{rep.generated}</td>
                <td className="p-3.5 text-right">
                  <button onClick={() => handleExport(rep.name)} className="px-3 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded text-xs font-semibold inline-flex items-center space-x-1">
                    <Download size={14} />
                    <span>Export CSV</span>
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
