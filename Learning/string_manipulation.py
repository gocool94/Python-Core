# Strings
"""
A set of characters 



"""


name = "Python"
lang = """
tamil,
English,
Telugu,"""

print(name)

#length of the variable
print(len(lang))


text = "Virat kohli"

#inbuilt functions of string

print(text.upper())
print(text.capitalize())
print(text.casefold())
print(text.lower())
print(text.replace("Virat","Akay"))


#Concatenation

gretting = "Hello"

name = input("Enter you name - ")

print(gretting + " " + name + " !")
