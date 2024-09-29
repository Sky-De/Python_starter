# # --------------------------------------------------------
# print("First python log")

# name = input("Insert your name: ")
# age = int(input("Insert your age: "))
# print(name + " is " + str(age) + " years old")

# # --------------------------------------------------------
# the_world_is_flat = True
# if the_world_is_flat:
#     print("Be careful not to fall off!")

# # Lists--------------------------------------------------------
# friends = ["Kevin","Max","Sam","Mike","Sky"]

# print(friends[0]) # first element
# print(friends[-1]) # last element
# print(friends[1:]) # index 1 and rest
# print(friends[2:4]) # from index 2 to index 3

# friends[0] = "newF"
# print(friends)

# # Functions used on list----------------------------------------
# listOne = [1,2,3,4,5,9,8,7,6]
# listTwo = ["a","s","z","b","c","d","d","d"]

# listTwo.extend(listOne) # adds two list

# listTwo.append("newItem") # adds new item at the end of list

# listTwo.insert(1,"insertedItem") # adds new item at specified index
# # listTwo.remove(listTwo[1])
# listTwo.remove("insertedItem") # removes item from list

# # listTwo.clear() # removes all item from list
# print(listTwo.pop()) # pop an item from end of list


# print(listTwo.index("a")) # checks item in list
# print(listTwo.count("d")) # counts items in list

# listOne.sort() # sorts lists
# print(listOne) 
# listOne.reverse()
# print(listOne)
# print(listTwo)

# newlistCopy = listOne.copy()
# print(newlistCopy)



# # Tuples--------------------------------------------------------
# # Tuples are immutable / basic diffrence list vs tuples
# cordinate = (4,5)
# cordinates = [(4,5),(14,51),(41,15),(422,35),(24,35)]

# print(cordinate)
# print(cordinate[0])
# print(cordinates)
# print(cordinates[0])

# # cordinate[1] = 10 #we can not change / immutable


# # Functions--------------------------------------------------------

# def my_function(name):
#     print("Hi to You " + name)
    
# my_function("sky")
# my_function("sia")


# def cube_number(number):
#     return number * number * number

# result_of_cube_number_2 = cube_number(2)
# print(cube_number(3))
# print(result_of_cube_number_2)


# If statements --------------------------------------------------------
