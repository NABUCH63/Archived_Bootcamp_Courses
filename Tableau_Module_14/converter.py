import pandas as pd
from datetime import datetime as dt
data = "data/201908-citibike-tripdata.csv"

bike_data = pd.read_csv(data)
bike_dataframe = pd.DataFrame(bike_data)
names = list(bike_dataframe)
print(names)
bike_dataframe["starttime"] = pd.to_datetime(bike_dataframe["starttime"], infer_datetime_format=True)
bike_dataframe["stoptime"] = pd.to_datetime(bike_dataframe["stoptime"], infer_datetime_format=True)
bike_dataframe["tripduration"] = pd.to_datetime(bike_dataframe["tripduration"], unit="s")
print(bike_dataframe[["starttime", "stoptime", "tripduration"]])
print(bike_dataframe.dtypes)

bike_dataframe.to_csv("data/Converted_Bike1.csv", index=False)