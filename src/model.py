from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def train_model(df):
    features = ["Time", "Source", "Destination", "Protocol", "No."]
    X = df[features]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    # Save model
    pickle.dump(model, open("models/model.pkl", "wb"))

    return model, X_test, y_test