# binarySearch + selection sort

myList = [1,2,3,4,5,6,7,8,9,10]
target_number = 9

myList1 = [5,6,33,2,3,1,9,11,10,4,7,8]

def binary_search_recurssive(low,high,arr,target):
    if high >= low:
        mid = (high + low) // 2
        mid_item = arr[mid]
        if mid_item == target:
            return mid
        elif mid_item > target:
            return binary_search_recurssive(low,mid-1,arr,target)
        elif mid_item < target:
            return binary_search_recurssive(mid+1,high,arr,target)
    return None

def binary_search_while(arr,target):
    low = 0
    mid = 0
    high = len(arr) -1
    while high >= low:
        mid = (high + low) // 2
        mid_item = arr[mid]
        if mid_item == target:
            return mid
        elif mid_item < target:
            low = mid + 1
        elif mid_item > target:
            high = mid -1
    return None


def selection_sort(arr):
    for i in range(0,len(arr)):
        index_of_min = i
        for j in range(i+1,len(arr)):
            if arr[index_of_min] > arr[j]:
                index_of_min = j
                if index_of_min !=i:
                    arr[index_of_min],arr[i] = arr[i],arr[index_of_min]
    return arr

print(binary_search_while(myList,target_number))
print(binary_search_recurssive(0,len(myList)-1,myList,target_number))
print(selection_sort(myList1))