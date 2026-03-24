# ██████████████████████████████████████████████████████████████
# ██   ⚡ PYTHON SET MASTERCLASS                              ██
# ██                                                          ██
# ██████████████████████████████████████████████████████████████



# ░▒▓█ ▶ 01 — WHAT IS A SET ? █▓▒░
# ══════════════════════════════════════════════════════════════

"""
A Set in Python is a collection of unique elements.

👉 No duplicates allowed
👉 Unordered
👉 Written using { }

"""



# ░▒▓█ ▶ 02 — WHY SET ? (REAL WORLD USE CASES) █▓▒░
# ══════════════════════════════════════════════════════════════
# User id
# Email id


# ░▒▓█ ▶ 03 — CREATING SETS { } █▓▒░
# ══════════════════════════════════════════════════════════════
"""

{}
set([])

"""

"""fruits = {"mango","Orange","Grapes","mango"}
fruits_1 = set(["mango","Orange","Grapes","mango"])
print(fruits_1)"""

# ░▒▓█ ▶ 04 — SET PROPERTIES █▓▒░
# UNIQUE • UNORDERED • MUTABLE
# ══════════════════════════════════════════════════════════════
fruits = {"mango","Orange","Grapes","Jackfruit"}

for i in fruits:
    print(i)

# ░▒▓█ ▶ 05 — ADDING ITEMS (add / update) █▓▒░
# ══════════════════════════════════════════════════════════════
"""colors = {"red", "blue"}
colors.add("green")
colors.update(["manjal" , "oodha"])
print(colors)"""

fruits = {"mango","Orange","Grapes","Jackfruit"}
fruits.add("Guava")
fruits.update(["pomo","Dragon fruit"])
print(fruits)

# ░▒▓█ ▶ 06 — REMOVING ITEMS (remove / discard / pop) █▓▒░
# ══════════════════════════════════════════════════════════════
"""colors.remove("manjal")
colors.discard("oo")
"""
fruits.remove("pomo")
print(fruits)
fruits.discard("berry")

# ░▒▓█ ▶ 07 — LOOPING THROUGH SET █▓▒░
# ══════════════════════════════════════════════════════════════

for i in fruits:
    print(i)


# ░▒▓█ ▶ 08 — BUILT-IN METHODS █▓▒░
# clear() • copy() • len()
# ══════════════════════════════════════════════════════════════
print(fruits)
new_fruits = fruits.copy()
print(len(fruits))
fruits.clear()
print(fruits)


# ░▒▓█ ▶ 09 — SET OPERATIONS (MATH POWER 🔥) █▓▒░
# union() • intersection() • difference()
# ══════════════════════════════════════════════════════════════
a = {1,2,3}
b = {3,4,5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))


# ░▒▓█ ▶ 10 — SET vs LIST vs TUPLE █▓▒░
# ══════════════════════════════════════════════════════════════
"""List -> All
Tuple -> change
SET -> change -> Unordered --> duplicate"""


# ░▒▓█ ▶ 11 — FROZENSET (IMMUTABLE MODE 🔒) █▓▒░
# ══════════════════════════════════════════════════════════════

fs = frozenset([1,2,3])
#duplicate tuple


# ░▒▓█ ▶ 12 — REAL LIFE PROJECT (REMOVE DUPLICATES) █▓▒░
# ══════════════════════════════════════════════════════════════
student = []
for i in range(0,10):
    name = input("Enter the student name ")
    student.append(name)

final_student = set(student)

print(f"The final students are {final_student}")



"""
data = [5, 12, 7, 20, 3, 15]

challenge = reduce(
    lambda x, y: x * y,
    filter(
        lambda x: x % 4 == 0,
        map(lambda x: x * 2, data)
    )
)

print("Final Output:", challenge)
"""