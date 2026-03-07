import os

import pandas as pd

voltage_files = [
    r"C:\Users\farza\transmission-faults-ml\Datasets\Voltage\cleaned\voltage_0.csv",
    r"C:\Users\farza\transmission-faults-ml\Datasets\Voltage\cleaned\voltage_1.csv",
    r"C:\Users\farza\transmission-faults-ml\Datasets\Voltage\cleaned\voltage_2.csv"
]

current_files = [
    r"C:\Users\farza\transmission-faults-ml\Datasets\Current\cleaned\current_0.csv",
    r"C:\Users\farza\transmission-faults-ml\Datasets\Current\cleaned\current_1.csv",
    r"C:\Users\farza\transmission-faults-ml\Datasets\Current\cleaned\current_2.csv"
]

DEST_DIR=r"C:\Users\farza\transmission-faults-ml\Datasets\Combined"

os.makedirs(DEST_DIR,exist_ok=True)

merged_dataset=[]

for volt_set,curr_set in zip(voltage_files,current_files):
    df_volt = pd.read_csv(volt_set)
    df_curr = pd.read_csv(curr_set)

    merged_df = pd.merge(df_volt, df_curr, on="STARTDATE", how="inner", suffixes=('_volt', '_curr'))

    merged_dataset.append(merged_df)


volt_curr_combined_dataset=pd.concat(merged_dataset,ignore_index=True)


volt_curr_combined_dataset=volt_curr_combined_dataset.sort_values("STARTDATE")

print(volt_curr_combined_dataset.shape)
print(volt_curr_combined_dataset.head())

output_path = os.path.join(DEST_DIR, "combined_voltage_current.csv")
volt_curr_combined_dataset.to_csv(output_path, index=False)

print("Saved to:", output_path)

