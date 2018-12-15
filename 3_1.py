import numpy as np
# making a plot of sinus function

x = np.array([i * 2 * np.pi / 50 for i in range(0, 51)])
y = np.sin(x) * 50
y = np.int_(y)

f = open('results_3_1.txt', 'w')
print(y)
for i in y:
    if i == 0:
        f.write ("0" + '\n')
    elif i > 0:
        f.write ("+" * i + '\n')
    else:
        f.write ("-" * np.abs(i) + '\n')

f.close()
