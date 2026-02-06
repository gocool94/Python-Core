# ==================================
# FOR LOOP - PART 1
# ==================================

# ----------------------------------
# BASIC FOR LOOP SYNTAX
# ----------------------------------
# for keyword
# in keyword
# indentation

Program = "Python"

for i in "Python is great":
    print(i)

# ----------------------------------
#  RANGE() FUNCTION
# ----------------------------------
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(9):
    print(i)

for i in range(5,10):
    print(i)

print("--------")
for i in range(0,11,2):
    print(i)
# ----------------------------------
# PRINTING NUMBERS USING FOR LOOP
# ----------------------------------
# Print 0 to 4
# Print 1 to 10

# ----------------------------------
# SIMPLE EXAMPLES
# ----------------------------------
# Print even numbers
print("Even numbers-----")
for i in range(0,11,2):
    print(i)
print("Odd numbers ----")
for j in range(1,11,2):
    print(j)
# Print odd numbers
# Countdown example

for reverse_number in range(100,0,-1):
    print(f"Seconds to launch {reverse_number}")

# ----------------------------------
# COMMON BEGINNER MISTAKES
# ----------------------------------
# Indentation errors
# Off-by-one error
# range confusion
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")
print("Hello world.!!")