# Regular Expressions

""" 
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

Examples:

[0-9] one digit
[0-9]+ one more more digit (because of + sign)
'\S+@\S+' = regex for email
^From (\S+@\S+) = extract email pattern only if regex matches ^From

re.search('[0-9]+') # returns True / False depending on whether the string matches the regex
re.findall('[0-9]+') # returned the matching string to be extracted 

""" #

import re

fname = 'regex_sum_6035'
xfile = open(fname)
lst = list()
sumtotal = 0
count = 0

for line in xfile:
    line = line.rstrip()
    lst = re.findall('[0-9]+',line)
    for l in lst:
        sumtotal = sumtotal + int(l)
        count = count + 1

print('Final',sumtotal)
print('Count',count)
