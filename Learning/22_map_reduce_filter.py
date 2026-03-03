# ██████████████████████████████████████████████████████████████
# ██   ⚡ PYTHON FUNCTIONAL PROGRAMMING MASTERCLASS           ██
# ██                                                          ██
# ██████████████████████████████████████████████████████████████

# Functional programming.

"""
Functional Programming means:

Writing small, reusable functions

Avoiding modification of variables

Avoiding side effects

Using functions like map(), filter(), and reduce()
"""

# ░▒▓█ ▶ 01 — WHAT IS MAP() ? █▓▒░
# ══════════════════════════════════════════════════════════════

"""
map() is used to apply a function to every element in a sequence.

👉 Transforms data
👉 Returns a map object
👉 Needs list() to display result
"""



# ░▒▓█ ▶ 02 — MAP() SYNTAX █▓▒░
# ══════════════════════════════════════════════════════════════

"""
map(function, iterable)
"""

numbers = [1,2,3,4,5]
doubled = list(map(lambda num : num * 2,numbers))
print("The doubled list is ",doubled)





# ░▒▓█ ▶ 03 — WHAT IS FILTER() ? █▓▒░
# ══════════════════════════════════════════════════════════════

"""
filter() selects elements based on a condition.

👉 Returns only True values
👉 Used for filtering data
"""

numbers = [1,2,3,4,5,6]

filtered_list = list(filter(lambda num : num % 2 == 0 , numbers))
print("Filtered list is", filtered_list)


# ░▒▓█ ▶ 04 — FILTER() SYNTAX █▓▒░
# ══════════════════════════════════════════════════════════════

"""
filter(function, iterable)
"""

numbers = [1, 2, 3, 4, 5, 6]




# ░▒▓█ ▶ 05 — WHAT IS REDUCE() ? █▓▒░
# ══════════════════════════════════════════════════════════════

"""
reduce() reduces the sequence into a single value.

👉 Combines elements
👉 Works cumulatively
👉 Requires functools module
"""



# ░▒▓█ ▶ 06 — REDUCE() SYNTAX █▓▒░
# ══════════════════════════════════════════════════════════════

"""
from functools import reduce
reduce(function, iterable)
"""

from functools import reduce

numbers = [1, 2, 3, 4]

reduced_value = reduce (lambda x, y :  x + y, numbers)
print(reduced_value)




# ░▒▓█ ▶ 07 — DIFFERENCE BETWEEN MAP | FILTER | REDUCE █▓▒░
# ══════════════════════════════════════════════════════════════
"""
map()     → Transform
filter()  → Select
reduce()  → Combine
"""



# ░▒▓█ ▶ 08 — REAL LIFE MINI PROJECT █▓▒░
# ══════════════════════════════════════════════════════════════
"""
Scenario:
You have student marks.

1️⃣ Increase all marks by 5 (map)
2️⃣ Keep only marks >= 50 (filter)
3️⃣ Find total class marks (reduce)
"""

from functools import reduce

marks = [45, 67, 32, 90, 51]

marks_addition = list(map(lambda mark : mark + 5, marks))
passed = list(filter(lambda mark : mark >= 50,marks_addition))
total = reduce(lambda x,y :x + y,passed)

print("Marks added", marks_addition)
print("Passed", passed)
print("Total", total)







# ░▒▓█ ▶ 09 — FINAL CHALLENGE FOR ALL 🔥 █▓▒░
# ══════════════════════════════════════════════════════════════
"""
Given:


🎯 Challenge:
1️⃣ Double all numbers
2️⃣ Keep numbers divisible by 4
3️⃣ Multiply remaining numbers
4️⃣ Write in ONE line only
5️⃣ Use only lambda
"""
data = [5, 12, 7, 20, 3, 15]

multiply = reduce (lambda x , y : x * y,list(filter(lambda x : x % 4 == 0, list(map(lambda x : x * 2 , data)) )) )
print(multiply)