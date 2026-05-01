import os
import joblib

from src.preprocess import load_data, preprocess
from src.train import train_model
from src.evaluate import evaluate

os.makedirs("results", exist_ok=True)
os.makedirs("models", exist_ok=True)

print("Loading dataset...")
df = load_data()

print("Preprocessing...")
X, y = preprocess(df)

print("Training model...")
model, X_test, y_test, preds, mae, rmse, r2 = train_model(X, y)

evaluate(y_test, preds)


def allocate(load):
    if load < 100:
        return "LOW → Normal Routing"
    elif load < 500:
        return "MEDIUM → Moderate Scaling"
    else:
        return "HIGH → Increase Bandwidth"

allocations = [allocate(p) for p in preds[:20]]

# Save output
with open("results/allocation_output.txt", "w", encoding="utf-8") as f:
    for i, val in enumerate(allocations):
        f.write(f"Prediction {i}: {val}\n")


print("\nOutputs generated:")
print("- prediction_vs_actual.png")
print("- allocation_output.txt")
print("Model saved: models/model.pkl")
print("\nMODEL PERFORMANCE")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.2f}")