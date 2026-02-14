# ============================================
# COLLECTION COMPREHENSION IN PYTHON
# ============================================

# --------------------------------------------
# 1️⃣ WHAT IS COLLECTION COMPREHENSION?
# --------------------------------------------
# Short & smart way to create collections
# Write loops in a single line
# Cleaner and professional Python style
list_1 = []
for i in range(6):
    list_1.append(i)
print(list_1)

list_2 = [i for i in range(6)]
print(list_2)


# --------------------------------------------
# 2️⃣ WHY USE COMPREHENSION?
# --------------------------------------------
# Reduces number of lines
# Improves readability
# Interview favourite concept
# Used in real-world Python projects


# --------------------------------------------
# 3️⃣ LIST COMPREHENSION – BASIC SYNTAX
# --------------------------------------------
# Syntax:
# [expression for item in iterable]

# --------------------------------------------
# 4️⃣ LIST COMPREHENSION WITH CONDITION
# --------------------------------------------
# Syntax:
# [expression for item in iterable if condition]
even = []
for i in range(0,10):
    if (i%2 ==0):
        even.append(i)
print(even)

even_1 = [i for i in range(0,10) if(i%2==0)]

# --------------------------------------------
# 5️⃣ SET COMPREHENSION
# --------------------------------------------
# Removes duplicates automatically
# Syntax:
# {expression for item in iterable}
numbers = [1, 2, 2, 3, 4, 4, 5]

pure_number = {i for i in numbers}
print(pure_number)



# --------------------------------------------
# 6️⃣ DICTIONARY COMPREHENSION
# --------------------------------------------
# Creates key-value pairs dynamically
# Syntax:
# {key: value for item in iterable}
students_score = {"Ram":50,"Virat":30,"Dhoni":66}
grade = {item: "pass" for item in students_score if students_score[item] > 30}
print(grade)



# --------------------------------------------
# 7️⃣ DICTIONARY COMPREHENSION WITH CONDITION
# --------------------------------------------
# Filter dictionary based on condition
# Useful for marks, results, permissions, etc.


# --------------------------------------------
# 8️⃣ GENERATOR EXPRESSION (TUPLE-LIKE)
# --------------------------------------------
# Tuple comprehension does NOT exist
# Uses round brackets ()
# Generates values one by one (memory efficient)
tuple_gene = (i for i in range(0,10))
print(tuple_gene)



# --------------------------------------------
# 9️⃣ REAL-LIFE USE CASES
# --------------------------------------------
# Filtering pass students
# Creating even/odd lists
# Removing duplicates
# Transforming data


# --------------------------------------------
# 🔟 COMMON BEGINNER MISTAKES
# --------------------------------------------
# Missing brackets
# Over-complicating logic
# Using comprehension where normal loop is clearer


# --------------------------------------------
# 1️⃣1️⃣ WHEN TO USE & WHEN TO AVOID
# --------------------------------------------
# Use for simple logic
# Avoid for complex nested conditions


# --------------------------------------------
# 1️⃣2️⃣ MINI CHALLENGES 🎯
# --------------------------------------------
# Create a list of squares from 1 to 10
# Extract even numbers using comprehension
# Create a dictionary of students and pass/fail
# Remove duplicates using set comprehension
