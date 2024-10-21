# binarySearch

myList = [1,2,3,4,5,6,7,8,9,10]
target_number = 9

# def bs(list,target):
#     low = 0
#     mid = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (high + low)  // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif target < mid_item:
#             high = mid -1
#     return None

# print(bs(myList,target_number))


# def myBs(list,target):
#     low = 0
#     mid = 0
#     high = len(list) -1
    
#     while low <= high:
#         mid = (high + low) // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif mid_item > target:
#             high = mid - 1
#     return None

# print(myBs(myList,target_number))



# def the_bs(list,target):
#     low = 0 
#     high = len(list) -1
#     mid = 0
#     while low <= high:
#         mid = (high + low) // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif mid_item > target:
#             high = mid -1
#     return None

# print(the_bs(myList,target_number))

# def myBs(list,target):
#     low = 0
#     mid = 0
#     high = len(list) -1
    
#     while low <= high:
#         mid = (high + low) // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif mid_item > target:
#             high = mid -1
#     return None

# print(myBs(myList,target_number))


# def binaryS(list,target):
#     low = 0
#     mid = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (high + low) // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif mid_item > target:
#             high = mid - 1
#     return None


# print(binaryS(myList,target_number))


# def bs(list,target):
#     low = 0
#     mid = 0
#     high = len(list) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
#         mid_item = list[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item > target:
#             high = mid - 1
#         elif mid_item < target:
#             low = mid + 1
#     return None

# print(bs(myList,target_number))



# def myBs(arr,target):
#     low = 0
#     mid = 0
#     high = len(arr) -1
#     while low <= high:
#         mid = (high + low ) // 2
#         midItem = arr[mid]
#         if midItem == target:
#             return mid
#         elif midItem < target:
#             low = mid + 1
#         elif midItem > target:
#             high = mid -1
#     return None

# print(myBs(myList,target_number))
        
        
# def bsR(low,high,arr,target):
#     if high >= low:
#         mid = (high + low ) // 2
#         mid_item = arr[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             return bsR(mid + 1, high,arr,target)
#         elif mid_item > target:
#             return bsR(low,mid -1,arr,target)
#     return None

# print(bsR(0,len(myList) -1,myList,target_number))

# def bsW(arr,target):
#     low = 0
#     mid = 0
#     high = len(arr) - 1
#     while (high >= low):
#         mid = ( high + low ) // 2
#         mid_item = arr[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item > target:
#             high = mid -1
#         elif mid_item < target:
#             low = mid + 1
#     return None

# print(bsW(myList,target_number))

# def bsR(low,high,arr,target):
#     if high >= low:
#         mid = (high + low) // 2
#         mid_item = arr[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item > target:
#             return bsR(low,mid -1,arr,target)
#         elif mid_item < target:
#             return bsR(mid +1 , high,arr,target)
#     return None
# print(bsR(0,len(myList) - 1,myList,target_number))


# def myBsW(arr,target):
#     low = 0
#     mid = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         mid_item = arr[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             low = mid + 1
#         elif mid_item > target:
#             high = mid - 1
#     return None

# def myBsR(low,high,arr,target):
#     if low <= high:
#         mid = (low + high)
#         mid_item = arr[mid]
#         if mid_item == target:
#             return mid
#         elif mid_item < target:
#             return myBsR(mid + 1,high,arr,target)
#         elif mid_item > target:
#             return myBsR(low,mid - 1,arr,target)
        
#     return None


# print(myBsW(myList,target_number))
# print(myBsR(0,len(myList)-1,myList,target_number))

def bs(arr,target):
    low = 0
    mid = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low ) // 2
        mid_item = arr[mid]
        if mid_item == target:
            return mid
        elif mid_item < target:
            low = mid + 1
        elif mid_item > target: 
            high = mid - 1
    return None

print(bs(myList,target_number))