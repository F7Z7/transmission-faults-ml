import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Load data
X = np.load("../datas/X.npy")

# ---------------- SPLIT ----------------
split = int(0.7 * len(X))

X_train = X[:split]   # assume normal
X_test = X[split:]

# ---------------- MODEL ----------------
input_dim = X.shape[1]

model = Sequential([
    Dense(64, activation='relu', input_shape=(input_dim,)),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(input_dim)
])

model.compile(optimizer='adam', loss='mse')

# Train only on "normal"
model.fit(X_train, X_train, epochs=20, batch_size=32)

# ---------------- DETECTION ----------------
X_pred = model.predict(X_test)

mse = np.mean(np.power(X_test - X_pred, 2), axis=1)

# Threshold
threshold = np.mean(mse) + 3*np.std(mse)

print("Threshold:", threshold)

anomalies = mse > threshold

print("Total samples:", len(mse))
print("Anomalies detected:", anomalies.sum())


anomaly_idx = np.where(anomalies)[0]
print("First anomaly indices:", anomaly_idx[:20])

global_anomaly_idx = anomaly_idx + split


print("Global anomalies:")
print(global_anomaly_idx[:20])


# #save datas
# np.save("../datas/mse.npy", mse)
# np.save("../datas/threshold.npy", threshold)
# np.save("../datas/anomalies.npy", anomalies)
# np.save("../datas/global_anomaly_indices.npy",global_anomaly_idx)
#

plt.figure(figsize=(15,5))
plt.plot(mse)
plt.scatter(anomaly_idx, mse[anomaly_idx], color='red')
plt.axhline(threshold, color='green')
plt.xlabel("Sample")
plt.ylabel("Reconstruction Error")
plt.title("Autoencoder Anomaly Detection")
plt.show()
print("Total test samples:", len(X_test))
print("Detected faults:", np.sum(anomalies))

model.save("../models/pmu_autoencoder.keras")