print("Electricity bill calculator ")
old_reading = int(input("Enter the old reading - "))
new_reading = int(input("Enter the new reading - "))
unit_charge = 3.89
unit_used = new_reading - old_reading
total_amount = unit_used * unit_charge
print(f" total units : {unit_used} total amount :Rs {total_amount}")