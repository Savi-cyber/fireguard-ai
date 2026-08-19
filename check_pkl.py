import joblib
import os

MODEL_PATH = "models/type1_model.pkl"

if os.path.exists(MODEL_PATH):
    bundle = joblib.load(MODEL_PATH)
    print("✅ PKL FILE LOADED SUCCESSFULLY")
    print("Keys in PKL:", bundle.keys())
else:
    print("❌ PKL FILE NOT FOUND")
