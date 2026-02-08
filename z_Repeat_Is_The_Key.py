# factorial + recursive sum

# recursion
def factorial_rec(x):
    if x == 1:
        return 1
    else:
        return x * factorial_rec(x-1)
    
# loop

def factorial_loop(x):
    fact = 1
    for i in range(1, x+1):
        fact = fact * i
    return fact    

print(factorial_rec(5))    
print(factorial_loop(5))    
    




# binarySearch + selection sort + quick sort

myList = [1,2,3,4,5,6,7,8,9,10]
target_number = 9

myList1 = [5,6,33,2,3,1,9,11,10,4,7,8]