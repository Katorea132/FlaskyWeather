# FlaskyWeather
This project provides information about a given city and country, identifying the former with a string and the later with a 2 letter country code in lowercase.
You'll require to install:
  - python 3.6 or later

Once you have python 3.6+ installed, follow these steps:
  - run from a command line "python3 -m venv name_of_venv" (or the equivalent for your OS), this will create a virtual environment in the current directory
  - activate the virtual environment with "source name_of_venv/bin/activate", assuming you are still on the same directory
  - Clonate this repository in your desired location
  - Run, inside the clonated repository directory "pip3 install -r requirements.txt"

With that you'll have the required elements to run the API, but there are 2 enviromental variables needed:
  - FLASK_ENV: This defaults to "production", if you want it running on debug mode, make sure to set this to "development".
  - API_ID: This is needed to access the openweathermap API, without this properly set with a valid id, the program won't start.

### Endpoints

- > get "/" - This will give you a short explanation on how to use the API
- > get "/weather" - This is the main endpoint, you'll need to provide a "city" and "country" parameter else, it will throw an error.
The city parameter must be a string and the country one a 2 letter string, consisting only of lower cap letters

example = '/weather?country=co&city=medellin'

This API will cache the answers for 2 minutes, so different requests from the same source will be met with the first response in a time lapse of the first 2 minutes.
This behaviour is not present on the debug mode for easier testing.

* The sunset and sunrise time are given in server time, which is, most likely, -5 gtm
