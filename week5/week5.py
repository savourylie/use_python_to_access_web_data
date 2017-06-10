from __future__ import print_function
import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter URL: ")
data = urllib.urlopen(url).read()
# print(data)

tree = ET.fromstring(data)
# print(tree)
counts = tree.findall('.//count')

result = 0

for count in counts:
	result += int(count.text)

print(result)

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

# while True:
#     address = raw_input('Enter location: ')
#     if len(address) < 1 : break

#     url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
#     print 'Retrieving', url
#     uh = urllib.urlopen(url)
#     data = uh.read()
#     print 'Retrieved',len(data),'characters'
#     print data
#     tree = ET.fromstring(data)


#     results = tree.findall('result')
#     lat = results[0].find('geometry').find('location').find('lat').text
#     lng = results[0].find('geometry').find('location').find('lng').text
#     location = results[0].find('formatted_address').text

#     print 'lat',lat,'lng',lng
#     print location
