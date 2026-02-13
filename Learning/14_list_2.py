# ================================
# Python List - Important Methods
# ================================

# --------------------------------
# extend() - another list-oda values add pannum
# --------------------------------


fruits = ["Orange","Apple","guava"]
more_fruits = ["grape", "papaya"]
fruits.extend(more_fruits)
print(fruits)
print(fruits.index("papaya"))

# index() 
#pos = list.index("apple")   # position
# --------------------------------

# count() - count of value?

fruits.append("Apple")
print(fruits.count("Apple"))
# --------------------------------
# sort() 
# --------------------------------


#list.sort()            # small to big
#list.sort(reverse=True)  # big to small
fruits.sort(reverse=True)
print(fruits)
# --------------------------------

# reverse()
#list.reverse()


# --------------------------------
# copy() 
# --------------------------------
#numbers_copy = numbers.copy()  # safe copy
#numbers_copy.append(100)

fruits_copy = fruits.copy()
fruits_copy.append("peach")
print(fruits_copy)

# --------------------------------
# clear()
# --------------------------------

fruits_copy.clear()
print(fruits_copy)
#numbers.clear()


