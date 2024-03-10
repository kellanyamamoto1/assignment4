# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kellan Yamamoto
# kellany@uci.edu
# 28388886

from OpenWeather import OpenWeather
import json
from LastFM import LastFM
from Profile import Profile, Post
from WebAPI import WebAPI

def test_api(message:str, apikey:str, webapi:WebAPI):
        webapi.set_apikey(apikey)
        webapi.load_data()
        result = webapi.transclude(message)
        print(result)

def main():

    #PROFILE DOESNT WORK // DONT KNOW HOW TO CONNECT TO SERVER
    profile = Profile()
    message = input("Write sentance using Keywords: @lastfm, @weather: ")
    post = Post(message)
    profile.add_post(post)
    try:
        profile.load_profile('profile.dsu')
    except Exception as ex:
        print(f"Error loading profile: {ex}")
        return

    posts = profile.get_posts()
    if len(posts) == 0:
        print("No posts found in the profile")
        return

    latest_post = posts[-1]
    print(f"Latest post timestamp: {latest_post.timestamp}")
    print(f"Latest post message: {latest_post.entry}")



    zipcode = "92697"
    ccode = "US"
    apikey = "ceb8cbc931c2f41301ba4a1548020fd4"

    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()
    open_weather.transclude(message)

    print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
    print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
    print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
    print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    print(f"The current weather for {zipcode} is {open_weather.description}")
    print(f"The current humidity for {zipcode} is {open_weather.humidity}")
    print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")

    FMapikey = "7cd2ee13dc3b0100dae94c5c7401df50"
    artist = 'Cher'
    album = 'Believe'
    lastfm = LastFM()
    lastfm.setFMapi(FMapikey)
    lastfm.set_artist_album(artist, album)
    lastfm.transclude(message)
    data = lastfm.loadFMdata()

    print(json.dumps(data, indent=4))

    test_api("Testing the weather: @weather", "ceb8cbc931c2f41301ba4a1548020fd4", open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

    test_api("Testing lastFM: @lastfm", "7cd2ee13dc3b0100dae94c5c7401df50", lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword


if __name__ == "__main__":
    main()

