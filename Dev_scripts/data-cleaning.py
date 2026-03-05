import pandas as pd
import os


SOURCE_DIR = "C:\\Users\\farza\\transmission-faults-ml\\Datasets"

voltage_raw_dir = os.path.join(SOURCE_DIR, "Voltage", "raw")
current_raw_dir = os.path.join(SOURCE_DIR, "Current", "raw")



voltage_clean_dir = os.path.join(SOURCE_DIR, "Voltage", "cleaned")
current_clean_dir = os.path.join(SOURCE_DIR, "Current", "cleaned")

os.makedirs(voltage_clean_dir, exist_ok=True)
os.makedirs(current_clean_dir, exist_ok=True)

#requ colmns

required_cols = [
    "STARTDATE",
    "PointName",
    "MeasurementData25hz"
]

def clean_dataset(input_path,output_path):
    if not os.path.exists(input_path):
        print("No such file:", input_path)
        return

    df=pd.read_csv(input_path)

    df=df[required_cols] #only keep the required ones

    df["STARTDATE"] = pd.to_datetime(df["STARTDATE"])

    df_wide = df.pivot_table(
        index="STARTDATE",
        columns="PointName",
        values="MeasurementData25hz"
    )

    df_wide = df_wide.sort_index()


    df_wide.to_csv(output_path)

    print(f"Saved cleaned file -> {output_path}")



for file in os.listdir(voltage_raw_dir):
    if file.endswith(".csv"):
        input_path = os.path.join(voltage_raw_dir, file)
        output_path = os.path.join(voltage_clean_dir, file)
        clean_dataset(input_path, output_path)


for file in os.listdir(current_raw_dir):
    if file.endswith(".csv"):
        input_path = os.path.join(current_raw_dir, file)
        output_path = os.path.join(current_clean_dir, file)
        clean_dataset(input_path, output_path)