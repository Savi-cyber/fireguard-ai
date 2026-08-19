import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
  Legend
);

// 🔁 Convert risk label to number
const riskToValue = (risk) => {
  if (risk === "Low") return 30;
  if (risk === "Medium") return 60;
  if (risk === "High") return 90;
  return 0;
};

export default function RiskChart({ type1, type2 }) {
  const data = {
    labels: ["Type-1 Risk", "Type-2 Risk"],
    datasets: [
      {
        label: "Risk Level",
        data: [
          riskToValue(type1),
          riskToValue(type2),
        ],
        backgroundColor: [
          type1 === "High"
            ? "#ef4444"
            : type1 === "Medium"
            ? "#f59e0b"
            : "#22c55e",
          type2 === "High"
            ? "#ef4444"
            : type2 === "Medium"
            ? "#f59e0b"
            : "#22c55e",
        ],
        borderRadius: 8,
        barThickness: 80,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        min: 0,
        max: 100,
        ticks: {
          callback: (value) => {
            if (value === 30) return "Low";
            if (value === 60) return "Medium";
            if (value === 90) return "High";
            return "";
          },
          color: "#94a3b8",
        },
        grid: {
          color: "#334155",
        },
      },
      x: {
        ticks: {
          color: "#94a3b8",
        },
        grid: {
          display: false,
        },
      },
    },
    plugins: {
      legend: {
        labels: {
          color: "#e5e7eb",
        },
      },
    },
  };

  return (
    <div className="h-[300px]">
      <Bar data={data} options={options} />
    </div>
  );
}
