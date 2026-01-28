# ==================================
# CONDITIONAL STATEMENTS - PART 1
# ==================================

# Why do we need conditions?
# Real-life decision making

# ==================================
# CONDITIONAL (COMPARISON) OPERATORS
# ==================================

# Datatype - Boolean
#True 
#False 

# Equal to (==)
# Not equal to (!=)
# Greater than (>)
# Less than (<)
# Greater than or equal to (>=)
# Less than or equal to (<=)
a = 10
b = 20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)   
print(a>=b)
print(a<=b)
# ==================================
# BOOLEAN VALUES
# ==================================

# True and False
# Result of comparison operators

# ==================================
# BASIC IF STATEMENT
# ==================================

# if syntax
# Colon and indentation
age = 9
if(age>18):
    print("You are eligible to vote")
    print("You can vote")
    print("Vote for a change.!")

# ==================================
# IF ELSE STATEMENT
# ==================================

# if block execution
# else block execution
# Flow of control

#age = int(input("Enter you age to check vote eligibility - "))
if(age>18):
    print("You are eligible to vote")
else:
    print("you are not eligible to vote.!")

#Word reverse 
# how to check if a word is palindrome or not
language = input("Enter the String to check palindrome..")
if(language == language[::-1]):
    print(f"String {language} is a palindrome")
    print("String is palindrome")
else:
    print(f"String {language} is not a palindrome")
    print("String is not a palindrome")

# ==================================
# INPUT WITH IF ELSE
# ==================================

# Getting user input
# Type conversion
# Decision based on input

# ==================================
# COMMON BEGINNER MISTAKES
# ==================================

# Using = instead of ==
# Missing colon (:)
# Indentation errors
# Forgetting type casting

# ==================================
# MINI CHALLENGE
# ==================================

# Electricity Bill Alert System
# Problem explanation

unit = int(input("Enter you units "))
if(unit>=1000):
    print("You have higher units, Charges may differ with lower rates")
