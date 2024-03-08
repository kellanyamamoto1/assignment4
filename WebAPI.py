# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886
import requests, json, urllib
from abc import ABC, abstractmethod

class WebAPI(ABC):

  def _download_url(self, url: str) -> dict:
    headers = {
      'User': 'Your User String'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      return response.json()
    else:
      # Handle error response
      return None

  def set_apikey(self, apikey:str) -> None:
    pass

  @abstractmethod
  def load_data(self):
    if self.apiKey is None:
            raise ValueError("API key is not set. Please use setFMapi method to set the API key.")
    if self.artist is None or self.album is None:
        raise ValueError("Artist or album is not set. Please use set_artist_album method to set the artist and album.")
    try:
        url = f""
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

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

  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
