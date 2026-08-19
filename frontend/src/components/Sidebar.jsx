import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 p-4">
      <h2 className="text-lg font-bold text-amber-400 mb-6">
        HARIS
      </h2>

      <nav className="space-y-3">
        <NavLink to="/" className="block text-slate-300 hover:text-amber-400">
          Dashboard
        </NavLink>
        <NavLink to="/predict" className="block text-slate-300 hover:text-amber-400">
          Predict
        </NavLink>
        <NavLink to="/about" className="block text-slate-300 hover:text-amber-400">
          About
        </NavLink>
      </nav>
    </aside>
  );
}
