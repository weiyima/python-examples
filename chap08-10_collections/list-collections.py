## Chapter 8 Assignment

# fname = input('Enter file name: ')
fname = 'romeo.txt'
xfile = open(fname)
poem = []
for line in xfile:
    sentence = line.rstrip().split()
    for word in sentence:
        if word not in poem : 
            poem.append(word)

poem.sort()
print(poem)

#Get all email address from mbox-short.txt
# fname = input('Enter file name: ')
fname = "mbox-short.txt"
xfile = open(fname)
count=0

for line in xfile:
    if not line.startswith("From") : continue
    if not line.startswith("From:") :
        sentence = line.rstrip().split()
        if len(sentence) < 1 : continue #guardian pattern
        print(sentence[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")

