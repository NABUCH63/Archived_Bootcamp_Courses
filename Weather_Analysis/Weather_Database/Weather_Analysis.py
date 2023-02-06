# Import dependencies
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime
import requests
from citipy import citipy
from config import OpenWeather_API_Key

# create empty lat/lon lists
lat = []
lon = []

# fill lists with random numbers per criteria
lat = np.random.uniform(low=-90, high=90, size=2000)
lon = np.random.uniform(low=-180, high=180, size=2000)

# zip together arrays into single list
cord = zip(lat, lon)
city_cord = list(cord)

# create empty lists for cities and countries
cities = []
countries = []

# loop through length of coordinate list generated, call citipy to append city data to lists
i = 0
for cords in range(0, len(city_cord)):

    if citipy.nearest_city(city_cord[cords][0], city_cord[cords][1]).city_name not in cities:
        cities.append(citipy.nearest_city(city_cord[cords][0], city_cord[cords][1]).city_name)
        countries.append(citipy.nearest_city(city_cord[cords][0], city_cord[cords][1]).country_code)
        i = i + 1
    print(f"Added New city {i}")

# zip arrays into single list of city, country
city_country = zip(cities, countries)
city_list = list(city_country)

# base URL of OpenWeather API
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + OpenWeather_API_Key

# create empty list for Wx data and initiate printout counters
city_data = []
record_count = 1
set_count = 1

# loop through all the cities in our list
for i, city in enumerate(cities):

# group cities in sets of 50 to limit API calls
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        time.sleep(60)

# create endpoint URL with each city based on city list. Replace any spaces with '+'.
    city_url = url + "&q=" + city.replace(" ", "+")

# log URL, record, and set numbers and the city
    print(f"Processed Record {record_count} of set {set_count} | {city}")

# add to the record count
    record_count +=1

# Run an API request for each of the cities
    try:

# Parse out the needed data
        city_weather = requests.get(city_url).json()
        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]
        city_desc = city_weather["weather"][0]["description"]

# convert the date to ISO format
        city_date = datetime.utcfromtimestamp(city_weather["dt"]).strftime("%Y-%m-%d %H:%M:%S")

# append the city data to the city_data list
        city_data.append({
            "City": cities[i].title(),
            "Lat": city_lat,
            "Lon": city_lng,
            "Max_Temp_(F)": city_max_temp,
            "Humidity_%": city_humidity,
            "Cloud_%": city_clouds,
            "Wind_Spd": city_wind,
            "Wx_Desc": city_desc,
            "Country": city_country,
            "Date": city_date})

# if an error is experienced, skip the city
    except IndexError:
        print(f"City Not Found. Skipping...")
    except KeyError:
        print(f"City Not Found. Skipping...")

# indicate the data loading is complete
print("-----------------")
print(f"Data Retrieval Completed")
print(f"----------------")

# Create dataframe from City Wx dataset
City_Wx_df = pd.DataFrame(city_data)

#reorder columns
City_Wx_df = City_Wx_df[["City", "Country", "Date", "Lat", "Lon", "Wx_Desc", "Max_Temp_(F)", "Humidity_%", "Cloud_%", "Wind_Spd"]]
print(City_Wx_df.head(10))

# create output CSV file for Wx data
City_Wx_df.to_csv("Output/WeatherPY_Database.csv", index_label="City_ID")

