import { Routes, Route, Link, useLocation } from "react-router-dom";
import { useState } from "react";

import Topbar from "./components/Topbar";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";
import About from "./pages/About";

export default function App() {

  const [predictionData, setPredictionData] = useState(null);
  const location = useLocation();

  const navStyle = (path) =>
    `p-3 rounded-lg transition-all duration-300
     ${location.pathname === path
       ? "bg-yellow-400 text-black font-bold shadow-lg"
       : "hover:bg-white/10 hover:text-yellow-400"
     }`;

  return (
    <div className="relative min-h-screen text-white flex overflow-hidden">

      {/* BACKGROUND IMAGE */}
      <div
        className="fixed inset-0 bg-cover bg-center z-0"
        style={{ backgroundImage: "url('/bg.jpg')" }}
      />

      {/* DARK OVERLAY */}
      <div className="fixed inset-0 bg-black/70 z-10 pointer-events-none"></div>

      {/* MAIN APP */}
      <div className="relative z-20 flex w-full">

        {/* 🔥 NEW SIDEBAR */}
        <div className="w-64 h-screen bg-slate-900/90 backdrop-blur-md border-r border-white/10 shadow-2xl p-6 flex flex-col">

          <h1 className="text-2xl font-bold text-yellow-400 mb-10">
            🔥 FireGuard AI
          </h1>

          <nav className="flex flex-col gap-4 text-lg">

            <Link to="/" className={navStyle("/")}>
              📊 Dashboard
            </Link>

            <Link to="/predict" className={navStyle("/predict")}>
              🔥 Predict
            </Link>

            <Link to="/about" className={navStyle("/about")}>
              ℹ️ About
            </Link>

          </nav>

        </div>

        {/* CONTENT */}
        <div className="flex-1 flex flex-col">

          <Topbar />

          <main className="flex-1 p-6">
            <Routes>
              <Route path="/" element={<Dashboard data={predictionData} />} />
              <Route
                path="/predict"
                element={<Predict setData={setPredictionData} />}
              />
              <Route path="/about" element={<About />} />
            </Routes>
          </main>

        </div>

      </div>
    </div>
  );
}