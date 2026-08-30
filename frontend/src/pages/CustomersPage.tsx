import { useState } from 'react';

export function CustomersPage() {
  const [customers, setCustomers] = useState([
    { id: 'cust-1', name: 'Acme Corp', email: 'contact@acme.com', phone: '555-0192', total_spent: 450.0 },
    { id: 'cust-2', name: 'Jane Doe', email: 'jane@example.com', phone: '555-0144', total_spent: 120.0 }
  ]);
  const [search, setSearch] = useState('');
  const [showModal, setShowModal] = useState(false);
  const [newCust, setNewCust] = useState({ name: '', email: '', phone: '' });

  const handleCreate = (e: React.FormEvent) => {
    e.preventDefault();
    setCustomers([...customers, { id: `cust-${Date.now()}`, ...newCust, total_spent: 0.0 }]);
    setShowModal(false);
    setNewCust({ name: '', email: '', phone: '' });
  };

  const filtered = customers.filter(c => c.name.toLowerCase().includes(search.toLowerCase()) || (c.email && c.email.toLowerCase().includes(search.toLowerCase())));

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Customers</h1>
          <p className="text-slate-500 text-sm">Customer profiles, purchasing history, and total spending.</p>
        </div>
        <button onClick={() => setShowModal(true)} className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-2 rounded-lg text-sm transition">
          + Add Customer
        </button>
      </div>

      <div className="bg-white p-4 rounded-xl border border-slate-200">
        <input type="text" placeholder="Search customer name or email..." value={search} onChange={e => setSearch(e.target.value)} className="w-72 px-3 py-1.5 border rounded-lg text-sm" />
      </div>

      <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold">
              <th className="p-3.5">Customer Name</th>
              <th className="p-3.5">Email</th>
              <th className="p-3.5">Phone</th>
              <th className="p-3.5">Total Spent</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {filtered.map(c => (
              <tr key={c.id} className="hover:bg-slate-50">
                <td className="p-3.5 font-medium text-slate-800">{c.name}</td>
                <td className="p-3.5 text-slate-600">{c.email || '—'}</td>
                <td className="p-3.5 text-slate-600">{c.phone || '—'}</td>
                <td className="p-3.5 font-semibold text-emerald-600">${c.total_spent.toFixed(2)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-xl shadow-xl max-w-md w-full p-6 space-y-4">
            <h2 className="text-lg font-bold text-slate-800">Add Customer Profile</h2>
            <form onSubmit={handleCreate} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Name</label>
                <input required type="text" value={newCust.name} onChange={e => setNewCust({...newCust, name: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Email</label>
                <input type="email" value={newCust.email} onChange={e => setNewCust({...newCust, email: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Phone</label>
                <input type="text" value={newCust.phone} onChange={e => setNewCust({...newCust, phone: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div className="flex justify-end space-x-2 pt-3">
                <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 border rounded-lg text-sm font-medium">Cancel</button>
                <button type="submit" className="px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-medium">Save Customer</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
