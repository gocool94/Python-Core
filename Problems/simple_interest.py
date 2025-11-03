# problem number 10 - Simple interest calculator

amount = float(input("Enter amount - "))
year = float(input("Enter year (if months - convert it to years) "))
interest = float(input("Enter the interest percentage "))

#PNR/100
Simple_interest = (amount * year * interest)/100
print(Simple_interest)