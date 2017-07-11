#Chapter 8 - List

friends = ['Joseph',0.99,'Hello','World']
friends[1] = 'Sally' #list are mutable, list are not
#print(friends)

#range(int) used to create range/list of size int (e.g. range(4) will be [0,1,2,3])
for i in range(len(friends)):
    friend = friends[i]
    print(friend)

#list functions 
friends[3:] #slicing - from 3 not including

stuff = [] #create empty list
stuff.append('Book')
stuff.append('Umbrella') #unlike string, list are mutable
stuff.append('Apple')
'Book' in stuff #search and compare. returns True/False
stuff.sort() #['Apple', 'Book', 'Umbrella']

#Simple list Data Structures
numlist = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done' :
        print('Done!')
        break
    try :
        fval = float(inp)
        numlist.append(fval)
    except :
        print('Not a valid number')

print('Total sum is:',sum(numlist))
print('Average is',sum(numlist)/len(numlist))

#  Strings and List working together, using split
whitespace = 'The big brown fox jumps over the log'
listws = whitespace.split()
print(list1)
csv = 'The,big,brown,fox,jumps,over,the,log'
listcsv = csv.split(',')
print(listcsv)

# Chapter 8 - Homework
