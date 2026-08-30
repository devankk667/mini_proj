import { useState } from 'react';

export function SalesPage() {
  const [sales, setSales] = useState([
    { id: 'sale-101', customer_name: 'Acme Corp', items_count: 2, total: 125.0, status: 'COMPLETED', date: '2026-08-30' },
    { id: 'sale-102', customer_name: 'Guest Customer', items_count: 1, total: 25.0, status: 'COMPLETED', date: '2026-08-30' }
  ]);
  const [showModal, setShowModal] = useState(false);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Sales Transactions</h1>
          <p className="text-slate-500 text-sm">Record customer sales, check stock levels, and issue receipts.</p>
        </div>
        <button onClick={() => setShowModal(true)} className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-2 rounded-lg text-sm transition">
          + New Sale
        </button>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold">
              <th className="p-3.5">Sale ID</th>
              <th className="p-3.5">Customer</th>
              <th className="p-3.5">Items</th>
              <th className="p-3.5">Total Amount</th>
              <th className="p-3.5">Status</th>
              <th className="p-3.5">Date</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {sales.map(s => (
              <tr key={s.id} className="hover:bg-slate-50">
                <td className="p-3.5 font-mono text-xs font-semibold text-indigo-600">{s.id}</td>
                <td className="p-3.5 font-medium text-slate-800">{s.customer_name}</td>
                <td className="p-3.5 text-slate-600">{s.items_count} items</td>
                <td className="p-3.5 font-semibold text-slate-900">${s.total.toFixed(2)}</td>
                <td className="p-3.5">
                  <span className="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">
                    {s.status}
                  </span>
                </td>
                <td className="p-3.5 text-slate-500">{s.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-xl shadow-xl max-w-lg w-full p-6 space-y-4">
            <h2 className="text-lg font-bold text-slate-800">Record New Sale</h2>
            <p className="text-sm text-slate-500">Select product items and complete checkout.</p>
            <div className="p-4 bg-slate-50 border rounded-lg text-xs text-slate-600 space-y-2">
              <div className="flex justify-between font-semibold">
                <span>Wireless Mouse x 2</span>
                <span>$50.00</span>
              </div>
              <div className="flex justify-between font-semibold">
                <span>Mechanical Keyboard x 1</span>
                <span>$75.00</span>
              </div>
              <div className="pt-2 border-t flex justify-between text-slate-900 font-bold text-sm">
                <span>Total Amount</span>
                <span>$125.00</span>
              </div>
            </div>
            <div className="flex justify-end space-x-2 pt-3">
              <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 border rounded-lg text-sm font-medium">Cancel</button>
              <button onClick={() => {
                setSales([{ id: `sale-${Date.now()}`, customer_name: 'Acme Corp', items_count: 3, total: 125.0, status: 'COMPLETED', date: new Date().toISOString().split('T')[0] }, ...sales]);
                setShowModal(false);
              }} className="px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-medium">Complete Checkout</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
