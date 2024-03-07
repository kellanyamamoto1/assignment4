# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

# API KEY: 7cd2ee13dc3b0100dae94c5c7401df50
# SHARED SECRET: 1c62c7b8c077d5ea2a1a70b4cb77b506


import urllib, json
from urllib import request,error
class LastFM:

    FMkey = None


    def setFMapi(self, FMapikey: str) -> None:
        self.apiKey = FMapikey

    def set_artist_album(self, artist: str, album: str) -> None:
        self.artist = artist
        self.album = album

    def loadFMdata(self):
        if self.apiKey is None:
            raise ValueError("API key is not set. Please use setFMapi method to set the API key.")
        if self.artist is None or self.album is None:
            raise ValueError("Artist or album is not set. Please use set_artist_album method to set the artist and album.")

        try:
            url = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={self.apiKey}&artist={self.artist}&album={self.album}&format=json"
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
        
    def transclude(self, message:str) -> str:
        words = message.split()
        for i, word in enumerate(words):
            if '@lastfm' in word:
                self.load_data()
                words[i] = word.replace('@lastfm', self.description)
        return ' '.join(words)



def main():
    FMapikey = "7cd2ee13dc3b0100dae94c5c7401df50"
    artist = 'Cher'
    album = 'Believe'
    lastfm = LastFM()
    lastfm.setFMapi(FMapikey)
    lastfm.set_artist_album(artist, album)
    data = lastfm.loadFMdata()
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()