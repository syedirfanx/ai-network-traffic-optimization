import matplotlib.pyplot as plt
import os

def evaluate(y_test, preds):
    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(8,5))
    plt.plot(y_test.values[:100], label="Actual")
    plt.plot(preds[:100], label="Predicted")
    plt.legend()
    plt.title("Network Traffic Prediction")
    plt.xlabel("Samples")
    plt.ylabel("Traffic Load")
    plt.tight_layout()
    plt.savefig("results/prediction_vs_actual.png")
    plt.close()