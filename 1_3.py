# program making operations on lists

def func(L1, L2, x):
    if (len(L1) != len(L2)):
        exit
    if ((set([x]) & set(["*", "+", "-", "/"])) == 0):
        exit
    L = [] 
    if x == "+": # choosing operations
        L = [L1[i] + L2[i] for i in range(len(L1))]
    if x == "-":
        L = [L1[i] - L2[i] for i in range(len(L1))]
    if x == "*":
        L = [L1[i] * L2[i] for i in range(len(L1))]
    if x == "/":
        L = [L1[i] / L2[i] for i in range(len(L1))]
    else:
        exit
    return L
    """switcher = {
        "+": for i in len(L1):
                 L[i] = L1[i] + L2[i],
        "-": for i in range(L1):
                 L[i] = L1[i] - L2[i],
        "*":  for i in range(L1):
                 L[i] = L1[i] * L2[i],
        "/": for i in range(L1):
                 L[i] = L1[i] / L2[i],
        }
        return switcher.get(x, "nothing")
    no sense
    """

a = [3, 4, 8]
b = [5, 9, 3]
f = func
print (f(a, b, '-'), '\n')
print (f(a, b, '*'), '\n')
