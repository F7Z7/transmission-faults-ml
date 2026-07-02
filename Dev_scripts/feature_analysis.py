import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../Datasets/Combined/combined_voltage_current.csv"
)

# normal operation
normal = df.iloc[0:3000].copy()

# largest fault region
fault = df.iloc[66110:66310].copy()

print("="*50)
print("NORMAL")
print("="*50)
print(normal.describe())

print("\n")
print("="*50)
print("FAULT")
print("="*50)
print(fault.describe())

normal["Voltage_Unbalance"] = \
    normal[["VBM","VRM","VYM"]].std(axis=1)

normal["Current_Unbalance"] = \
    normal[["IBM","IRM","IYM"]].std(axis=1)

fault["Voltage_Unbalance"] = \
    fault[["VBM","VRM","VYM"]].std(axis=1)

fault["Current_Unbalance"] = \
    fault[["IBM","IRM","IYM"]].std(axis=1)

print("\nVoltage Unbalance")
print("Normal:", normal["Voltage_Unbalance"].mean())
print("Fault :", fault["Voltage_Unbalance"].mean())

print("\nCurrent Unbalance")
print("Normal:", normal["Current_Unbalance"].mean())
print("Fault :", fault["Current_Unbalance"].mean())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(normal["Voltage_Unbalance"])
plt.title("Normal Voltage Unbalance")
plt.xlabel("Sample")
plt.ylabel("Std(VBM, VRM, VYM)")

plt.subplot(1,2,2)
plt.plot(fault["Voltage_Unbalance"])
plt.title("Fault Voltage Unbalance")
plt.xlabel("Sample")
plt.ylabel("Std(VBM, VRM, VYM)")

plt.tight_layout()
plt.show()

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(normal["Current_Unbalance"])
plt.title("Normal Current Unbalance")

plt.subplot(1,2,2)
plt.plot(fault["Current_Unbalance"])
plt.title("Fault Current Unbalance")

plt.tight_layout()
plt.show()