import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print(type(info)) ### dictionary

for item in info:
    print(item)
    print(type(item))
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])

data2 = '''
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

# info = json.loads(data2)
# print('User count:', len(info))

# # for item in info:
# #     print('Name', item['name'])
# #     print('Id', item['id'])
# #     print('Attribute', item['x'])

# print(type(info)) ### list
# print(type(info[0])) ### list of dictionaries