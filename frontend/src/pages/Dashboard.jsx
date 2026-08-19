import React, { useEffect, useState } from "react";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  CartesianGrid, ResponsiveContainer, Cell
} from "recharts";

export default function Dashboard() {

  const [riskData, setRiskData] = useState({
    type1: "Low",
    type2: "Low",
    final: "Low"
  });

  const [history, setHistory] = useState([]);
  const [explain, setExplain] = useState([]);

  useEffect(() => {

    const saved = JSON.parse(localStorage.getItem("prediction"));

    if (saved) {

      setRiskData(saved);

      const h = JSON.parse(localStorage.getItem("history")) || [];

      const newHistory = [
        `${new Date().toLocaleString()} — ${saved.final} Risk`,
        ...h
      ].slice(0, 5);

      setHistory(newHistory);
      localStorage.setItem("history", JSON.stringify(newHistory));

      // 🔥 ALERT ONLY WHEN ALL HIGH
      if (
        saved.type1 === "High" &&
        saved.type2 === "High" &&
        saved.final === "High"
      ) {
        setTimeout(() => {
          const audio = new Audio("/sounds/alert.wav");
          audio.play().catch(() => {});
        }, 500);
      }

      // EXPLAIN AI
      let r = [];

      r.push(saved.type1 === "High"
        ? "🔥 High fire activity detected"
        : saved.type1 === "Medium"
        ? "⚠️ Moderate fire activity"
        : "✅ Low fire activity");

      r.push(saved.type2 === "High"
        ? "🔥 Extreme weather conditions"
        : saved.type2 === "Medium"
        ? "⚠️ Moderate weather risk"
        : "✅ Safe weather");

      r.push(saved.final === "High"
        ? "🚨 HIGH RISK – Immediate attention required"
        : saved.final === "Medium"
        ? "⚠️ Medium Risk – Stay alert"
        : "✅ Low Risk – Safe");

      setExplain(r);
    }

  }, []);

  const value = r => r === "Low" ? 1 : r === "Medium" ? 2 : 3;

  const color = r =>
    r === "Low" ? "#4ade80" :
    r === "Medium" ? "#facc15" :
    "#f87171";

  const data = [
    { name: "Type1", value: value(riskData.type1), risk: riskData.type1 },
    { name: "Type2", value: value(riskData.type2), risk: riskData.type2 },
    { name: "Final", value: value(riskData.final), risk: riskData.final }
  ];

  return (
    <div className="max-w-6xl mx-auto space-y-10 text-white">

      {/* ALERT */}
      {riskData.final === "High" && (
        <div className="bg-gradient-to-r from-red-600 to-red-800 p-3 rounded-lg text-center font-semibold shadow-lg animate-pulse">
          🚨 HIGH WILDFIRE RISK DETECTED — TAKE ACTION
        </div>
      )}

      {/* TITLE */}
      <h1 className="text-4xl font-bold tracking-wide">
        🔥 AI Wildfire Intelligence Dashboard
      </h1>

      {/* CARDS */}
      <div className="grid md:grid-cols-3 gap-6">

        {["Type-1 Risk", "Type-2 Risk", "Final Risk"].map((t, i) => {

          const val =
            i === 0 ? riskData.type1 :
            i === 1 ? riskData.type2 :
            riskData.final;

          return (
            <div
              key={i}
              className="bg-slate-900/80 backdrop-blur-md p-6 rounded-xl text-center shadow-xl border border-white/10 hover:scale-105 transition"
            >
              <h3 className="mb-2 text-gray-300">{t}</h3>

              <h1
                className="text-3xl font-bold"
                style={{
                  color: color(val),
                  textShadow: `0 0 12px ${color(val)}`
                }}
              >
                {val}
              </h1>

            </div>
          );
        })}

      </div>

      {/* GRAPH */}
      <div className="bg-slate-900/90 p-6 rounded-xl shadow-xl border border-white/10">

        <h3 className="mb-4 text-lg">📊 Risk Analytics</h3>

        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>

            <CartesianGrid strokeDasharray="3 3" stroke="#334155" />

            <XAxis dataKey="name" stroke="#e2e8f0" />

            <YAxis
              ticks={[1, 2, 3]}
              domain={[0, 3]}
              stroke="#e2e8f0"
            />

            <Tooltip
              contentStyle={{ background: "#020617", border: "none" }}
              labelStyle={{ color: "white" }}
            />

            <Bar
              dataKey="value"
              radius={[10, 10, 0, 0]}
              minPointSize={25}   // 🔥 FIX FOR LOW BAR
            >
              {data.map((e, i) => (
                <Cell key={i} fill={color(e.risk)} />
              ))}
            </Bar>

          </BarChart>
        </ResponsiveContainer>

      </div>

      {/* EXPLAIN */}
      <div className="bg-slate-900/80 p-6 rounded-xl shadow-xl border border-white/10">

        <h3 className="text-yellow-400 mb-3">🧠 AI Explanation</h3>

        <ul className="space-y-2 text-gray-300">
          {explain.map((e, i) => (
            <li key={i}>{e}</li>
          ))}
        </ul>

      </div>

      {/* HISTORY */}
      <div className="bg-slate-900/80 p-6 rounded-xl shadow-xl border border-white/10">

        <h3 className="mb-3">📜 Prediction History</h3>

        {history.map((h, i) => (
          <p key={i} className="text-gray-300">{h}</p>
        ))}

      </div>

    </div>
  );
}