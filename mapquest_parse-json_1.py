import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago"
dest = "Ovalle"
key = "ReJI2akLmDH1HLRsNV4LsMuSxc1rdV7k"
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
json_data = requests.get(url).json()
print(json_data)
