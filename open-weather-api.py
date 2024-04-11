import requests
APPID = 'Put your api-key here'

cities = ['London', 'Paris', 'Berlin', 'New York', 'Tokyo', 'Moscow']
temps = []

for city in cities:
    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                 params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': APPID})
    data = res.json()
    temps.append(data['main']['temp'])


import matplotlib.pyplot as plt


plt.bar(cities, temps)
plt.show()


