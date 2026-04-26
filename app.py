import pandas as pd
import pickle
from src.preprocess import load_data, preprocess
from src.allocation import allocate_resources

# Load data
df = load_data()
df = preprocess(df)

# Load model
model = pickle.load(open("models/model.pkl", "rb"))

features = ["Time", "Source", "Destination", "Protocol", "No."]
predictions = model.predict(df[features])

df["predicted_load"] = predictions

# Apply allocation logic
df["allocation"] = df["predicted_load"].apply(allocate_resources)

print(df[["Time", "Length", "predicted_load", "allocation"]].head())

df.to_csv("results/output.csv", index=False)