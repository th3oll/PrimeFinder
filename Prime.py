primeNums = []
invalidInput = True
primeNums.append(0)
while invalidInput:
    try:
        maxRange = int(input('Max number to find primes: '))
        invalidInput = False
    except:
        print('Type a valid number', '\n')

for i in range(0, maxRange + 1):
    
    for c in primeNums: # For every prime number found
        if c != 0 and c != 1 and (i % c) == 0: # Check if the number in question (i) is prime, by 
            break                              # dividing it by every other prime number
    else:                                      # TODO: Optimize this by checking only the sqrt(primeNums)
        if len(primeNums) % 100 == 0:
            print('List size =',len(primeNums), '--- Current number =',primeNums[-1]) # Progress update to the user
        primeNums.append(i)

primeNums.pop(0)
primeNums.pop(0)
primeNums.pop(0)
primeNums.pop(2)

myFile = open('primeOutput.txt','w')
myFile.write(str(primeNums))
