import numpy as np

# dla l. parzystych generuje silnie z liczby podzilonej przez 2 (np. (10/2)! )
# dla l. nparz. liczy silnie ulamkow (np. (2/3)! )

def gamma (x):
    if (x == 0):
        return 1
    if (x == 1):
        return np.sqrt(np.pi) / 2
    elif (x%2 == 0):
         return x / 2 * gamma (x - 2)
    else:
         return x / 2. * gamma (x - 2)
