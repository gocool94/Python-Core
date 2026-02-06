#factorial of a number

"""num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial:", fact)"""

    




#factorial of a number

num = 5 
#5! 5 * 4 * 3 * 2 * 1
i = 1
fac = 1
while(i<=num):
    fac = fac * i
    print(fac)
    i = i + 1 #End condition -> infinite loop
print(f"factorial is {fac}")



#ATM machine

attempt = 3
password = 123

while(attempt!=0):
    pass_word = int(input("Enter your password "))
    if pass_word != password:
        attempt = attempt - 1
        print("Password incorrect, Please retry.")
        print(f"You Still have {attempt} only")
    elif pass_word == password:
        print(f"Successfully logged in")
        break

