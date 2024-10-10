# binarySearch

myList = [1,2,3,4,5,6,7,8,9,10]

def bs(list,target):
    low = 0
    mid = 0
    high = len(list) - 1
    while low <= high:
        mid = (high + low)  // 2
        mid_item = list[mid]
        if mid_item == target:
            return mid
        elif mid_item < target:
            low = mid + 1
        elif target < mid_item:
            high = mid -1
    return None

print(bs(myList,9))


