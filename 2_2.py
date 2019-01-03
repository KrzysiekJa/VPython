import math
# pi calculating with Laibniz' method

f = open('results_2_2.txt', 'w')
piii = 0.0
L = [t for t in range(1, 2 * 10**7 + 1, 2)]

for i in range(0, len(L)):
    if (i % 2 == 0) :
        x = 1.0 / L[i]
    else:
        x = -(1.0 / L[i])
    piii += 4 * x
    if (i <=99 or i == 999 or i == 9999 or i == 99999 or i == 999999 or i == 9999999):
        z = piii / math.pi
        f.write(str(i + 1) + ') ' + str(piii) + '  ' + str(z) + '\n')

f.close()
