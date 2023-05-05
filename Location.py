# # # importing geopy library
# # from geopy.geocoders import Nominatim

# # # calling the Nominatim tool
# # loc = Nominatim(user_agent="GetLoc")

# # # entering the location name
# # getLoc = loc.geocode("Nellore Andhra Pradesh")

# # # printing address
# # print(getLoc.address)

# # # printing latitude and longitude
# # print("Latitude = ", getLoc.latitude, "\n")
# # print("Longitude = ", getLoc.longitude)

# # import requests
# # import urllib.parse

# # address = 'Vikram Nagar, Nellore'
# # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

# # response = requests.get(url).json()
# # print(response[0]["lat"])
# # print(response[0]["lon"])


# import requests

# response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Nellore+Andhra+Pradesh')

# resp_json_payload = response.json()

# print(resp_json_payload['results'])

from geopy.geocoders import Nominatim

def get_coordinates(Address):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(Address)

    return (location.latitude, location.longitude)