"""
📘 For Loop with if-else & Pattern Problems
1️⃣ Why use if-else inside for loop

• Decision making inside repetition
• Different output for different values

2️⃣ Even or Odd problem

• Checking conditions inside loop
• Understanding modulo logic

3️⃣ Pattern problems using for loop

• Star patterns
• Number patterns
• Row-wise thinking

4️⃣ Common beginner mistakes

• Indentation issues
• Range confusion
• Logic errors

5️⃣ Mini challenges

🧠 Problem: Sum of Numbers Based on Condition
📌 Problem Statement

Write a Python program that:

Iterates from 1 to 30

Adds even numbers to one sum

Adds odd numbers greater than 10 to another sum

Prints both sums at the end

"""


#Even or odd
"""
for i in range(1,100):
    if (i%2==0):
        print(f"The number {i} is even")
    else:
        print(f"The number {i} is odd ")
"""


#Star pattern

"""num = int(input("Enter the number - "))

for n in range(1,num+1):
    print("*" * n)"""
"""
num = int(input("Enter the number for inverted star - "))

for n in range(num , 0 , -1):
    print(str(n) * n)


    """

count_even_sum = 0
count_odd_sum = 0
for i in range(1,31):
    if (i%2==0):
        count_even_sum = count_even_sum + i
        print("Even")
    else:
        if (i>10): 
            count_odd_sum = count_odd_sum+ i

print(f"Odd sum value is  {count_odd_sum}")
print(f"Even sum value is {count_even_sum}")




    