import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
desired_width = 1000
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', None)
df = pd.read_csv("climate_data.csv")

#converted Date colum from obj to Datetime & extracted new column (Year) from date column
df["Date"]= pd.to_datetime(df["Date"])
df['year'] = df['Date'].dt.year
#df.info()

new_data = df.set_index('Date')

#First_dataset
First_dataset_2014 = new_data["1-1-2014":"31-12-14"]
#print(data_2014)

#Second_dataset
df_1 = pd.read_csv("austin_weather.csv")

#Converted date oject to datetime for slicing specific date
df_1["Date"]= pd.to_datetime(df_1["Date"])

#making date an index
new_data_1 = df_1.set_index('Date')
Second_dataset_2014 = new_data_1["1-1-2014":"31-12-14"]
#print(Second_dataset)

fig, ax = plt.subplots(2, 1, sharey=True)
#Plotting Climate Data
ax[0].plot(First_dataset_2014.index, First_dataset_2014["Average temperature (°F)"])
ax[0].plot(First_dataset_2014.index, First_dataset_2014["Maximum temperature (°F)"])
ax[0].plot(First_dataset_2014.index, First_dataset_2014["Minimum temperature (°F)"])

#Plotting Austin data
ax[1].plot(Second_dataset_2014.index, Second_dataset_2014["TempHighF"])
ax[1].plot(Second_dataset_2014.index, Second_dataset_2014["TempAvgF"])
ax[1].plot(Second_dataset_2014.index, Second_dataset_2014["TempLowF"])




plt.show()

#df.info()
#print(df_1.isnull().sum())
#print(Second_dataset)