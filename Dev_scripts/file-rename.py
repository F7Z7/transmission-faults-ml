import os

Base_Path = "/Datasets"

voltage_dir = os.path.join(Base_Path, "Voltage")
current_dir = os.path.join(Base_Path, "Current")

for i, filename in enumerate(os.listdir(voltage_dir)):
    if filename.lower().endswith(".xlsx"):
        old_path = os.path.join(voltage_dir, filename)
        new_name = f"voltage_{i}.xlsx"
        new_path = os.path.join(voltage_dir, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
for i, filename in enumerate(os.listdir(current_dir)):
    if filename.lower().endswith(".xlsx"):
        old_path = os.path.join(current_dir, filename)
        new_name = f"current_{i}.xlsx"
        new_path = os.path.join(current_dir, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
