import pandas as pd

#for testing datasets
voltage_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Voltage\\cleaned\\voltage_0.csv"
current_dataset="C:\\Users\\farza\\transmission-faults-ml\\Datasets\\Current\\cleaned\\current_0.csv"


for dataset in [voltage_dataset,current_dataset]:
    df = pd.read_csv(dataset)


    print(df.columns)

    # The columns are
    #     STARTDATE
    #     SubstationId
    #     DeviceType
    #     DeviceId
    #     PointName
    #     MeasurementId
    #     MeasurementData25hz
    #     MeasurementData25hz: Quality

# we only need
# STARTDATE
# PointName
# MeasurementData25hz