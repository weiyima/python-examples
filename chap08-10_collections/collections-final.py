fname = 'mbox-short.txt'
xfile = open(fname)
x = list()
tmp = list()
d = dict()

for lines in xfile:
    if not lines.startswith("From") : continue
    if lines.startswith("From:") : continue
    x = lines.rstrip().split()
    hour = (x[5])[:2]
    d[hour] = d.get(hour,0) + 1

for k,v in d.items():
    tmp.append((k,v))

tmp = sorted(tmp)

for k,v in tmp:
    print(k,v)




