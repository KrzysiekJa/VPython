# counting sum and mutliplication of series of numbers
k = 0
L = []
while k < 200:
    print ('If you want to stop, write: stop' + '\n')
    a = input('Type a number: ')
    if a == "stop":
        break
    a = int(a)
    L.append(a)
    k += 1

b = 0
c = 1
for i in L:
    b += i
    c *= i
    
print ('Sum and mutliplication :' + '\n' + str(b) + ' ' + str(c))
