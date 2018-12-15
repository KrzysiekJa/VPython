# program is finding all numbers, less than one hundred, that require Pithagoras equation : a^2 + b^2 = c^2 -> big Fermat's thesis

for i in range (1, 100):
    for j in range (1, i):
        for k in range (i + 1, i + j):
            a = i * i
            b = j * j
            c = k * k
            if (a + b == c):
                print(str(j) + '^2 ' + '+ ' + str(i) + '^2 ' + '= ' + str(k) + '^2' + '\n')
            a = a * i
            b = b * j
            c = c * k
            if (a + b == c):
                print(str(j) + '^3 ' + '+ ' + str(i) + '^3 ' + '= ' + str(k) + '^3' + '\n')
            a *= i
            b *= j
            c *= k    
            if (a + b == c):
                print(str(j) + '^4 ' + '+ ' + str(i) + '^4 ' + '= ' + str(k) + '^4' + '\n')
            a *= i
            b *= j
            c *= k    
            if (a + b == c):
                print(str(j) + '^5 ' + '+ ' + str(i) + '^5 ' + '= ' + str(k) + '^5' + '\n')
            a *= i
            b *= j
            c *= k    
            if (a + b == c):
                print(str(j) + '^6 ' + '+ ' + str(i) + '^6 ' + '= ' + str(k) + '^6' + '\n')
