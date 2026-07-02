import numpy as np

# Load saved data
mse = np.load("../datas/mse.npy")
threshold = np.load("../datas/threshold.npy")
anomalies = np.load("../datas/anomalies.npy")
anomaly_idx = np.load("../datas/global_anomaly_indices.npy")

print("=" * 50)
print("AUTOENCODER ANOMALY STATISTICS")
print("=" * 50)

print(f"Total windows analyzed      : {len(mse)}")
print(f"Threshold                   : {threshold:.6f}")

print(f"Total gloabal anomalies detected    : {len(anomaly_idx)}")

print(
    f"Percentage anomalous        : "
    f"{100*len(anomaly_idx)/len(mse):.2f}%"
)

print("\nFirst 20 anomaly windows:")
print(anomaly_idx[:20])

print("\nReconstruction error statistics")
print(f"Mean MSE: {np.mean(mse):.6f}")
print(f"Std MSE : {np.std(mse):.6f}")
print(f"Min MSE : {np.min(mse):.6f}")
print(f"Max MSE : {np.max(mse):.6f}")

# contiguous fault regions
fault_regions = []

if len(anomaly_idx) > 0:
    start = anomaly_idx[0]
    prev = anomaly_idx[0]

    for idx in anomaly_idx[1:]:
        if idx == prev + 1:
            prev = idx
        else:
            fault_regions.append((start, prev))
            start = idx
            prev = idx

    fault_regions.append((start, prev))

print("\nDetected fault regions:")
for i, (s, e) in enumerate(fault_regions, 1):
    print(f"Fault {i}: window {s} -> {e}")

print("\nTotal fault regions:", len(fault_regions))

WINDOW_SIZE = 25
STEP = 5

print("\nFault locations in PMU samples:\n")

for i, (s, e) in enumerate(fault_regions, 1):

    sample_start = s * STEP
    sample_end = e * STEP + WINDOW_SIZE

    print(
        f"Fault {i}: "
        f"windows {s}-{e} "
        f"-> PMU samples {sample_start}-{sample_end}"
    )