alist = []
check = True
while check:
    try:
        maxRange = int(input('Max number to find primes: '))
        check = False
    except:
        print('Type a valid number', '\n')

for i in range(0, maxRange + 1):

    for c in range(int(len(alist) ** 0.5)): # For every prime number found
        if alist[c] != 0 and alist[c] != 1 and (i % alist[c]) == 0: # Check if the number in question (i) is prime, by 
            break                                                   # dividing it by every other prime number
    else:
        if len(alist) % 100 == 0 and len(alist) != 0:
            print('List size =', len(alist), '--- Current number =', alist[-1]) # Progress update to the user
        if i != 0 and i != 1:
            alist.append(i)


## print(alist)
myFile = open('primeOutput.txt', 'w')
myFile.write(str(alist))
