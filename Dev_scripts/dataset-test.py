import pandas as pd

#for testing datasets
voltage_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Voltage\\voltage_0.csv"
current_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Current\\current_0.csv"


for dataset in [voltage_dataset,current_dataset]:
    df = pd.read_csv(dataset, header=1)
    print(df.head(20))