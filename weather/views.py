import requests
from django.shortcuts import render


def index(request):
    city = 'Warsaw'
    api_key = 'YOUR_API_KEY'  # Placeholder, replace with a real key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_temperature = data['main']['temp']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        context = {
            'city': city,
            'current_temperature': current_temperature,
            'description': description,
            'icon': icon,
        }
        return render(request, 'weather/index.html', context)
    else:
        return render(request, 'weather/index.html', {'error': 'Failed to fetch weather data.'})
