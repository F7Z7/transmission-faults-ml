import os
import pandas as pd

Base_Path = "C:\\Users\\farza\\transmission-faults-ml\\Datasets"

voltage_dir = os.path.join(Base_Path, "Voltage")
current_dir = os.path.join(Base_Path, "Current")

for filename in os.listdir(voltage_dir):
    if filename.endswith(".xlsx"):

        input_path = os.path.join(voltage_dir, filename)


        df = pd.read_excel(input_path)


        output_name = os.path.splitext(filename)[0] + ".csv"
        output_path = os.path.join(voltage_dir, output_name)


        df.to_csv(output_path, index=False)

        print(f"Converted: {filename} → {output_name}")