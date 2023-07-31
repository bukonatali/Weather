import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = '692034af11928db5760d7045bfbbf478'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    # для сохранения данных в табличке
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        if res.get('main'):
            city_info = {
                'city': city.name,
                'temp': res(res['main']['temp']),
                'icon': res['weather'][0]['icon'],
                'error': False,
            }
        else:
            city_info = {
                'city': city.name,
                'error': True,
            }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
