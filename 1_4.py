a = int(raw_input('Choose number: '))
L = []
for k in range(1, a - 1):
    if a%k == 0:
        L.append(k)
    else:
        continue
print L
