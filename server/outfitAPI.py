import requests, os

"""
API for providing outfits
"""

API_KEY = os.environ.get('OPEN_WEATHER_MAP_KEY', '2f1fc3af6d1791f4a078b27231ac4fad')

precipitation_jacket = ["drizzle", "snow", "rain", "blizzard", "hail", "ice", "heavy rain", "Extreme rain", "Extreme snow"]


def get_weather(city):
    weather = {}
    api_response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather',
        params={'q': city, 'APPID': API_KEY, "units": "metric"}
    )
    data = api_response.json()
    weather['temp'] = data['main']['temp']
    weather['precipitation'] = data['weather'][0]['main']

    return weather

def provide_outfit(city):
    """
    Provide a "Smart" outfit for the user.

    :return: JSON object
    """

    jacket_needed = False

    # Check weather
    weather = get_weather(city)
    if weather['precipitation'] in precipitation_jacket or weather['temp'] <= 10:
        jacket_needed = True

    if jacket_needed:
        # Check database for jacket.

    else:
        # 
