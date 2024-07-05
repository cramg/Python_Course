# Import Libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking location
url = input('Enter location: ')
print('Retrieving', url)

# Getting XML
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

# Parsing data with ET
tree = ET.fromstring(data)

# Using XPath selector string to look for 'count' tag
counts = tree.findall('.//count')
print('Count:', len(counts))

# Getting sum 
summ = 0
for count in counts:
    summ += int(count.text)

print('Sum:', summ)
