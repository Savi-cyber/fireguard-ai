import pandas as pd
import numpy as np
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ======================================================
# 0. PROJECT PATH SETUP (SAFE & FINAL)
# ======================================================

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RESULT_DIR = os.path.join(PROJECT_ROOT, "result")

INPUT_PATH = os.path.join(RESULT_DIR, "type1_features.csv")
OUTPUT_PATH = os.path.join(RESULT_DIR, "type1_predictions.csv")

print("PROJECT ROOT:", PROJECT_ROOT)
print("INPUT PATH:", INPUT_PATH)

# ======================================================
# 1. LOAD FEATURE DATA
# ======================================================

if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"❌ File not found: {INPUT_PATH}")

df = pd.read_csv(INPUT_PATH)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ======================================================
# 2. CREATE FUTURE RISK LABEL (NO DATA LEAKAGE)
# ======================================================

def risk_label(count):
    if count >= 10:
        return "High"
    elif count >= 3:
        return "Medium"
    else:
        return "Low"

# Predict NEXT DAY risk using TODAY features
df["future_risk"] = (
    df.groupby(["lat_bin", "lon_bin"])["fire_count"]
    .shift(-1)
    .fillna(0)
    .apply(risk_label)
)

print("\nFuture Risk Distribution:")
print(df["future_risk"].value_counts())

# ======================================================
# 3. SELECT FEATURES & TARGET
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
# 4. TRAIN / TEST SPLIT
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ======================================================
# 5. TRAIN RANDOM FOREST MODEL
# ======================================================

print("\nTraining RandomForest model...")

model = RandomForestClassifier(
    n_estimators=120,
    max_depth=15,
    min_samples_leaf=20,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ======================================================
# 6. EVALUATION
# ======================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\n✅ MODEL ACCURACY: {accuracy * 100:.2f} %\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# ======================================================
# 7. FEATURE IMPORTANCE
# ======================================================

importance_df = pd.DataFrame({
    "feature": FEATURES,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\n🔥 Feature Importance:")
print(importance_df)

# ======================================================
# 8. SAVE PREDICTIONS (FIXED INDEX ISSUE)
# ======================================================

df_out = df.loc[X_test.index].copy()
df_out["predicted_risk"] = y_pred

df_out.to_csv(OUTPUT_PATH, index=False)

print("\n🔥 TYPE-1 MODEL BUILDING COMPLETED 🔥")
print("Predictions saved to:", OUTPUT_PATH)
