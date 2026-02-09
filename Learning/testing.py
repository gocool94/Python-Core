print("Welcome to python amusement park")

total_amount = 0

while True :
    print("     Menu" \
    "\n 1. Buy Ticket" \
    "\n 2. Total Amount" \
    "\n 3. Exit")
    value = int(input("Enter the input "))
    if value == 1:
        age = int(input("Enter the age: "))
        if age<=5 :
            print("Ticket is free for kids")
            total_amount = 0
        elif age<=12 :
            print("Amount = 120 for age less than 12")
            total_amount = 120
        elif age<=59:
            print("Amount for adult is 200")
            total_amount = 200

        student_check = input("Are you a student yes/no")
        if student_check == 'yes':
            total_amount = total_amount * 0.20
            print("Student discount is checked")
            print(f"Amount after student discount is {total_amount}")
    if value == 2:
        print(f"The total amount is {total_amount}")
    
    if value == 3:
        print("Thank you for using ticketing system")
        break


       print("Invalid input, please try again")
