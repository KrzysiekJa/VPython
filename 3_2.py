import time
import random
# a simulation of random choice by random funtion with use of terminal

print("|" + ' ' * 13 + "START"+ ' ' * 12 + "|")

i = 0
k = 0

while (i > -15 and i < 15):
    time.sleep(0.05)
    j = random.choice([-1, 1])
    print("|" + ' ' * (14 + i) + "*" + str(i) + ' ' * (14 - i) + "|")
    i = i + j
    k = k + 1
    
    
print("|" + ' ' * (14 + i) + "*" + str(i) + ' ' * (14 - i) + "|" + "\n")
print('We flip ' + str(k) + ' times cloin :)' + '\n')
