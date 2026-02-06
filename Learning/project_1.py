print("\n ***********************Welcome to Amusement park Ticketing system..!***************")

total_amount = 0

while True:
    # 1. Buy Tickets
    print("\n Menu" \
    "\n 1. Buy Tickets" \
    "\n 2. Show total amount" \
    "\n 3. Exit ")
    choice = input("Enter your choice - ")
    if choice == '1':
        age = int(input("Enter your age - "))
        if age <= 5:
            total_amount = 0
            print("Kids ku kaasu ila..!")
        elif age <= 12:
            total_amount = 120
            print("Kinder kids ku 120 rupees ")
        elif age <= 59:
            total_amount = 200
            print("Adults ku 200 rupees")
        else:
            total_amount = 100
            print("Grand parents ku senior concession 100 rupees")
        
        is_student = input("Are you a Student yes/no  ")
        if is_student == 'yes':
            discount = total_amount * 0.20
            total_amount = total_amount - discount
            print("Student discount applied..!")
        
    # 2. Total Amount
    
    if choice == '2':
        print(f"Your total amount is {total_amount}")

    # 3. Exit

    if choice == '3':
        print("Thank you for using our ticketing system..")
        break