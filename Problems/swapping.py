#problem num 9 - swapping of two numbers

a = int(input("Enter a number "))
b = int(input("Enter b number "))

print(f"Before swapping a value is {a} and b value is {b}")

temp = a
a = b
b = temp

print(f"After swapping a value is {a} and b value is {b}")
