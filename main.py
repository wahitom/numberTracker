#  import phone numbers after pip install
import phonenumbers

# import phone number from myphone
from myphone import number

# import geocoder from phonenumbers
from phonenumbers import geocoder

# 
pepnumber = phonenumbers.parse(number)

# extract country location
location = geocoder.description_for_number(pepnumber, "en")

print(location)