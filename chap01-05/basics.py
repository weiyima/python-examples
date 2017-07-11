#comments in python
print('Hello World');

#Type
sval = '123'
ival = int(sval)
print(ival)

#User Input
inp = input('Europe floor? ')
usf = int(inp)+1
print('US floor', usf)

#Type and User Input
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = float(hrs) * float(rate)
print("Pay:",pay)

#Simple if-else and functions()
x = 4
def size(x):
    if x < 2 :
        print('Smaller')
    elif x < 10 :
        print('Medium')
    else :
        print('Large')
size(x)

#try-except and technique to hit an error message (traceback)
astr = input('Enter a number')
try:
    istr = int(astr)
except:
    istr = -1

if istr > 0 :
    print('Nice work!')
else : 
    print('Not a number')
print(istr)

score = input("Enter Score: ")

#def functions
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('es'),'Sarah');

def addtwo(a,b):
    added = a + b
    return added

print(addtwo(1,4));

#Loops and Iteration
friends = [1,2,3]
def looper():
    for i in friends:
        print(i)

looper()
