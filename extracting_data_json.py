import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Asking location
url = input('Enter location: ')
print('Retrieving', url)

# Getting JSON
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

# Parse data with JSON
info = json.loads(data)

# Getting sum
count = 0
summ = 0

for uu in info['comments']:
    summ += uu['count']
    count += 1

# Printing sum
print('Count:', count)
print('Sum:', summ)
