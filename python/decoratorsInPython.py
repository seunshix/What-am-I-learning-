# Functions are objects

def add_five(num):
    print(num + 5)

print(add_five)
# The line above outputs <function add_five at 0x0000021D469404A0>
# This tells me that functions in python are also objects

# 2. Functions within functions

def add_ten(num):
    def add_two(num):
        return num+2
    num_plus_two = add_two(num)
    print(num_plus_two + 8)

#add_two(10) # this will give a NameError because add_two is within add_five scope

# 3. Returning functions with functions

def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    
    if operation == '+':
        return add
    elif operation == '-':
        return sub

add_function = get_math_function('+')
print(add_function(4, 6))

sub_function = get_math_function('-')
print(sub_function(4, 6))


# 4. Decorating a function

# def title_decorator(print_name_function):
#     def wrapper():
#         print('Professor:')
#         print_name_function()
#     return wrapper

# def print_my_name():
#     print('Eniola')

# def print_your_name():
#     print('Joe')

# decorated_function = title_decorator(print_your_name)
# decorated_function()

# 5. Decorators

# def title_decorator(print_name_function):
#     def wrapper():
#         print('Professor:')
#         print_name_function()
#     return wrapper

# @title_decorator
# def print_my_name():
#     print('Eniola')

# @title_decorator
# def print_your_name():
#     print('Joe')

# print_your_name


# 6. Decorators w/ Parameters

def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print('Professor:')
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_my_name(name, age, sex):
    print(f'Your name is {name}, you are a {sex} of {age} years old')
print_my_name('Shelby', 16, 'woman')