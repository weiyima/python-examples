import json
import urllib.request, urllib.parse, urllib.error


data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''


while True:
  address = input('Enter location: ')
  if len(address) < 1: break
  # address = ' http://py4e-data.dr-chuck.net/comments_42.json'
  print('Retrieving', address)

  uh = urllib.request.urlopen(address)
  data = uh.read()

  print('Retrieved', len(data), 'characters')

  # print(data.decode())
  # print('==================== raw JSON above =============')

  js = json.loads(data)
  # print(json.dumps(js, indent=2))

  count = 0
  sumtotal = 0

  for item in js["comments"]:
      # print('Name', item["name"])
      sumtotal = sumtotal + int(item['count'])
      count = count + 1

  print('Count',count)
  print('Sum',sumtotal)


# for u in js['users']:
#     print(u['screen_name'])
#     if 'status' not in u:
#         print('   * No status found')
#         continue
#     s = u['status']['text']
#     print('  ', s[:50])