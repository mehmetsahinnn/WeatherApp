import requests
from django.shortcuts import render

def view_weather(request, lat, long):
    lat = float(lat)
    long = float(long)
    api_key = 'API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}'
    weather_data = requests.get(url).json()
    return render(request, 'view_weather.html', {'weather_data': weather_data})
