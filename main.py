from twilio.rest import Client

import requests
import urllib.parse

address = input("Address: ")
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

Lon_lat = requests.get(url).json()
lat = Lon_lat[0]["lat"]
lon = Lon_lat[0]["lon"]
Weatherbi_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
api_key = "ab8a50326b3cd07d6e57040f58f4f3f6"
# print(lon)
# print(lat)


weather_params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
}

response = requests.get(Weatherbi_Endpoint, params=weather_params)
response.raise_for_status()
print(response)


# will_rain = False
#
# for hour_data in weather_slice:
#     condition_code = hour_data['weather'][0]['id']
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
    # print("Bring an umbrella.")
