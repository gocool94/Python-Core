#determine the largest of two numbers

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

if (num1 == num2):
    print("Both the numbers are equal")
elif(num1 > num2):
    print(f"{num1} is the greatest number")
else:
    print(f"{num2} is the greatest number")