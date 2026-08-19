import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# ======================================================
# LOAD MODELS
# ======================================================

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

type1_bundle = joblib.load(os.path.join(PROJECT_ROOT, "models", "type1_model.pkl"))
type2_bundle = joblib.load(os.path.join(PROJECT_ROOT, "models", "type2_model.pkl"))

type1_model = type1_bundle["model"]
type1_features = type1_bundle["features"]

type2_model = type2_bundle["model"]
type2_features = type2_bundle["features"]

# ======================================================
# USER INPUT
# ======================================================

print("\n🔥 HYBRID WILDFIRE RISK SYSTEM 🔥\n")

print("---- TYPE-1 INPUT (Fire History) ----")
fire_count = int(input("Fire count: "))
avg_frp = float(input("Average FRP: "))
max_frp = float(input("Max FRP: "))
night_fire_ratio = float(input("Night fire ratio (0–1): "))
confidence_score = float(input("Confidence score (0–1): "))
fire_trend = float(input("Fire trend: "))

print("\n---- TYPE-2 INPUT (Weather) ----")
temp = float(input("Temperature: "))
RH = float(input("Humidity: "))
wind = float(input("Wind speed: "))
rain = float(input("Rainfall: "))

# ======================================================
# MODEL PREDICTIONS
# ======================================================

type1_input = pd.DataFrame([{
    "fire_count": fire_count,
    "avg_frp": avg_frp,
    "max_frp": max_frp,
    "night_fire_ratio": night_fire_ratio,
    "confidence_score": confidence_score,
    "fire_trend": fire_trend
}])[type1_features]

type2_input = pd.DataFrame([{
    "temp": temp,
    "RH": RH,
    "wind": wind,
    "rain": rain
}])[type2_features]

type1_risk = type1_model.predict(type1_input)[0]
type2_risk = type2_model.predict(type2_input)[0]

# ======================================================
# HYBRID LOGIC (SAFETY-FIRST)
# ======================================================

risk_score = {"Low": 0, "Medium": 1, "High": 2}

t1 = risk_score[type1_risk]
t2 = risk_score[type2_risk]

# Weather is critical → safety-first weighting
hybrid_score = (0.6 * t1) + (0.4 * t2)

if hybrid_score < 0.6:
    final_risk = "Low"
elif hybrid_score < 1.4:
    final_risk = "Medium"
else:
    final_risk = "High"

# ======================================================
# OUTPUT
# ======================================================

print("\n🔥 FINAL RESULT 🔥")
print("Type-1 Risk (Historical):", type1_risk)
print("Type-2 Risk (Weather):", type2_risk)
print("Hybrid Score:", round(hybrid_score, 2))
print("➡ FINAL WILDFIRE RISK:", final_risk)

# ======================================================
# 📊 PROFESSIONAL BAR CHART (INPUTS + OUTPUTS)
# ======================================================

labels = [
    "Fire Count", "Avg FRP", "Max FRP",
    "Night Ratio", "Confidence", "Fire Trend",
    "Temperature", "Humidity", "Wind", "Rain",
    "Type-1 Risk", "Type-2 Risk", "Hybrid Risk"
]

values = [
    fire_count, avg_frp, max_frp,
    night_fire_ratio, confidence_score, fire_trend,
    temp, RH, wind, rain,
    t1, t2, risk_score[final_risk]
]

colors = (
    ["#3498db"] * 6 +   # Fire history inputs (Blue)
    ["#9b59b6"] * 4 +   # Weather inputs (Purple)
    ["#e74c3c"] * 3     # Risk outputs (Red)
)

plt.figure(figsize=(15, 6))
plt.bar(labels, values, color=colors)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Value / Risk Level")
plt.title("Hybrid Wildfire Risk Analysis (Inputs + Outputs)")

# Reference lines for risk levels
plt.axhline(1, linestyle="--", linewidth=0.8)
plt.axhline(2, linestyle="--", linewidth=0.8)

plt.tight_layout()
plt.show()
