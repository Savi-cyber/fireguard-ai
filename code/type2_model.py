import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "result", "type2_features.csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "type2_model.pkl")

df = pd.read_csv(DATA_PATH)

FEATURES = ["temp", "RH", "wind", "rain"]

X = df[FEATURES]
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=150,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
print("✅ TYPE-2 MODEL ACCURACY:", round(acc * 100, 2), "%")

bundle = {
    "model": model,
    "features": FEATURES,
    "risk_levels": ["Low", "High"]
}

joblib.dump(bundle, MODEL_PATH)

print("🔥 TYPE-2 MODEL SAVED 🔥")
