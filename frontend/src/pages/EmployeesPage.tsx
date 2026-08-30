import { useState } from 'react';

export function EmployeesPage() {
  const [employees, setEmployees] = useState([
    { id: 'emp-1', name: 'Store Manager', role: 'MANAGER', department: 'Operations', salary: 4500.0, status: 'ACTIVE' },
    { id: 'emp-2', name: 'Sales Staff', role: 'STAFF', department: 'Sales', salary: 2800.0, status: 'ACTIVE' }
  ]);
  const [showModal, setShowModal] = useState(false);
  const [newEmp, setNewEmp] = useState({ name: '', role: 'STAFF', department: 'Sales', salary: 3000 });

  const handleCreate = (e: React.FormEvent) => {
    e.preventDefault();
    setEmployees([...employees, { id: `emp-${Date.now()}`, ...newEmp, status: 'ACTIVE' }]);
    setShowModal(false);
    setNewEmp({ name: '', role: 'STAFF', department: 'Sales', salary: 3000 });
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-slate-800">Employee Management</h1>
          <p className="text-slate-500 text-sm">Manage staff members, roles, permissions, and salary records.</p>
        </div>
        <button onClick={() => setShowModal(true)} className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium px-4 py-2 rounded-lg text-sm transition">
          + Add Employee
        </button>
      </div>

      <div className="bg-white rounded-xl border border-slate-200 overflow-hidden shadow-sm">
        <table className="w-full text-left text-sm border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200 text-slate-600 font-semibold">
              <th className="p-3.5">Employee Name</th>
              <th className="p-3.5">Role</th>
              <th className="p-3.5">Department</th>
              <th className="p-3.5">Salary</th>
              <th className="p-3.5">Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {employees.map(e => (
              <tr key={e.id} className="hover:bg-slate-50">
                <td className="p-3.5 font-medium text-slate-800">{e.name}</td>
                <td className="p-3.5"><span className="px-2 py-0.5 rounded text-xs font-semibold bg-indigo-50 text-indigo-700">{e.role}</span></td>
                <td className="p-3.5 text-slate-600">{e.department}</td>
                <td className="p-3.5 font-semibold text-slate-900">${e.salary.toFixed(2)}</td>
                <td className="p-3.5"><span className="px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">{e.status}</span></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {showModal && (
        <div className="fixed inset-0 bg-slate-900/40 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-xl shadow-xl max-w-md w-full p-6 space-y-4">
            <h2 className="text-lg font-bold text-slate-800">Add New Employee</h2>
            <form onSubmit={handleCreate} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Full Name</label>
                <input required type="text" value={newEmp.name} onChange={e => setNewEmp({...newEmp, name: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Role</label>
                <select value={newEmp.role} onChange={e => setNewEmp({...newEmp, role: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm">
                  <option value="ADMIN">ADMIN</option>
                  <option value="OWNER">OWNER</option>
                  <option value="MANAGER">MANAGER</option>
                  <option value="STAFF">STAFF</option>
                </select>
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Department</label>
                <input required type="text" value={newEmp.department} onChange={e => setNewEmp({...newEmp, department: e.target.value})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Monthly Salary ($)</label>
                <input required type="number" value={newEmp.salary} onChange={e => setNewEmp({...newEmp, salary: parseFloat(e.target.value) || 0})} className="w-full px-3 py-1.5 border rounded-lg text-sm" />
              </div>
              <div className="flex justify-end space-x-2 pt-3">
                <button type="button" onClick={() => setShowModal(false)} className="px-4 py-2 border rounded-lg text-sm font-medium">Cancel</button>
                <button type="submit" className="px-4 py-2 bg-indigo-600 text-white rounded-lg text-sm font-medium">Save Employee</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
