# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

# API KEY: ceb8cbc931c2f41301ba4a1548020fd4


import urllib, json, datetime
from urllib import request,error
from ui import *

class OpenWeather:

    def __init__(self, zipcode=None, ccode=None):
        self.zipcode = zipcode
        self.ccode = ccode
        self.api_key = None
        self.weather_description = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.humidity = None
        self.city = None
        self.sunset = None

    api_key = None

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        if self.api_key is None:
            raise ValueError("API key is not set. Please use set_apikey method to set the API key.")
        
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.api_key}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            self.description = data['weather'][0]['description']
            self.temperature = data['main']['temp']
            self.high_temperature = data['main']['temp_max']
            self.low_temperature = data['main']['temp_min']
            self.longitude = data['coord']['lon']
            self.latitude = data['coord']['lat']
            self.humidity = data['main']['humidity']
            self.city = data['name']
            self.sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        except urllib.error.URLError as e:
            raise Exception(f"Lost local connection to the Internet: {e}")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise Exception("API service is unavailable: HTTP 404 - Not Found")
            elif e.code == 503:
                raise Exception("API service is unavailable: HTTP 503 - Service Unavailable")
            else:
                raise Exception(f"HTTP Error: {e.code} - {e.reason}")
        except json.JSONDecodeError as e:
            raise Exception("Invalid data formatting from the remote API")


    def set_apikey(self, apikey:str) -> None:
        '''    
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
    
        '''
        self.api_key = apikey
    
    def transclude(self, message:str) -> str:
        words = message.split()
        for i, word in enumerate(words):
            if '@weather' in word:
                self.load_data()
                words[i] = word.replace('@weather', self.description)
        return ' '.join(words)


def main() -> None:

    zipcode = "92697"
    ccode = "US"
    apikey = "ceb8cbc931c2f41301ba4a1548020fd4"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()


    

if __name__ == '__main__':
    main()