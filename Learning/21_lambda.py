## Lambda

def double(x):
    return x * 2
print(double(x=10))

#lambda parameters : expression
double_using_lambda = lambda x : x * 2
print(double_using_lambda(20))

add = lambda x , y : x + y
print(add(19,20))

max = lambda x , y : x if x > y else y
print(f"{max(2000,30)} is greater")
min = lambda x , y :x if x < y else y
print(f"{min(30,2000)} is lesser")


is_even = lambda x : x%2 == 0
print(is_even(22))

age_check = lambda x :'you are eligible to vote' if x > 18 else 'you are not eligible to vote'
print(age_check(1))