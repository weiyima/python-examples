import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
#address = 'http://py4e-data.dr-chuck.net/comments_6039.xml'

address = input('Enter location: ')
#if len(address) < 1: break
print('Retrieving', address)    
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')

#print(data.decode())
tree = ET.fromstring(data)

count = 0
sumtotal = 0
for i in tree.findall('.//count'):
    sumtotal = sumtotal + int(i.text)
    count = count + 1

print('Count:',count)
print('Sum:',sumtotal)

