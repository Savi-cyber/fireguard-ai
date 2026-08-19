import pandas as pd
import os

# ======================================================
# 0. ABSOLUTE PATH SETUP (100% SAFE)
# ======================================================

# Project root: wildfire prediction/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

RESULT_DIR = os.path.join(PROJECT_ROOT, "result")

INPUT_PATH = os.path.join(RESULT_DIR, "type1_cleaned_firms.csv")
OUTPUT_PATH = os.path.join(RESULT_DIR, "type1_features.csv")

print("PROJECT ROOT:", PROJECT_ROOT)
print("INPUT PATH:", INPUT_PATH)

# ======================================================
# 1. LOAD CLEANED FIRMS DATA
# ======================================================

if not os.path.exists(INPUT_PATH):
    raise FileNotFoundError(f"❌ File not found: {INPUT_PATH}")

df = pd.read_csv(INPUT_PATH, parse_dates=["timestamp"])

print("Loaded rows:", df.shape[0])
print("Loaded columns:", df.shape[1])

# ======================================================
# 2. DATE FEATURE
# ======================================================

df["date"] = df["timestamp"].dt.date

# ======================================================
# 3. DAY / NIGHT FLAG
# ======================================================

df["hour"] = df["timestamp"].dt.hour
df["is_night"] = ((df["hour"] < 6) | (df["hour"] >= 18)).astype(int)

# ======================================================
# 4. CONFIDENCE SCORE
# ======================================================

confidence_map = {"l": 0.3, "n": 0.6, "h": 1.0}
df["confidence_score"] = df["confidence"].map(confidence_map)

# ======================================================
# 5. AGGREGATION (AREA + DAY)
# ======================================================

print("Aggregating features...")

features = (
    df.groupby(["lat_bin", "lon_bin", "date"])
    .agg(
        fire_count=("frp", "count"),
        avg_frp=("frp", "mean"),
        max_frp=("frp", "max"),
        night_fire_ratio=("is_night", "mean"),
        confidence_score=("confidence_score", "mean"),
    )
    .reset_index()
)

# ======================================================
# 6. FIRE TREND
# ======================================================

features = features.sort_values(["lat_bin", "lon_bin", "date"])

features["fire_trend"] = (
    features.groupby(["lat_bin", "lon_bin"])["fire_count"]
    .diff()
    .fillna(0)
)

# ======================================================
# 7. CLIP EXTREMES
# ======================================================

features["avg_frp"] = features["avg_frp"].clip(upper=500)
features["max_frp"] = features["max_frp"].clip(upper=1000)

# ======================================================
# 8. SAVE
# ======================================================

features.to_csv(OUTPUT_PATH, index=False)

print("\n🔥 TYPE-1 FEATURE ENGINEERING COMPLETED 🔥")
print("Saved to:", OUTPUT_PATH)
