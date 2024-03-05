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
        
        url = f"https://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.api_key}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        self.weather_description = data['weather'][0]['description']
        self.temperature = data['main']['temp']
        self.high_temperature = data['main']['temp_max']
        self.low_temperature = data['main']['temp_min']
        self.longitude = data['coord']['lon']
        self.latitude = data['coord']['lat']
        self.humidity = data['main']['humidity']
        self.city = data['name']
        self.sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

    def set_apikey(self, apikey:str) -> None:
        '''    
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
    
        '''
        self.api_key = apikey
        

def main() -> None:

    zipcode = "92697"
    ccode = "US"
    apikey = "ceb8cbc931c2f41301ba4a1548020fd4"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
    print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
    print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
    print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    #print(f"The current weather for {zipcode} is {open_weather.description}")
    print(f"The current humidity for {zipcode} is {open_weather.humidity}")
    print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")


    

if __name__ == '__main__':
    main()