# Scope --> Local vs Global variable
# ** Args
# ** Kwargs


#Global Variable & Local Variable


channel = "Viay Tv"

def my_room():
    global secret
    secret = "I have diary"
    print(f"{secret} in my room")
    print(channel)

my_room()
print(secret)


def calculate_bill(*values):
    total = sum(values)
    print(f"total bill {total}")

calculate_bill(20,10,12,12,12,14,35,46)

def print_student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()} :{value}")

print_student_details(name="Keerthiga" , age = 32 , city="Chennai", role = "Engineer",hobby="playing cricket")











# Quick problem




total_user = 0
def create_profile(name,*skills,**extra_info):
    global total_user
    total_user += 1

    print(f"User has been created : {name}")
    print(f"User ID : {total_user}")

    #Args loop
    print("Skills")
    for skill in skills:
        print(f"{name} has {skill} Skills")
    

    ## kwargs loop
    print("Extra information ")
    for key, value in extra_info.items():
        print(f" --> {key} : {value}")

create_profile("Bagya","Python","SQL", city="Chennai",DOB = '26-01')
create_profile("Anu","Java","SQL",experience = 2, company = "TCS")
