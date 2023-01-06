from django.shortcuts import render, redirect
import requests


def home(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=9dd0c1f8e8a2d10485c888ca2b027a38"
    
    if request.method == "POST":
        search = request.POST['search']
        r = requests.get(url.format(search)).json()
        
        city_weather = {
            'city': search,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        return render(request, 'weather/index.html',{'weather':city_weather})
    else:
        city = 'Abuja'
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        return render(request, 'weather/index.html',{'weather':city_weather})