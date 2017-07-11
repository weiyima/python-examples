# Follow Links in Python
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# count = 4
# position = 3
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

c = 0
while c < count+1:
    print('Retreiving:',url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    url = tags[position-1].get('href',None)
    c = c + 1

# # Retrieve all of the <span> tags
# tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag
#     #print('TAG:', tag)
#     #print('URL:', tag.get('href', None))
#     #print('Contents:', tag.contents[0])
#     #print('Attrs:', tag.attrs)
#     count = count + 1
#     sumtotal = sumtotal + int(tag.contents[0])

# print('Count',count)
# print('Sum',sumtotal)