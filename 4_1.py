# program is counting pi in different dimentions' cases

import numpy as np
import factorial   # my own module

N = np.zeros (17)
x = np.random.uniform(-1, 1, (10**6, 17)) ** 2

for i in range(0, 10**6):
    for j in range(2, 17):
        if (np.sum (x[i,0:j]) > 1):
            break
        else:
            N[j - 1] = N[j - 1] + 1

f = open('results_4_1.txt', 'w')

for k in range(1, 17):
    Vm = (np.power(np.pi, ((k + 1)/ 2.))) / factorial.gamma(k + 1)
    Vs = np.power(2, k + 1) * (N[k] / 10**6)
    f.write (str (k + 1) + ') ' + str(Vs) + '  ' + str(Vm) + '  ' + str(Vs/Vm) + '  '+ str(N[k]) + '\n')

f.close()
