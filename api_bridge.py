"""
This module contains the functionalities needed to correctly
bridge the FlaskyWeather API with another weather API
and provide the information in the required format
"""
import requests
import os
from datetime import datetime

base_url = "http://api.openweathermap.org/data/2.5/weather?units=metric&q="
api_id_param = "&appid=" + os.getenv('API_ID')


def bridge(args):
    """Acts as a bridge between both APIs
    requesting the information from openweathermap API
    and returning the required data to the FlaskyWeather
    in the correct format

    Args:
        args (dict): Both arguments pased to the FlaskyWeather API

    Returns:
        tuple: An answer and a status code
    """
    q_param = args["city"] + "," + args["country"]
    complete_url = base_url + q_param + api_id_param
    response = requests.get(complete_url)
    if response.status_code != 200:
        return (f"We couldn't find the city '{args['city']}' with the \
country code '{args['country']}'", 404)
    return answer_builder(response.json()), 200


def answer_builder(resp):
    """Builds the dictionary to return in case that the
    bridged API did find the given location

    Args:
        resp (dict): Dictionary from the API's response

    Returns:
        dict: Built dictionary with the required data in the given format
    """
    return {
        "location_name": f"{resp['name']}, {resp['sys']['country']}",
        "temperature": str(resp['main']['temp']) + " °C",
        "wind": f"{resp['wind']['speed']} m/s, {resp['wind']['deg']} degrees",
        "cloudiness": resp['weather'][0]['description'],
        "pressure": f"{resp['main']['pressure']} hpa",
        "humidity": str(resp['main']['humidity']) + "%",
        "sunrise": datetime.fromtimestamp(
            resp['sys']['sunrise']).strftime('%H:%M'),
        "sunset": datetime.fromtimestamp(
            resp['sys']['sunset']).strftime('%H:%M'),
        "geo_coordinates": f"[{resp['coord']['lat']}, {resp['coord']['lon']}]",
        "requested_time": str(datetime.now()).split('.')[0]
    }
