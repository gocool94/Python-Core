# purpose of a decorator is to decorate a base function and add more beauty to it
# decorator is also a function


import time

def timer_check(base_fn):
    def enhanced_fn(*args):
        start_time = time.time()
        base_fn(*args)
        end_time = time.time()
        print(f"Task time is : {end_time - start_time} seconds")
    return enhanced_fn


def make_coffee():
    print("Preparing coffee..")
    time.sleep(1)
    print("Coffee is prepared..")

def make_tea():
    start_time = time.time()
    print("preparing tea")
    time.sleep(1)
    print("Tea is prepared..")
    end_time = time.time()
    print(f"Task time is : {end_time - start_time} seconds")




make_coffee()
#make_tea()
"""
dec_brew_tea = timer_check(make_coffee)
dec_brew_tea()

writing like this is equal to the

@timer_check
def make_coffee():
    print("Preparing coffee..")
    time.sleep(1)
    print("Coffee is prepared..")

"""


#decorator function with parameters

@timer_check
def brew_code(timereq):
    print("Creating brew ")
    time.sleep(timereq)
    print("Brew code..!")

brew_code(5)





