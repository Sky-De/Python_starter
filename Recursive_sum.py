myList = [1,2,3]

def loopSum(arr):
    total = 0
    for i in range(len(arr)):
        total += myList[i]
    
    print(str(total) + " loopSum")    
        
loopSum(myList)

def recursiveSum(arr):
    if arr == []:
        return 0 
    return arr[0] + recursiveSum(arr[1:])
    

print(str(recursiveSum(myList)) + " recursiveSum")
    
    
def recursiveCounter(arr):
    if arr == []:
        return 0
    return 1 + recursiveCounter(arr[1:])

print(str(recursiveCounter(myList))+ " recursiveCounter")