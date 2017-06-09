from __future__ import print_function, division
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

print("Retrieving: {}".format(url))

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')

for i in range(count):
	for j, tag in enumerate(tags):
		if j == pos - 1:
			url = tag.get('href', None)
			print("Retrieving: {}".format(url))

			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)					    
			tags = soup('a')

