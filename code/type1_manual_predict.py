import joblib
import pandas as pd
import os

# =========================================
# LOAD MODEL
# =========================================

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "type1_model.pkl")

bundle = joblib.load(MODEL_PATH)

model = bundle["model"]
features = bundle["features"]

print("\n🔥 TYPE-1 MANUAL RISK PREDICTION 🔥\n")

# =========================================
# MANUAL INPUT (USER)
# =========================================

fire_count = int(input("Enter fire count: "))
avg_frp = float(input("Enter average FRP: "))
max_frp = float(input("Enter max FRP: "))
night_fire_ratio = float(input("Enter night fire ratio (0–1): "))
confidence_score = float(input("Enter confidence score (0–1): "))
fire_trend = float(input("Enter fire trend: "))

# =========================================
# CREATE INPUT DATAFRAME
# =========================================

input_df = pd.DataFrame([{
    "fire_count": fire_count,
    "avg_frp": avg_frp,
    "max_frp": max_frp,
    "night_fire_ratio": night_fire_ratio,
    "confidence_score": confidence_score,
    "fire_trend": fire_trend
}])[features]

# =========================================
# PREDICT
# =========================================

prediction = model.predict(input_df)[0]
probabilities = model.predict_proba(input_df)[0]

# =========================================
# OUTPUT
# =========================================

print("\n🔥 PREDICTED WILDFIRE RISK 🔥")
print("➡ Risk Level:", prediction)

print("\nConfidence:")
for label, prob in zip(model.classes_, probabilities):
    print(f"  {label}: {prob*100:.2f}%")
