import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score
)

# ==========================================================
# Load fault feature data
# ==========================================================

df = pd.read_csv("../datas/fault_clusters.csv")

features = df[["Voltage_Unbalance", "Current_Unbalance"]]

# Standardize features
scaler = StandardScaler()
X = scaler.fit_transform(features)

# ==========================================================
# Validate Existing Clustering (K = 3)
# ==========================================================

labels = df["Cluster"]

print("=" * 60)
print("CLUSTER VALIDATION")
print("=" * 60)

sil = silhouette_score(X, labels)
db = davies_bouldin_score(X, labels)
ch = calinski_harabasz_score(X, labels)

print(f"Silhouette Score        : {sil:.4f}")
print(f"Davies-Bouldin Index    : {db:.4f}")
print(f"Calinski-Harabasz Score : {ch:.2f}")

print("\nInterpretation")

if sil > 0.70:
    print("Excellent cluster separation.")

elif sil > 0.50:
    print("Good cluster separation.")

elif sil > 0.25:
    print("Moderate cluster separation.")

else:
    print("Weak cluster separation.")

# ==========================================================
# Elbow Method
# ==========================================================

inertia = []

K = range(1, 8)

for k in K:
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)
    inertia.append(model.inertia_)

plt.figure(figsize=(7,5))
plt.plot(K, inertia, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.grid(True)
plt.show()

# ==========================================================
# Silhouette Score vs K
# ==========================================================

scores = []

for k in range(2,8):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X)

    scores.append(
        silhouette_score(X, labels)
    )

plt.figure(figsize=(7,5))
plt.plot(range(2,8), scores, marker="o")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Analysis")
plt.grid(True)
plt.show()

best_k = range(2,8)[scores.index(max(scores))]

print("\nSuggested K based on Silhouette Score :", best_k)