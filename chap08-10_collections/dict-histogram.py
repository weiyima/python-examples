fname = 'mbox-short.txt'
xfile = open(fname)
di = dict()

for lines in xfile:
    if not lines.startswith('From') : continue
    if not lines.startswith('From:') :
        email = lines.rstrip().split()
        key = email[1]
        di[key] = di.get(key,0) + 1 #get old value or 0 if not seen before


bigvalue = None
bigkey = None

# Find the maximum loop
for key in di:
    if bigkey is None:
        bigkey = key
        bigvalue = di[bigkey] #initiate first key-value pair
    if di[key] > bigvalue:
        bigkey = key
        bigvalue = di[bigkey]

print(bigkey,bigvalue)


# OR using 2 variables
largest = -1
largekey = None
for k,v in di.items():
    if v > largest:
        largest = v
        largekey = di[k[]]

