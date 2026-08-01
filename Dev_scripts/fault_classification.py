# fault_classification.py

import pandas as pd
import numpy as np

# ----------------------------------
# Load clustered fault information
# ----------------------------------

df = pd.read_csv("../datas/fault_clusters.csv")

print("=" * 60)
print("RULE-BASED FAULT CLASSIFICATION")
print("=" * 60)

fault_types = []

for _, row in df.iterrows():

    v = row["Voltage_Unbalance"]
    i = row["Current_Unbalance"]

    # --------------------------------------------------
    # Simple engineering rules
    # (These thresholds should be refined later)
    # --------------------------------------------------

    if i > 4.70 and v > 523:
        fault = "Severe Fault (Possible 3-Phase / LLL)"

    elif i > 4.58 and v > 523:
        fault = "Possible Line-Line (LL)"

    elif v < 510:
        fault = "Possible Single Line-Ground (LG)"

    else:
        fault = "Unknown / Mild Disturbance"

    fault_types.append(fault)

df["Predicted_Type"] = fault_types

print(df)

df.to_csv("../datas/fault_classification.csv", index=False)

print("\nClassification saved to fault_classification.csv")

print("\nSummary\n")

print(df["Predicted_Type"].value_counts())