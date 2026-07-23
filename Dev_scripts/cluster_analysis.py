import pandas as pd

# Load clustered fault data
df = pd.read_csv("../datas/fault_clusters.csv")

print("=" * 60)
print("CLUSTER STATISTICS")
print("=" * 60)

stats = df.groupby("Cluster").agg({
    "Voltage_Unbalance": ["count", "mean", "std", "min", "max"],
    "Current_Unbalance": ["mean", "std", "min", "max"]
})

print(stats)

print("\n")

# Print in readable form
for cluster in sorted(df["Cluster"].unique()):
    c = df[df["Cluster"] == cluster]

    print("=" * 50)
    print(f"Cluster {cluster}")
    print("=" * 50)

    print(f"Samples : {len(c)}")

    print("\nVoltage Unbalance")
    print(f" Mean : {c['Voltage_Unbalance'].mean():.3f}")
    print(f" Std  : {c['Voltage_Unbalance'].std():.3f}")
    print(f" Min  : {c['Voltage_Unbalance'].min():.3f}")
    print(f" Max  : {c['Voltage_Unbalance'].max():.3f}")

    print("\nCurrent Unbalance")
    print(f" Mean : {c['Current_Unbalance'].mean():.3f}")
    print(f" Std  : {c['Current_Unbalance'].std():.3f}")
    print(f" Min  : {c['Current_Unbalance'].min():.3f}")
    print(f" Max  : {c['Current_Unbalance'].max():.3f}")

    print()

df = pd.read_csv("../datas/fault_clusters.csv")

print("="*60)
print("FAULT CLUSTER INTERPRETATION")
print("="*60)

for cluster in sorted(df["Cluster"].unique()):

    c = df[df["Cluster"] == cluster]

    print(f"\nCluster {cluster}")
    print(f"Number of anomalies : {len(c)}")

    print(f"Average Voltage Unbalance : {c['Voltage_Unbalance'].mean():.2f}")
    print(f"Average Current Unbalance : {c['Current_Unbalance'].mean():.2f}")

    if c["Current_Unbalance"].mean() > 4.7:
        print("Interpretation : High current unbalance disturbance")

    elif c["Current_Unbalance"].mean() > 4.6:
        print("Interpretation : Moderate disturbance")

    else:
        print("Interpretation : Mild disturbance")