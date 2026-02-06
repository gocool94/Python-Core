print("🎡 Welcome to Python Amusement Park")

total_amount = 0

while True:
    print("\n===== MENU =====")
    print("1. Buy Ticket")
    print("2. Show Total Amount")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # 👉 BUY TICKET
    if choice == "1":
        age = int(input("Enter age: "))
        student = input("Are you a student? (yes/no): ")

        # Base price by age
        if age < 5:
            price = 0
            print("Free Ticket 🎉")

        elif age <= 12:
            price = 100

        elif age <= 59:
            price = 200

        else:
            price = 120

        # 🎓 Student Discount Logic
        if student.lower() == "yes" and price > 0:
            discount = price * 0.20   # 20% discount
            price = price - discount
            print("Student Discount Applied 🎓")

        total_amount += price
        print("Ticket Price:", price)

    # 👉 SHOW TOTAL
    elif choice == "2":
        print("Total Amount so far:", total_amount)

    # 👉 EXIT SYSTEM
    elif choice == "3":
        print("Thank you! Enjoy your ride 😎")
        break

    else:
        print("Invalid Choice ❌")
