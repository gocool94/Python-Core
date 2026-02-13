print("Welcome to the shopping cart..!")
basket = []
total = 0
while True:
    print("" \
    "\n1. Add item" \
    "\n2. Delete item" \
    "\n3. Show basket" \
    "\n4. Purchase item "
    "\n5. Show total bill"
    "\n6. exit"
        )
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to be stored - ")
        basket.append(item)
        print(f"{item} has been added to the list")
    elif choice == 2:
        item = input("Enter the item to be deleted - ")
        basket.remove(item)
        print(f"{item} has been deleted to the list")
    elif choice == 3:
        print("Items remaining are : ")
        for items in basket:
            print(f"\n {items}")
    elif choice == 4:
        print("/n ")
        print(basket)
        purchase_item = int(input("Please provide the index of the list element to purchase"))
        basket.pop(purchase_item)
        purchased_value = int(input("enter the price -- "))
        total = total + purchased_value
    elif choice == 5:
        print(f"Total bill amount is {total}")
    elif choice == 6:
        print("Thanks for using bill basket..!")
        break



    

