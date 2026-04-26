import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    df = pd.read_csv("data/packets.csv")
    return df

def preprocess(df):
    # Encode categorical variables
    le_protocol = LabelEncoder()
    le_source = LabelEncoder()
    le_dest = LabelEncoder()

    df["Protocol"] = le_protocol.fit_transform(df["Protocol"].astype(str))
    df["Source"] = le_source.fit_transform(df["Source"].astype(str))
    df["Destination"] = le_dest.fit_transform(df["Destination"].astype(str))

    # Target = network load
    df["target"] = df["Length"]

    return df