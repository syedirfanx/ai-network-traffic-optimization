from src.preprocess import load_data, preprocess
from src.model import train_model

df = load_data()
df = preprocess(df)

train_model(df)