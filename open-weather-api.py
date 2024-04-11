import requests
APPID = '0bbadc1a26b25cadc263ef83f3c5d35e'

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


