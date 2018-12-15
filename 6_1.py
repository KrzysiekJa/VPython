import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use ('classic')

# generator of fractal : Barnsley fern

x = np.zeros( 10 ** 6)
y = np.zeros( 10 ** 6)

Z = np.random.randint (101, size = 10**6)

for i in range (1, 10**6):
    if (0 < Z[i] <= 85):
        x[i] = 0.85 * x[i - 1] + 0.04 * y[i - 1]
        y[i] = -0.04 * x[i - 1] + 0.85 * y[i - 1] + 1.6
        continue
    if (85 < Z[i] <= 92):
        x[i] = 0.2 * x[i - 1] - 0.26 * y[i - 1]
        y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
        continue
    if (92 < Z[i] <= 99):
        x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
        y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44
        continue
    if Z[i] == 100:
        x[i] = 0
        y[i] = 0.16 * y[i - 1]
        continue


plt.plot ( x, y, 'b,', zorder = 1)
ax = plt.gca ()
ax.set_facecolor('black')

plt.show ()
