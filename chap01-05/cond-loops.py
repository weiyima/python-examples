
# for loops to find largest number
numberlist = [3,4,15,21,74]
largest_so_far = -1
print('Before',largest_so_far)

for the_num in numberlist:
    if the_num > largest_so_far:
        largest_so_far = the_num
        print(largest_so_far, the_num)

print('After',largest_so_far)


# Creating counters, increment, within for loops
count = 0
sumtotal = 0

for item in [9,41,12,3,74,15]:
    count = count + 1
    sumtotal = sumtotal + item
    print('After',count, sumtotal)

# Boolean Search
numlist = [9,41,12,3,74,15]
count = 0
found = False

for value in numlist:
    count = count + 1
    print(value)
    if value == 3:
        found = True
        break

print(numlist[count-1],found)

# Search for smallest value & the "None" value type as Flag

numberlist = [3,4,15,21,74]
smallest = None

for value in numberlist:
    if smallest is None: #nifty trick for "first time" priming
        smallest = value
    elif value < smallest:
        smallest = value

print(smallest)