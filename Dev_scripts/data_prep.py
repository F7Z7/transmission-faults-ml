import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

source=r"C:\Users\farza\transmission-faults-ml\Datasets\Combined\combined_voltage_current.csv"

df=pd.read_csv(source)

df = df.drop(columns=["STARTDATE"])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)


scaled_df=pd.DataFrame(scaled_data,columns=df.columns)

def create_windows(data, window_size=25, step=5):

    X = []

    for i in range(0, len(data) - window_size, step):
        window = data.iloc[i:i+window_size].values.flatten()
        X.append(window)

    return np.array(X)

X = create_windows(scaled_df)

print("Final ML shape:", X.shape)

# save for model
np.save("../datas/X.npy", X)