
# # selection_sort with While loop

myList = [5,6,33,2,3,1,9,11,10,4,7,8]


def selection_sort(arr):
  for i in range(0,len(arr)):
    indexOfMin = i
    for j in range(i+1,len(arr)):
      if arr[indexOfMin] > arr[j]:
        indexOfMin = j
      if(indexOfMin != i):
        arr[i],arr[indexOfMin] = arr[indexOfMin], arr[i]
  return arr

sortedList = selection_sort(myList)

print(sortedList)