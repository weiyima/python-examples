# Tuples are unmodifiable list
y = ['Glenn', 'Sally', 'Joseph']
x = ('Glenn', 'Sally', 'Joseph')
>>> type(y) #<class 'list'> functions: append, count, index, remove, sort
>>> type(x) #<class 'tuple'> functions: count, index | Simple, more memory efficient

#Tuple can exists on left hand side of assignment
(x,y) = (4,'fred')

#Tuples can be used for comparispn. If first item is equal, py goes on to the next
(0,3,3) < (0,2,5)

#Sorting list of tuples
d = {'a':10, 'b':1, 'c':22}
d.items()
sorted(d.items()) # sorted ascending by the keys
>>> [('a', 10), ('b', 1), ('c', 22)]

sortedkey = sorted(d.items()) #sorted in key order
for k,v in sortedkey:
    print(k,v)

######## Sorting VALUE by order

#Step 1: Create a tuple of k,v and a tmp = list()
c = {'a':10, 'b':3, 'c':22}
tmp = list()

#Step 2: Create a reverse (value, key) tuple and assigned to a list
for k,v in c.items():
    tmp.append((v,k))   # [(22, 'c'), (10, 'a'), (3, 'b')] c.items() returns a list of tuples

#Step 3: Sort the list of tuples, descending based on the value 
tmp = sorted(tmp, reverse=True)
print(tmp)

#Step 4: Iterate and only select top X values using a list slice
for val, key in lst[:10]
    print(key, val)


## Even shorter version | "List Comprehension"
sortedvalues = sorted([ (v,k) for k,v in c.items() ], reverse=True)
print(sortedvalues)