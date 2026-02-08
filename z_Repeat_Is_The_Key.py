# factorial----------------------------------------------- 

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
    
# sum ----------------------------------------------------------

sumList = [1,2,3]
#loop
def loop_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

print(loop_sum(sumList))

#recursion
def rec_sum(arr):
    if arr == []:
        return 0
    return arr[0] + rec_sum(arr[1:])

print(rec_sum(sumList))


# binarySearch + selection sort + quick sort
