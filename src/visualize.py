import matplotlib.pyplot as plt

def plot_results(df):
    plt.figure(figsize=(10,5))
    plt.plot(df["Length"], label="Actual Load")
    plt.plot(df["predicted_load"], label="Predicted Load")
    plt.legend()
    plt.title("Network Load Prediction")
    plt.savefig("results/traffic_prediction.png")
    plt.show()