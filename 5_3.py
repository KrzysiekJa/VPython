import operator, functools
# bithday paradox with different amount of people cases

k = 365

for i in range (2, 367):
    # with use of special equation from https://en.wikipedia.org/wiki/Birthday_problem#Calculating_the_probability
    # prob_different = series of multiplication of all elements from list comprehension
    prob_different = functools.reduce (operator.mul, [1 - (j / k) for j in range (0,i)])
    
    print (i, " ",  1 - prob_different)
