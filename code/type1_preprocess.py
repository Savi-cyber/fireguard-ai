import pandas as pd

# ==============================
# 1. LOAD ALL FIRMS FILES
# ==============================

paths = [
    "type1 datasets/fire_nrt_J1V-C2_565335.csv",
    "type1 datasets/fire_nrt_M-C61_565334.csv",
    "type1 datasets/fire_nrt_SV-C2_565336.csv"
]



dfs = []

for path in paths:
    print(f"Loading {path}")
    df = pd.read_csv(path)
    dfs.append(df)

# ==============================
# 2. MERGE DATASETS
# ==============================

df = pd.concat(dfs, ignore_index=True)
print("Merged shape:", df.shape)

# ==============================
# 3. CLEAN COLUMN NAMES
# ==============================

df.columns = df.columns.str.strip()

# ==============================
# 4. REMOVE INVALID ROWS
# ==============================

df = df.dropna(subset=[
    'latitude',
    'longitude',
    'acq_date',
    'acq_time',
    'frp',
    'confidence'
])

print("After removing nulls:", df.shape)

# ==============================
# 5. FIX DATE & TIME
# ==============================

df['acq_date'] = pd.to_datetime(df['acq_date'])

df['acq_time'] = df['acq_time'].astype(str).str.zfill(4)

df['timestamp'] = pd.to_datetime(
    df['acq_date'].astype(str) + ' ' +
    df['acq_time'].str[:2] + ':' +
    df['acq_time'].str[2:]
)

# ==============================
# 6. SORT BY TIME
# ==============================

df = df.sort_values('timestamp')

# ==============================
# 7. REMOVE LOW CONFIDENCE FIRES
# ==============================

df = df[df['confidence'] != 'low']

print("After confidence filtering:", df.shape)

# ==============================
# 8. SPATIAL BINNING (AREA CREATION)
# ==============================

df['lat_bin'] = df['latitude'].round(2)
df['lon_bin'] = df['longitude'].round(2)

# ==============================
# 9. SAVE CLEAN DATA
# ==============================
df.to_csv("result/type1_cleaned_firms.csv", index=False)

print("\n🔥 TYPE-1 PREPROCESSING COMPLETED 🔥")
