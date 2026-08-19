import pandas as pd
import os
import joblib
from sklearn.ensemble import RandomForestClassifier

# ======================================================
# PATH SETUP
# ======================================================

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULT_DIR = os.path.join(PROJECT_ROOT, "result")
MODEL_DIR = os.path.join(PROJECT_ROOT, "models")

os.makedirs(MODEL_DIR, exist_ok=True)

DATA_PATH = os.path.join(RESULT_DIR, "type1_features.csv")
MODEL_PATH = os.path.join(MODEL_DIR, "type1_model.pkl")

# ======================================================
# LOAD FEATURE DATA
# ======================================================

df = pd.read_csv(DATA_PATH)

print("Loaded rows:", len(df))
print("Columns:", df.columns.tolist())

# ======================================================
# CREATE future_risk (RULE-BASED LOGIC)
# ======================================================

def assign_risk(row):
    if row["fire_count"] >= 4 and row["max_frp"] >= 50:
        return "High"
    elif row["fire_count"] >= 2:
        return "Medium"
    else:
        return "Low"

df["future_risk"] = df.apply(assign_risk, axis=1)

print("\nFuture Risk Distribution:")
print(df["future_risk"].value_counts())

# ======================================================
# FEATURES & TARGET
# ======================================================

FEATURES = [
    "fire_count",
    "avg_frp",
    "max_frp",
    "night_fire_ratio",
    "confidence_score",
    "fire_trend"
]

X = df[FEATURES]
y = df["future_risk"]

# ======================================================
# TRAIN MODEL
# ======================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

model.fit(X, y)

# ======================================================
# SAVE MODEL BUNDLE
# ======================================================

bundle = {
    "model": model,
    "features": FEATURES,
    "risk_levels": ["Low", "Medium", "High"]
}

joblib.dump(bundle, MODEL_PATH)

print("\n🔥 TYPE-1 MODEL SAVED SUCCESSFULLY 🔥")
print("Saved at:", MODEL_PATH)
