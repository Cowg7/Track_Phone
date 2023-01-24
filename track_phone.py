import phonenumbers 
import folium
from my_number import number

from phonenumbers import geocoder

Key = '4ac064a03ddf4454a125045e788fc0bc'
samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "es")
print(yourLocation)

##obtener proveedor de servicios

from phonenumbers import carrier

service_proveedor = phonenumbers.parse(number)
print(carrier.name_for_number(service_proveedor, "es"))

##obtener long y lat en maps

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
##print(result)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

##guardamos el mapa en un archivo html

myMap.save("myLocation.html")