import os
import urllib.parse
import requests

KEY = os.getenv('API_KEY')
LOCATION = os.getenv('LOCATION', 'São Paulo')
FORECAST_HOUR_URI = os.getenv('FORECAST_HOUR_URI')
FORECAST_5D_URI = os.getenv('FORECAST_5D_URI')
LOCATION_URI = os.getenv('LOCATION_URI')


def parse_to_celsius(f_temperature):
    result = (float(f_temperature) - 32) * (5/9)
    return round(result)


def filter_city_from(cities):

    for city in cities:
        city_key_attr = [city.get('LocalizedName'),
            city.get("AdministrativeArea").get('LocalizedName')]

        if LOCATION in city_key_attr:
            if city.get("AdministrativeArea").get('LocalizedType') == 'State':
                return city


def get_location():
    
    response = requests.get(f'{LOCATION_URI}?apikey={KEY}&q={urllib.parse.quote(LOCATION)}')

    if response.status_code == 200:
        city = filter_city_from(response.json())
        return city.get('Key')


def get_forecast_for(hours, location):

    response = requests.get(f'{FORECAST_HOUR_URI}/{hours}hour/{location}?apikey={KEY}')

    if response.status_code == 200:

        forecast = []

        for hour in response.json():
            forecast.append({
                'date': hour.get('DateTime'),
                'status': hour.get('IconPhrase'),
                'temperature': parse_to_celsius(hour.get('Temperature').get('Value'))
            })

        return forecast


def get_5days_forecast(location):

    response = requests.get(f'{FORECAST_5D_URI}/{location}?apikey={KEY}')

    if response.status_code == 200:

        forecast = []

        for day in response.json().get('DailyForecasts'):
            forecast.append({
                'date': day.get('Date'),
                'status': day.get('Day').get('IconPhrase'),
                'max': parse_to_celsius(day.get('Temperature').get('Maximum').get('Value')),
                'min': parse_to_celsius(day.get('Temperature').get('Minimum').get('Value'))
            })

        return forecast


def get_forecast(event, context):

    location_key = get_location()

    return {
        'next_days': get_5days_forecast(location_key),
        'next_hours': get_forecast_for(12, location_key)
    }
