# Factorail

# recursion
def rec_factorial(x):
    if x == 1:
        return 1
    else:
        return x * rec_factorial(x-1)

# loop
def factorial(x):
    fact = 1
    for i in range(1, x+1 ):
        fact = fact * i
    return fact

print(rec_factorial(5))
print(factorial(5))