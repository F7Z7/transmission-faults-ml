import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# -----------------------------
# Load PMU data
# -----------------------------
df = pd.read_csv("../Datasets/Combined/combined_voltage_current.csv")

# Load anomaly indices (global PMU sample indices)
anomaly_idx = np.load("../datas/global_anomaly_indices.npy")

# Keep only valid indices
anomaly_idx = anomaly_idx[anomaly_idx < len(df)]

# -----------------------------
# Extract anomalous samples
# -----------------------------
fault_data = df.iloc[anomaly_idx][
    ["VBM","VRM","VYM","IBM","IRM","IYM"]
].copy()

# -----------------------------
# Feature Engineering
# -----------------------------
fault_data["Voltage_Unbalance"] = fault_data[["VBM","VRM","VYM"]].std(axis=1)
fault_data["Current_Unbalance"] = fault_data[["IBM","IRM","IYM"]].std(axis=1)

# -----------------------------
# Normalize
# -----------------------------
X = fault_data[
    ["Voltage_Unbalance","Current_Unbalance"]
]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# K-Means
# -----------------------------
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)

fault_data["Cluster"] = labels

print("\nCluster Counts")
print(fault_data["Cluster"].value_counts())

# Save results
fault_data.to_csv("../datas/fault_clusters.csv", index=False)

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

centroid_df = pd.DataFrame(
    centroids,
    columns=["Voltage_Unbalance", "Current_Unbalance"]
)

print(centroid_df)

centroid_df.to_csv("../datas/cluster_centroids.csv", index=False)
# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(8,6))

plt.scatter(
    fault_data["Voltage_Unbalance"],
    fault_data["Current_Unbalance"],
    c=labels,
    cmap="tab10",
    s=40
)

plt.xlabel("Voltage Unbalance")
plt.ylabel("Current Unbalance")
plt.title("Clustering of Detected Faults")

plt.grid(True)
plt.show()