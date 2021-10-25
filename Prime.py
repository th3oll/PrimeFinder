alist = []
check = True
alist.append(0)
while check:
    try:
        maxRange = int(input('Max number to find primes: '))
        check = False
    except:
        print('Type a valid number', '\n')

for i in range(0, maxRange + 1):
    
    for c in alist:
        if c != 0 and c != 1 and (i % c) == 0:
            break
    else:
        if len(alist) % 100 == 0:
            print('List size =',len(alist), '--- Current number =',alist[-1])
        alist.append(i)

alist.pop(0)
alist.pop(0)
alist.pop(0)
alist.pop(2)
myFile = open('primeOutput.txt','w')
myFile.write(str(alist))
