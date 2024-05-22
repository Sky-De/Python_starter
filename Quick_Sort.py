myList = [2,1,4,8,3,9,5,7,6]

def QuickSort(arr):
   if len(arr) < 2:
       return arr
   else:
       pivot = arr[0]
       less = [i for i in arr[1:] if i <= pivot]
       greater = [i for i in arr[1:] if i > pivot]
       return QuickSort(less) + [pivot] + QuickSort(greater)

print(QuickSort(myList))