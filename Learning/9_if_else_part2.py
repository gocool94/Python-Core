"""
EPISODE 9 : Else if (elif) & Logical Operators in Python


---------------------------------------------------
1. if, elif, else
2. Logical operators: and, or, not
3. Common mistakes
4. Final coding challenge
---------------------------------------------------
"""

# ---------------------------------------------
# 1️⃣ BASIC if - elif - else
# ---------------------------------------------
# Already If & Else paathom..!
# Python-la decision eduka if, elif, else use pannuvom
# One condition TRUE na, adhu mattum execute aagum

# Age related problem 

age = 17
if (age > 18):
    print("Age is greater than 18")
elif (age == 18):
    print("You are exactly 18, Apply for Voters ID")
else:
    print("You are not eligible for voters id")

# ---------------------------------------------
# 2️⃣ ANOTHER SIMPLE EXAMPLE – Traffic Signal
# ---------------------------------------------

# signal variable-la traffic light value irukku

"""signal = input("Enter the signal ")
if signal == 'green':
    print("Goooooooo..!")
elif signal == 'yellow':
    print("Get ready..!")
elif signal == 'red':
    print("Stop")
else:
    print("Signal has some issue..!")"""


# ---------------------------------------------
# 3️⃣ LOGICAL OPERATORS
# ---------------------------------------------

# Logical operators use pannina
# multiple conditions check pannalam



# ---- AND operator ----
# and -> rendu conditions-um TRUE irukkanum
# Program for Voting and has_id = True

has_id = False
age = 19
if ((age > 18) and (has_id == True)):
    print("You can cast your vote..!")
else:
    print("You cannot vote.!")



# ---- OR operator ----
# or -> edhavadhu onnu TRUE irundha podhum
# Program consider sunday or saturday as holiday

day = 'SaturDay'.lower()
if ((day == 'sunday') or (day == 'saturday')):
    print("Yaaaaay, It's a holiday..!")
else:
    print("Go to school or work.!")



# ---- NOT operator ----
# not -> opposite result tharum
'''
is_raining = False

if not is_raining:
    print("You can go outside ☀️")
else:
    print("Stay inside 🌧️")
'''

# ---------------------------------------------
# 4️⃣ elif + logical operators (Marks example)
# ---------------------------------------------

"""
Mark 90 to 100 -> A grade
MArk 80 to 90 -> B grade
Mark 70 - 80 -> C grade
Mark 60 -70 -> D grade
MArk 50 - 60 -> Fail
"""

mark = 90 #int(input("Enter the mark scored - "))

if((mark >=90) and (mark <=100)):
    grade = 'A'
elif mark>=80 and mark<90 :
    grade = 'B'
elif mark>=70 and mark<80:
    grade = "C"
elif mark>=60 and mark<70:
    grade = "D"
elif mark>=50 and mark<60:
    grade = "Fail.!"
else:
    Grade = "Same class Fail.!"

print(f"The mark scored is {mark} and the grade is {grade}")





# ---------------------------------------------
# 5️⃣ COMMON BEGINNER MISTAKES (Explain only)
# ---------------------------------------------

# ❌ else if use panna koodadhu
# else if marks > 50: 
# #Elif  -- use pannanum..!  ❌

# ✅ Correct keyword is elif
# elif marks > 50:      ✅

# ❌ colon miss panna koodadhu
# if age > 18           ❌

# ✅
# if age > 18:          ✅


# ---------------------------------------------
# 6️⃣ FINAL CODING CHALLENGE 🎯
# ---------------------------------------------

"""
CHALLENGE: Simple Login System

Rules:
username = "admin"
password = "1234"

1. Username AND password correct na
   -> Login successful

2. Username correct BUT password wrong na
   -> Wrong password

3. Username wrong na
   -> Invalid username
"""

#  code 👇

username = input("Enter the username ")
password = input ("Enter the password ")

if (username == 'user' and password == 'password'):
    print("Login successfull.!")
elif (username =='user' or password == 'password'):
    print("Either one of them is correct.!")
    if (username != 'user'):
        print("Username is not valid.!")
    else:
        print("Passsword is not valid.!")
else:
    print("username and password is incorrect")
