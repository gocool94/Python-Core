    
print("Welcome to Bill basket..!")

Total_amount = 0
basket = []

while True:
    print("" \
        "\n1. Add item" \
        "\n2. Delete item" \
        "\n3. Show basket" \
        "\n4. Purchase item "
        "\n5. Show total bill"
        "\n6. exit"
            )
    choice = int(input("Enter your choice -- "))
    
    if choice == 1:
        item = input("Enter the item -- ")
        basket.append(item)
        print(f"{item} has been added..!")
        print("-------------")
    elif choice == 2:
        print(basket)
        item = input("Enter the item to be deleted -- ")
        basket.remove(item)
        print(f"{item} has been deleted..!")
        print("-------------")
    elif choice == 3:
        print(f"The basket has {basket}")
    elif choice == 4:
        print(basket)
        item  = input("Enter the item you have purchased -- ")
        amount = int(input("Enter the purchased amount -- "))
        Total_amount += amount

    elif choice ==5:
        print(f"The total bill is {Total_amount}")
    elif choice == 6:
        print("Thanks for using Basket Bill calculator..!")
        break
    else:
        print("Invalid input..!")