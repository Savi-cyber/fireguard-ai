import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INPUT_PATH = os.path.join(PROJECT_ROOT, "result", "type2_cleaned.csv")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "result", "type2_features.csv")

df = pd.read_csv(INPUT_PATH)

# =========================================
# CREATE RISK LABEL (RULE BASED)
# =========================================
# If area burned > 0 → fire occurred → High risk

df["risk"] = df["area"].apply(lambda x: "High" if x > 0 else "Low")

# =========================================
# DROP AREA (NOT USED IN PREDICTION)
# =========================================

df = df.drop(columns=["area"])

print("Feature rows:", df.shape)

df.to_csv(OUTPUT_PATH, index=False)

print("🔥 TYPE-2 FEATURE ENGINEERING COMPLETED 🔥")
