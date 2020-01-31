import json
import urllib
import re
from urllib.request import urlopen

url = "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fweather.gc.ca%2Frss%2Fcity%2Fbc-66_e.xml"
#url = "https://weather.gc.ca/rss/city/bc-85_e.xml"
json_url = urlopen(url)
data = json.loads(json_url.read())
# key[0] is for watches and warnings
# key[1] is for current conditions
# key[2] is for the forecast
#for key in data:
#    print(key, '->', data[key], '\n')

print("\n\n*****************************\n\n")
#print ("Here is the data: \n\n\n")
print("Watches and Warnings")
print(data["items"][0]["title"])
#print("Current Conditions\n\n")
#print(data["items"][1]["title"])
#print("\n\n\nLots of data to sort out\n\n\n")
#print(data["items"][1]["description"])
clean_description = data["items"][1]["description"]
#print ("This is clean_description")

clean_description = clean_description.replace('<b>','\n')
clean_description = clean_description.replace('</b>','')
clean_description = clean_description.replace('<br>','\t')

#print ("This is the cleaned up description")
print (clean_description)
print ("72 hour weather forecast:\n")
print(data["items"][2]["title"])
#print("next part...\n\n******************************\n")
print(data["items"][3]["title"])
print(data["items"][4]["title"])
print(data["items"][5]["title"])
print(data["items"][6]["title"])
print(data["items"][7]["title"])
print(data["items"][8]["title"])
print(data["items"][9]["title"])

