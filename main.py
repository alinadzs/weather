import requests

city = 'Vladikavkaz, RU'
appid = '274529f20f3fe894f05c3b2e6986a9d3'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print(data)
print("город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Миниманьная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("скорость ветра:", data['wind']['speed'])
print("видимость:", data['visibility'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'run', 'APPID': appid})
data = res.json()
print(":")
for i in data['list']:
    print("дата <", i['dt_txt'], "> \r\nтемпература <", '{0:+3.0f}'.format(i['main']['temp']),
          "> \r\nпогодные условия <", i['weather'][0]['description'], ">")
    print("скорость ветра <", i['wind']['speed'], "> \r\nвидимость <", i['visibility'], ">")
    print("____________________________")
