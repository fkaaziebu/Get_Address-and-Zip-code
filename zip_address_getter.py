from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="geoapiExercises")

# Get the city name from the user
place = input("Enter City Name: ")

# Geocode the location
location = ""
try:
    location = geolocator.geocode(place)
except Exception as e:
    print("Error loading address and zip codes:", str(e))

# Print the geolocation details
print(location)