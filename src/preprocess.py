import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    return pd.read_csv("data/packets.csv")

def preprocess(df):
    df = df.copy()

    # Encode categorical columns
    cat_cols = ["Source", "Destination", "Protocol"]

    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))

    # Remove non-numeric text columns
    drop_cols = ["Length", "Info"]
    drop_cols = [col for col in drop_cols if col in df.columns]

    X = df.drop(columns=drop_cols)
    y = df["Length"]

    return X, y