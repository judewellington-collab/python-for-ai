def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    pass #this line is just best practice. It means the function doesn't return anything.

greet(first_name="Jude", last_name="Wellington")

"""
best practice for function name is to have all lower case or snake case
"""

def check_weather():
    temperature=16  
    if temperature>25:
        print("It's hot outside")
    else:
        print("It's cold outside")

check_weather()

##default values to parameters
##parametr without default value comes first

def greet_people(last_name,first_name="Jude"):
    print(f"hello {first_name} {last_name}")

greet_people(last_name="Madhan",first_name="Vinay")

"""
variables defined outside function is called global variable
variable defined inside function is called local variable
global variable can be accessed inside the function.
local variable cannot be accessed outside the function.
"""

#this discount is a global variable
discount_global=20

def calculate_total(price):
    tax_rate=0.05
    #this discount is a local variable
    discount_local=10
    tax=price*tax_rate
    final_price=price+tax-discount_local
    print(f"Total: {final_price} and discount local variable: {discount_local}")
    final_price=price+tax-discount_global
    print(f"Total: {final_price} and discount global variable: {discount_global}")

calculate_total(price=100)

#this discount prints the global variable value
print(discount_global)

"""
return values in a function
"""

def add_return(a,b):
    return a+b

result=add_return(a=5,b=6)
print(result)

#calculate area
def calculate_area(length,width):
    area=length*width
    return area

room_area=calculate_area(length=5,width=4)
print(f"room size is {room_area} sq ft")

#returning multiple values from a function
def simple_function():
    numbers=[1,2,3,4,5]
    first_number=numbers[0]
    last_number=numbers[-1]
    return first_number,last_number

f,l=simple_function()
print(f)
print(l)
