# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

# API KEY: 7cd2ee13dc3b0100dae94c5c7401df50
# SHARED SECRET: 1c62c7b8c077d5ea2a1a70b4cb77b506


import urllib, json, datetime
from urllib import request,error
class LastFM:

    FMkey = None

    def setFMapi(self, FMapikey: str) -> None:
        self.FMkey = FMapikey

    def loadFMdata(self):
        if self.FMkey is None:
            raise ValueError("API key is not set. Please use set_apikey method to set the API key.")
        
        try:
            url = f"http://www.last.fm/api/auth/?api_key={self.FMkey}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
           
            



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


def main():
    FMapikey = "7cd2ee13dc3b0100dae94c5c7401df50"
