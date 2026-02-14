# ============================================
# Python Dictionary | Core Python in Tamil
# Episode 16
# ============================================


# --------------------------------------------
# 1. What is a Dictionary?
# --------------------------------------------
# Dictionary stores data as key : value pairs
# Example: name -> "Arun", age -> 25

Alphabet = {'A':'Apple', 'B':'Ball','C':'Cat'}


# --------------------------------------------
# 2. Creating a Dictionary
# --------------------------------------------
student = {
    "name": "Arun",
    "age": 21,
    "course": "Python"
}   


# --------------------------------------------
# 3. Accessing Values using Keys
# --------------------------------------------
# dict[key]
print(student["age"])



# --------------------------------------------
# 4. Using get() Method (Safe Access)
# --------------------------------------------
# If key not found, it returns None instead of error
print(student.get("name"))



# --------------------------------------------
# 5. Adding New Key-Value Pair
# --------------------------------------------
student["additionals"] = 'Java'
print(student)


# --------------------------------------------
# 6. Updating Existing Value
# --------------------------------------------

student["additionals"] = 'Javascript'
print(student)


# --------------------------------------------
# 7. Removing Items from Dictionary
# --------------------------------------------
# pop() - removes specific key
# dict.pop("city")
#student.pop("additionals")

# popitem() - removes last inserted item
# dict.popitem()
"""student.popitem()
print(student)"""
# del keyword
# del dict["value"]

del student['additionals']
print(student)

# --------------------------------------------
# 8. Dictionary Methods
# --------------------------------------------
# keys()   - returns all keys
# values() - returns all values
# items()  - returns key-value pairs

print(student.keys())
print(student.values())
print(student.items())


# --------------------------------------------
# 9. Looping through Dictionary
# --------------------------------------------
# using key
for i in student.keys():
    print(student[i])

# Using items()
for keys , values in student.items():
    print(f"{keys} value is {values}")



# --------------------------------------------
# 10. Checking Key Exists
# --------------------------------------------
if 'name' in student:
    print("name exist")


# --------------------------------------------
# 11. Dictionary Length
# --------------------------------------------
#len()
print(len(student))

# --------------------------------------------
# 12. Clearing Dictionary
# --------------------------------------------
#.clear()
student.clear()

print(student)


# --------------------------------------------
# 13. Real-Life Example
# --------------------------------------------
user_profile = {
    "username": "tech_tamizhan",
    "email": "tech@example.com",
    "password":123,
    "is_active": True
}

username_input = input('Enter the username--')
password_input = int(input("Enter the password---"))

if username_input == user_profile.get("username") and password_input == user_profile.get("password"):
    print("Access granted")
else:
    print("Access denied..!")


# --------------------------------------------
# End of Dictionary Basics
# Next: Dictionary Mini Project & Problems
# --------------------------------------------
