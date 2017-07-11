

## Combinining techniques
# is None for initiating | try-except | while True but break, continue
largest = None
smallest = None

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        print('Maximum is', largest)
        print('Minimum is', smallest)
        break
    try:
        fval = int(sval)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = fval
        largest = fval
    elif smallest > fval:
        largest = smallest
        smallest = fval
    else:
        largest = fval
num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except: 
        print('Invalid input')
        continue
    num = num + 1
    tot = tot + fval

print(tot,num,tot/num)

