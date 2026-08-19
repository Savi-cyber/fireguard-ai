import pandas as pd

# Load Type-1 predictions
df = pd.read_csv("result/type1_predictions.csv")

# Check logic: risk vs fire history
check = df.groupby("predicted_risk")[["fire_count", "avg_frp"]].mean()

print("\n🔥 TYPE-1 LOGIC CHECK 🔥\n")
print(check)
