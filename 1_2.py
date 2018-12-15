# even/odd number

k = 0
while k < 200:
    print ('If you want to stop write: stop')
    a = input('Type a number: ')
    if a == "stop":
        break
    a = int(a)
    if a < 0:
        break
    if a%2 == 0:
        print (str(a) + ' is even')
    else:
        print (str(a) + ' is odd')
