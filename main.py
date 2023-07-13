from twilio.rest import Client
import requests
import urllib.parse

account_sid = 
auth_token = 

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
weather_data = response.json()
weather_slice = weather_data['weather'][0]
# print(weather_slice)

mensagem = ''

condition_code = weather_slice['id']
if int(condition_code) < 700:
    mensagem = "Bring an umbrella."
else:
    mensagem = "Clear sky"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=mensagem,
    from_="+12345162408",
    to="+5511941109001"
)
print(message.status)
