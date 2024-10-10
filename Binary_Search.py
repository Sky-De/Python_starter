
# # Binary with While loop

# myList = [1,2,3,4,5,6,7,8,9,10]
# target = 7

# def my_binary_search_while(list,target):
#   low = 0
#   high = len(list) - 1
#   mid = 0
#   while low <= high:
#       mid = (high + low) // 2
#       if list[mid] < target:
#         low = mid + 1   
#       elif list[mid] > target:
#         high = mid - 1   
#       if list[mid] == target:
#        return mid
          
#   return None    
    
# print(my_binary_search_while(myList,target))


# # Binary with recursion
myList = [1,2,3,4,5,6,7,8,9,10]

def my_binary_search_recursive(low,high,list,target):
  if(high >= low):
    mid = (high + low) // 2
    if list[mid] == target:
      return mid
    elif list[mid] > target:
      return my_binary_search_recursive(low, mid - 1 , list, target)
    else:
      return my_binary_search_recursive(mid + 1, high , list, target)
  return None


print(my_binary_search_recursive(0,len(myList) - 1, myList,10))