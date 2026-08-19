import joblib
import pandas as pd
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "type2_model.pkl")

bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
features = bundle["features"]

print("\n🔥 TYPE-2 MANUAL WEATHER RISK 🔥")

temp = float(input("Temperature: "))
RH = float(input("Humidity: "))
wind = float(input("Wind speed: "))
rain = float(input("Rainfall: "))

input_df = pd.DataFrame([{
    "temp": temp,
    "RH": RH,
    "wind": wind,
    "rain": rain
}])[features]

risk = model.predict(input_df)[0]
print("\nPredicted Weather Risk:", risk)
