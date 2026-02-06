#ATM machine

attempt = 3
password = "123"

while(attempt!=0):
    password_input = input("Enter your password ")
    if password != password_input:
        attempt = attempt - 1
        print(f"Wrong password & you still have {attempt} attempts left")
    elif password == password_input:
        print(f"Login successful.!")
        break