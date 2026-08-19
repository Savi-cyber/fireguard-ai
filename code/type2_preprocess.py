import pandas as pd
import os

# =========================================
# PATH SETUP
# =========================================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "type2 dataset", "forestfires.csv")
OUTPUT_PATH = os.path.join(PROJECT_ROOT, "result", "type2_cleaned.csv")

print("Loading:", DATA_PATH)

df = pd.read_csv(DATA_PATH)

print("Original shape:", df.shape)

# =========================================
# KEEP ONLY REQUIRED COLUMNS
# =========================================

df = df[["temp", "RH", "wind", "rain", "area"]]

# =========================================
# HANDLE MISSING VALUES
# =========================================

df = df.dropna()

print("After cleaning:", df.shape)

# =========================================
# SAVE CLEANED DATA
# =========================================

df.to_csv(OUTPUT_PATH, index=False)

print("🔥 TYPE-2 PREPROCESSING COMPLETED 🔥")
