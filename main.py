#  import phone numbers after pip install
import phonenumbers

#  import opencage to view location
import opencage
from opencage.geocoder import OpenCageGeocode

# import folium
import folium

# import phone number from myphone
from myphone import number

# import geocoder from phonenumbers
from phonenumbers import geocoder

# import carrier to view the service provider
from phonenumbers import carrier



# 
pepnumber = phonenumbers.parse(number)

# extract country location
location = geocoder.description_for_number(pepnumber, "en")

print(location)

# viewing the service provider 
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

api_key = 'eb394b806fe54a228d2d2bf492bfaed4'

geocoder = OpenCageGeocode(api_key)

query = str(location)
results = geocoder.geocode(query)
# print(results)

# extract just the latitude and the longitude 
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng'] 

print(latitude, longitude)

myMap = folium.Map(location=[latitude, longitude], zoom_start=9)
folium.Marker([latitude, longitude], popup=location).add_to(myMap)

# save the information in a file
myMap.save("mylocation.html")

