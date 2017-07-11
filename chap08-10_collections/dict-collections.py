# Chapter 9 - Collections: Dictionaries

## Simple Example
purse = dict()
purse['money'] = 12 #kv pair
purse['candy'] = 3
purse['tissues'] = 75
print(purse) #they are un-sorted, and mutable just like list, but with a key


## Dictionaries for counting
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

counts.items()
print(counts)
counts.get('csev',-1) #get value of key, else, return default (-1)

#simplified counting with get
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1

print(counts)

#Counting items in a list
counts = dict()
inp = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
sentence = inp.split()
for word in sentence:
    counts[word] = counts.get(word,0) + 1  #standard trick

print(counts)

#Definite loops and Dictionaries

json = {'chuck':1,'fred':42,'jan':100}
for key in json:
    print(key,json[key])

list(json) #returns a list of keys
json.keys() #returns a dict_keys
json.values() #returns a dict_values
json.items() #returns dict_items

for key,value in json.items(): # this is CRAZYYY amazing! 2 iteration variables for key-value
    print(key,value)