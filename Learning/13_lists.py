# ==============================
# PYTHON LISTS — PART 1 (BASICS)
# ==============================

#Fruit shopping list
Fruit_1 = "Apple"
Fruit_2 = "Orange"
Fruit_3 = "Banana"
Fruit_4 = "Grapes"



# 1️⃣ What is a List?
# A list is a collection of multiple items stored in a single variable.
# Lists are ordered, changeable (mutable), and allow duplicate values.


# 2️⃣ Creating a List
fruits = ["Orange", "Banana","Grapes","Apple"]


# Empty list
shopping_bag = []


# 3️⃣ List Can Store Mixed Data Types
mix_datatype = [23,4.5,True,"Virat Kohli"]


# 4️⃣ Accessing List Elements (Indexing)
# Index starts from 0
print(fruits[1])

# Negative indexing (from end)
print(f"The last element is {fruits[-1]}")


# 5️⃣ Slicing Lists
# list[start:end]
new_list = fruits[1:]
print(new_list)


# 6️⃣ Changing List Values (Mutable Nature)
print(fruits)
fruits[1] = "pomo"
print(fruits)


# 7️⃣ List Length
print(len(fruits))

# 8️⃣ Adding Items
#listname.append(item)          # Adds item at end
fruits.append("green apple")
print(fruits)
#listname.insert(index, item)
fruits.insert(2,"pineapple")   
print(fruits)    # Inserts at specific index


# 9️⃣ Removing Items
#list_name.remove(item) 
fruits.remove("pineapple")         # Removes specific value
#list_name.pop()
fruits.pop()                # Removes last item
#list_name.pop(index)  
# 
fruits.pop(2)             # Removes item by index

print(fruits)
# 🔟 Looping Through a List

for each_item in fruits:
    print(each_item)

for i in mix_datatype:
    print(i)



# 1️⃣1️⃣ Checking Item Exists
#using in keyword and if 

if "Apple" in fruits:
    print("Apple is present")

# List will come under python collections more to go..!

