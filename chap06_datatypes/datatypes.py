#String manipulation
fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	index = index + 1
    print(letter)

##same as the above but more beautiful
for letters in fruit:
    print(letters)

# String Slicing
s = 'Monty Python'
print(s[0:4]) #0 up to not including 4 or 0 to 3. 
print(s[7:]) #7 till the end

#fwoah! The "in" reserved word
if 1 in [2,3,1,5,6]:
    print('Found it')

#String Methods
greet = 'Hello Bob'
greet.lower()
greet.capitalize()

banana = 'banana'
banana.find('na') #return position where it starts
banana.replace('a','A') #'bAnAnA'
banana.startswith('b') # True

#dir provides all function of a datatype
dir(string);
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 
'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#Homework
text = "X-DSPAM-Confidence:    0.8475";

index = 0
for letter in text:
    index = index + 1
    if letter.isnumeric() == True:
        print(float(text[index-1:]))
        break

print(text[text.find('0'):])