# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

# API KEY: ceb8cbc931c2f41301ba4a1548020fd4


import urllib, json
from urllib import request,error

class OpenWeather():

    def set_apikey(self, apikey:str) -> None:
        '''    
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
    
        '''
        self.api_key = apikey
        

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        if self.api_key is None:
            raise ValueError("API key is not set. Please use set_apikey method to set the API key.")
        
        url = f"https://api.openweathermap.org/data/2.5/weather?&appid={self.api_key}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        self.weather_description = data['weather'][0]['description']
        

def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj

def main() -> None:
    zip = "96797"
    ccode = "US"
    apikey = "ceb8cbc931c2f41301ba4a1548020fd4"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"
    
    weather = OpenWeather()
    weather.set_apikey("your_api_key_here")
    weather.load_data()
    print(weather.weather_description)

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj)


if __name__ == '__main__':
    main()