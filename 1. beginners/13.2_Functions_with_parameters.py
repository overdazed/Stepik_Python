##### Functions with parameters #####

# In the previous lesson we defined a function draw_box()that outputs a star rectangle with dimensions 5×7:
def draw_box():
    for i in range(5):
        print('*' * 7)

draw_box()

# It would be much more convenient if the function draw_box()output a rectangle with arbitrary dimensions. 
# Indeed, functions can accept input parameters, which makes them more flexible.

# Functions with parameters are declared in the same way as functions without parameters, only with the following in parentheses:

def function_name(parameters):
    code block
    

# Let's rewrite the previous version of the function draw_box() 
# so that it accepts parameters that specify the height and width of the rectangle:

def draw_box(height, width):    # the function takes two parameters
    for i in range(height):
        print('*' * width)
        
# Now our function draw_box()takes two integer parameters height- the height of the rectangle and width- 
# the width of the rectangle, and to call it we need to specify them.

# To display a star rectangle measuring 5 by 7, we write the code:
draw_box(5, 7)

# To display a rectangle measuring 10 by 15, we write the code:
draw_box(10, 15)

# Now, using our new version of the function, draw_box()we can display rectangles of different sizes in one program. The following program code:
draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)


### More examples ###

# Let's write a function print_hello(n)that takes one natural number n and prints the word Hello exactly n once.

def print_hello(n):
    print('Hello' * n)
    
print_hello(3)
print_hello(5)
times = 2
print_hello(times)

# The function print_hello() can be made more flexible by passing one more parameter to it - the text to be output:

def print_text(txt, n):
    print(txt * n)
    
print_text('Hello', 5)
print_text('A', 10)


### Parameters vs Arguments ###

# An argument is any piece of data that is passed to a function when the function is called. 
# A parameter  is a variable that receives an argument passed to a function.

# For function draw_box(height, width):
​def draw_box(height, width):
    for i in range(height):
        print('*' * width)
# the parameters are the variables heightand width.

# At the time of calling the function draw_box(height, width):
height = 10
draw_box(height, 9)
# the arguments are heightand 9.

# !!! Function parameters are often called parametric variables.


### Making changes to settings ###

#When an argument is passed to a function, the function's parametric variable will refer to the value of that argument. 
# However, any changes you make to the parametric variable will not affect the argument.

def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)

# In the body of the function, changes are made to the values ​​of the parametric variables heightand width, 
# but this did not in any way affect the value of the variables n and m from the main program, which were 
# passed as arguments to the function draw_box().


### Notes ###

# Note 1
# Functions in Python can take as many parameters as you like.

# Note 2: 
# Sometimes instead of parameters and arguments they talk about formal parameters  and actual parameters. 
# Formal parameters are variables that we write when describing a function. 
# Actual parameters are what are actually substituted when calling a function.

# ---------------------------------------------------------------------------------------------------------------------
## The portion of data sent to a function at the time of its call is called ##
# title
##argument
# package
# parameter

## A special variable that receives a chunk of data when a function is called is called ##
## parameter
# argument
# header
# package

## Take a look at the function header below: ##
def my_function(a, b, с):
## Now take a look at the call to this function: ##
my_function(3, 2, 1)
## What values will be assigned to parameters a, b, c when the call is executed? ##

a - 3
b - 2
c - 1


## Take a look at the definition of function below: ##
def print_number(a, b, c):
    d = (a + c) // b
    print(d)
# What value will be shown after calling print_number(2, 3, 11)?


## What will the program below show? ##
def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

x = 1
y = 7
print(x, y)
change_us(x, y)
print(x, y)


## What will the program below show? ##
def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1

print_text('Python', 4)


# ------------------------------------------------------------------------------------------------
## The Star Triangle ##
# Write a draw_triangle(fill, base) function that takes two parameters:
## fill - the fill character;
## base - the size of the base of the isosceles triangle;
# and then outputs it.

# 7.8 - 8
# function declaration
def draw_triangle(fill, base):
    for i in range(base//2 + 2):
        print(fill * i)
    for j in range(base//2, 0, -1):
        print(fill * j)

# read data
fill = input()
base = int(input())

# call the function
draw_triangle(fill, base)
############
def draw_triangle(fill, base):
    for i in range(base // 2):
        print(fill * (i + 1))

    for i in range(base // 2, -1, -1):
        print(fill * (i + 1))

fill = input()
base = int(input())

draw_triangle(fill, base)

# ----------------------------------------------------------------------------------------------------
## Full name ##
# Write a function  print_fio(name, surname, patronymic)that takes three parameters:
## name – person’s name;
## surname – person’s surname;
## patronymic – person’s patronymic;
# and then prints the person’s full name.

# объявление функции
def print_fio(name, surname, patronymic):
    full_name = (surname[0] + name[0] + patronymic[0]).upper()
    print(full_name)

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

# ----------------------------------------------------------------------------------------------------
## Sum of digits ##

# Write a function print_digit_sum()that takes one integer numand prints the sum of its digits.

def print_digit_sum(n):
    # Convert the integer to a string to iterate over its digits
    num_str = str(n)
    # Initialize sum to 0
    digit_sum = 0
    # Iterate over each digit and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)
    # Print the sum of digits
    print(digit_sum)

# Test the function
n = int(input())

print_digit_sum(n)
####
# объявление функции
def print_digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10

    print(digit_sum)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)