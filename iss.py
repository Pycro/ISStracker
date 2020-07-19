#A sequence of API requests to gather available data on the ISS

import json
import urllib.request
import time

#my coords (note you need to put your coords here! currently set for the Wirral UK)
lat = 53.3121
lon = -2.9642

#Get the list of next passovers in JSON format
url = 'http://api.open-notify.org/iss-pass.json'
url = url +'?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(str(len(result['response'])) + ' passovers of ISS coming up for your location')
print()
print('Datetime\t\t\t\tDuration(Mins)')

#Loop through the JSON and extract the passover time and duration
#convert the duration from seconds to minutes
for i in range(0,len(result['response'])):
    passtime = time.ctime(result['response'][i]['risetime'])
    duration = "{:.2f}".format(float(result['response'][i]['duration']/60))
    print(passtime+'\t\t'+str(duration))

print()
print('Current location')

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print(result)
lat = result['iss_position']['latitude']
lon = result['iss_position']['longitude']
print('Latitude : ' + str(lat))
print('Longitude : ' + str(lon))

#url to make to resolve coords
#https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=-34.44076&lon=-58.70521


url = 'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat='+str(lat)+ '&lon='+str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print()
try:
    if str(result).startswith("{'error'"):
        print("Unable to provide location over water")
    else:
        pass#print(result)
except:
    pass
try:
    print('City : ' + str(result['address']['city']))
except:
    pass
try:
    print('State : ' + str(result['address']['state']))
except:
    pass
try:
    print('Country : ' + str(result['address']['country']))
except:
    pass

#Get the crew information details

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
#print(result)
print()
print('Crewcount : ' + str(result['number']))
crewcount = int(result['number'])
for i in range(0,crewcount):
    print(result['people'][i]['name'])
