import { useState } from 'react';

export function PurchasesPage() {
  const [purchases, setPurchases] = useState([
    { id: 'pur-201', supplier_name: 'Tech Distributors', items_count: 10, total: 450.0, status: 'COMPLETED', date: '2026-08-28' }
  ]);
  const [showModal, setShowModal] = useState(false);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Purchase Orders</h1>
          <p className="text-slate-500 text-sm">Create supplier purchase orders and restock inventory automatically.</p>
        </div>
        <button onClick={() => setShowModal(true)} className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-2 rounded-lg text-sm transition">
          + New Purchase Order
        </button>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold">
              <th className="p-3.5">PO ID</th>
              <th className="p-3.5">Supplier</th>
              <th className="p-3.5">Items</th>
              <th className="p-3.5">Total Cost</th>
              <th className="p-3.5">Status</th>
              <th className="p-3.5">Date</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {purchases.map(p => (
              <tr key={p.id} className="hover:bg-slate-50">
                <td className="p-3.5 font-mono text-xs font-semibold text-indigo-600">{p.id}</td>
                <td className="p-3.5 font-medium text-slate-800">{p.supplier_name}</td>
                <td className="p-3.5 text-slate-600">{p.items_count} units</td>
                <td className="p-3.5 font-semibold text-slate-900">${p.total.toFixed(2)}</td>
                <td className="p-3.5">
                  <span className="px-2.5 py-1 rounded-full text-xs font-bold bg-blue-100 text-blue-800">
                    {p.status}
                  </span>
                </td>
                <td className="p-3.5 text-slate-500">{p.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-xl shadow-xl max-w-lg w-full p-6 space-y-4">
            <h2 className="text-lg font-bold text-slate-800">Create Supplier Purchase Order</h2>
            <div className="p-4 bg-slate-50 border rounded-lg text-xs text-slate-600 space-y-2">
              <div className="flex justify-between font-semibold">
                <span>Mechanical Keyboard x 10</span>
                <span>$450.00</span>
              </div>
            </div>
            <div className="flex justify-end space-x-2 pt-3">
              <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 border rounded-lg text-sm font-medium">Cancel</button>
              <button onClick={() => {
                setPurchases([{ id: `pur-${Date.now()}`, supplier_name: 'Tech Distributors', items_count: 10, total: 450.0, status: 'COMPLETED', date: new Date().toISOString().split('T')[0] }, ...purchases]);
                setShowModal(false);
              }} className="px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-medium">Submit & Receive Stock</button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
