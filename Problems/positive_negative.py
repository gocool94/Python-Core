#check if a number is positive negative or zero

num = int(input("Enter a number "))

if (num == 0):
    print("The given number is zero")
elif(num < 0):
    print("The number is negative")
else:
    print("The number is positive")