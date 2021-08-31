# Project repository: https://github.com/daviddrysdale/python-phonenumbers
# Damn module, no need.

import phonenumbers
from phonenumbers import carrier, geocoder, timezone

nmbr = phonenumbers.parse("+8801850561548")

# Get time zone
print(geocoder.description_for_number(nmbr,"en"))
