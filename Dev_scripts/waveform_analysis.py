import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Load Data
# ============================================================

df = pd.read_csv("../Datasets/Combined/combined_voltage_current.csv")
anomaly_idx = np.load("../datas/global_anomaly_indices.npy")

WINDOW_SIZE = 5
PADDING = 150
FAULTS_PER_FIGURE = 4

# ============================================================
# Find Continuous Fault Regions
# ============================================================

fault_regions = []

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

print("=" * 60)
print("FAULT REGIONS")
print("=" * 60)

for i, (s, e) in enumerate(fault_regions, 1):
    print(f"Fault {i}: Window {s} -> {e}")

# ============================================================
# Plot Faults
# ============================================================

num_faults = len(fault_regions)

for fig_start in range(0, num_faults, FAULTS_PER_FIGURE):

    fig_end = min(fig_start + FAULTS_PER_FIGURE, num_faults)
    faults_in_fig = fig_end - fig_start

    fig, axes = plt.subplots(
        faults_in_fig,
        2,
        figsize=(15, 4 * faults_in_fig)
    )

    # If only one fault in figure, make axes 2D
    if faults_in_fig == 1:
        axes = np.array([axes])

    for row, fault_idx in enumerate(range(fig_start, fig_end)):

        start_window, end_window = fault_regions[fault_idx]

        start_sample = start_window * WINDOW_SIZE
        end_sample = end_window * WINDOW_SIZE + WINDOW_SIZE

        left = max(0, start_sample - PADDING)
        right = min(len(df), end_sample + PADDING)

        region = df.iloc[left:right]

        # ----------------------------------------------------
        # Voltage Plot
        # ----------------------------------------------------
        ax = axes[row, 0]

        ax.plot(region.index, region["VBM"], label="VBM")
        ax.plot(region.index, region["VRM"], label="VRM")
        ax.plot(region.index, region["VYM"], label="VYM")

        ax.axvspan(
            start_sample,
            end_sample,
            color="red",
            alpha=0.25,
            label="Detected Fault"
        )

        ax.set_title(f"Fault {fault_idx + 1} - Voltage")
        ax.set_ylabel("Voltage")
        ax.grid(True)
        ax.legend(fontsize=8)

        # ----------------------------------------------------
        # Current Plot
        # ----------------------------------------------------
        ax = axes[row, 1]

        ax.plot(region.index, region["IBM"], label="IBM")
        ax.plot(region.index, region["IRM"], label="IRM")
        ax.plot(region.index, region["IYM"], label="IYM")

        ax.axvspan(
            start_sample,
            end_sample,
            color="red",
            alpha=0.25,
            label="Detected Fault"
        )

        ax.set_title(f"Fault {fault_idx + 1} - Current")
        ax.set_ylabel("Current")
        ax.set_xlabel("PMU Sample")
        ax.grid(True)
        ax.legend(fontsize=8)

        print("-" * 60)
        print(f"Fault {fault_idx + 1}")
        print(f"Window Range : {start_window} - {end_window}")
        print(f"PMU Samples  : {start_sample} - {end_sample}")

    plt.tight_layout()
    plt.show()