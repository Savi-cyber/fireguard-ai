export default function RiskCard({ title, value }) {
  const colors = {
    Low: "border-green-500 text-green-400",
    Medium: "border-amber-400 text-amber-400",
    High: "border-red-500 text-red-400",
  };

  return (
    <div
      className={`bg-slate-800 border-l-4 p-4 rounded ${
        colors[value] || ""
      }`}
    >
      <p className="text-sm text-slate-400">{title}</p>
      <p className="text-2xl font-semibold mt-1">
        {value}
      </p>
    </div>
  );
}
