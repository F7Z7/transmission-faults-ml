import pandas as pd

#for testing datasets
voltage_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Voltage\\voltage_0.xlsx"
current_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Current\\current_0.xlsx"


for dataset in [voltage_dataset,current_dataset]:
    df = pd.read_excel(dataset, header=1)
    print(df.head(20))