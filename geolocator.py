from geopy.geocoders import Nominatim

# Create the geolocator object eith a user-agent
geolocator = Nominatim(user_agent="geoapiExcercises")

# Get the city name from the user
place = input("Enter City Name: ")

# Geocode the Location
location = geolocator.geocode(place)

# print the geolocation details
print(location)