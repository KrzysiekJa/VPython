import math
import random
# pi calculating with spheral method

S_s = 4.0
N_r = 0.0
S_r = math.pi

f = open('results_2_1.txt', 'w')

for i in range(1, 10**6 + 1):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <= 1):
        N_r += 1
        S_r  = S_s * (N_r / i)
    if (i <= 100 or i == 10**3 or i == 10**4 or i == 10**5 or i == 10**6):
        z = S_r / math.pi
        f.write(str(i) + ') ' + str(S_r) + '  ' + str(z) + '\n')

f.close()
