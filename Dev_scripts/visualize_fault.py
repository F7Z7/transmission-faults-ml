import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(
    r"C:\Users\farza\transmission-faults-ml\Datasets\Combined\combined_voltage_current.csv"
)

# visualize region where autoencoder detected anomalies
start = 4700
end = 5300

plt.figure(figsize=(15,5))

plt.plot(df["VBM"][start:end], label="VBM")
plt.plot(df["VRM"][start:end], label="VRM")
plt.plot(df["VYM"][start:end], label="VYM")

plt.legend()
plt.title("Voltage around detected anomaly")
plt.show()


plt.figure(figsize=(15,5))

plt.plot(df["IBM"][start:end], label="IBM")
plt.plot(df["IRM"][start:end], label="IRM")
plt.plot(df["IYM"][start:end], label="IYM")

plt.legend()
plt.title("Current around detected anomaly")
plt.show()