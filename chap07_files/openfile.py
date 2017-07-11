
## Opening a file | file handler | try except pattern
filename = input('Enter file name: ')
try:
    fh = open(filename)
    for line in fh:
        print(line.upper().rstrip())
except:
    print('Error! File cannot be opened.')
    quit()


#fname = 'mbox-short.txt'
fname = input('Enter file name: ')
fh = open(fname)

count = 0
value = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue  # useful to "skip" if no match
    count = count + 1
    pos = line.find(':')
    value = value + float(line[pos+2:].rstrip())

print('Average spam confidence:',value/count)


#### open's a specified file | create a file handler | 
#### for loop to count lines, technique to "skip" using continue keyword
#### find a pattern, sums value and print average