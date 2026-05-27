import requests


def get_weather(city_name, api_key):

    URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric', 
        'lang': 'ru'
    }
    
    try:
        response = requests.get(URL, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        
        print(f"\n")
        print(f"Погода в городе {city}, {country}")
        print("-"*35)
        print(f"Погода: {temp:.1f}°C, {description}")
        print(f"Влажность: {humidity}%")
        print(f"Давление: {pressure} гПа")

    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания. Попробуйте снова.")
    except requests.exceptions.ConnectionError:
        print("Ошибка: Нет соединения с сервером.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Ошибка: Неверный API ключ")
        else:
            print(f"Ошибка HTTP: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")


API_KEY = "9e424bba84946907eb93b72ae2c60058"
CITY = "Priozersk"

get_weather(CITY, API_KEY)