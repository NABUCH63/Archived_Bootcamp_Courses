# Weather Analysis

## Background

Created a weather database search based on randomly generated lat/lon pairs. These were then associated with the nearest city via "citipy". The resulting cities were used to search for the most recent weather data calling the "OpenWeather API". The final output was "WeatherPY_Database.csv", listing each city and it's associtated weather information.

The WeatherPy_Database.csv was input into google's Places API to find the nearest hotel to the city's latitude and longitude. The hotel name was appended to the existing dataframe. This dataframe was then used to filter down to a desired temperature range, and output a new dataframe of potential desintations as "Hotel_Search_Results.csv".

The destinations were used to select 4 locations within driving range. These were input into a directions layer and overlayed on a gmaps figure. The resulting routes and locaiton markers were output, along with the selected destinations as a separate file "Desitnations_Output.csv".

## Results

A nifty roadtrip through the central states at a refreshing summer temp.

## Challenges

Formatting latitude and longitudes for input into the API requests, and which python environment to use (jupyter or PyCharm) to get citipy/gmaps to function as intended. PyCharm could not display output figures with GMAPS. Jupyter Notebook could not call 'citipy' for an unknown reason, but other environments could.