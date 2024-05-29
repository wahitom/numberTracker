#  import phone numbers after pip install
import phonenumbers

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
