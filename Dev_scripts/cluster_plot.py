import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../datas/fault_clusters.csv")

colors = ["tab:blue", "tab:orange", "tab:green"]

plt.figure(figsize=(8,6))

for cluster in sorted(df["Cluster"].unique()):
    temp = df[df["Cluster"] == cluster]

    plt.scatter(
        temp["Voltage_Unbalance"],
        temp["Current_Unbalance"],
        s=70,
        label=f"Cluster {cluster}"
    )

# Plot centroids
centroids = df.groupby("Cluster")[["Voltage_Unbalance",
                                   "Current_Unbalance"]].mean()

plt.scatter(
    centroids["Voltage_Unbalance"],
    centroids["Current_Unbalance"],
    c="red",
    marker="X",
    s=250,
    label="Centroids"
)

plt.xlabel("Voltage Unbalance")
plt.ylabel("Current Unbalance")
plt.title("Fault Cluster Analysis")
plt.grid(True)
plt.legend()

plt.show()


