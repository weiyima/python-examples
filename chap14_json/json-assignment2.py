import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?sensor=false&'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=2))       
    print('================== Extract key value =============')
    place_id = js["results"][0]["place_id"]
    print('Place ID:', place_id)
    continue

    count = 0

    for items in js:
        place_id = js["results"][count]["place_id"]
        count = count + 1
        print('Place ID:', place_id)
        continue



    # print(json.dumps(js, indent=4))
    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)
