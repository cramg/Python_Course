import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create variables
url = input('Enter URL:')
scount = input('Enter count:')
count = int(scount)
spos = input('Enter position:')
pos = int(spos)

#First retrieve
print('Retrieving:', url)

# Loop

for uu in range(count):
    # Parse link
    links = []
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))

    url = links[pos-1]
    print('Retrieving:', links[pos-1])
