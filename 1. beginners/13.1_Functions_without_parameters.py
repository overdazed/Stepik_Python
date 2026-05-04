##### custom functions #####

### Functions ###
# In previous lessons, 
# we used Python's built-in functions print(), input(), int(), str(), len() and many others. 
# It's time to start writing your own functions.

# At the very beginning of the course, you were asked to solve a problem in 
# which you needed to draw a star rectangle with dimensions 5×7 
# (5 lines and 7 columns).

# Our first version of the code looked something like this:
print('*******')
print('*******')
print('*******')
print('*******')
print('*******')

# Next, we would study the operator of multiplying a string by a number (the repetition operator) and write the code:
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)
print('*' * 7)

# And finally, we studied loops, after which the code would look like:
for _ in range(5):
    print('*' * 7)
    
# Now let’s imagine that you need to draw not one such rectangle, but several, say, 3 of them.
# Then the program code will look like:
for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)

print()

for _ in range(5):
    print('*' * 7)
    
# And although the previous code completely solves the problem, it is not without its drawbacks. 
# 1. Firstly, it is quite cumbersome due to the repetition of the part of the code responsible for drawing the rectangle. 
# 2. Secondly, if you need to change the dimensions of the rectangle, you will have to change them three times, 
# in each part of the code that displays the rectangle.

# Instead of repeating the code to draw the rectangle, you can wrap it in a separate function and call it 3 times.

# To create a function we write the following code:

def draw_box():
    for _ in range(5):
        print('*' * 7)
        
# When a function is created, in order to see the result of its work, you need to call it by name:
draw_box()

# Now, to draw 3 rectangles, you can write the code:
draw_box()
print()
draw_box()
print()
draw_box()

# The code has become shorter, more readable (due to the successful name of the function), 
# and most importantly, if different dimensions of the rectangle are required, 
# it will be enough to change only the function itself draw_box().


### Naming functions ###
# unctions are named in the same way as variables. 
# The function name should be descriptive enough that 
# anyone reading your code can guess what the function does.

# Python also requires compliance with the same rules as when naming variables:
# 1. The function name uses only the Latin letters az, AZ, numbers and the underscore character (_);
# 2. The function name cannot begin with a number;
# 3. The name of the function should, if possible, reflect its purpose;
# 4. upper and lower case characters are different.

# !!! Remember :  Python is a case-sensitive language. When naming variables and functions, 
# it is customary to use the lower_case_with_underscores style 
# (words made up of small letters with underscores).

# Because functions perform actions , most programmers prefer to use verbs in function names . For example:
# - the function that draws the rectangle can be called  draw_box();
# - the function that prints the receipt can be called print_check();
# - a function that calculates wages before deductions can be called calculate_gross_рау().

# Each of these names gives a description of what the function does.


### Function Declaration ###
# So, a function is a separate, functionally independent part of a program that performs a specific task.

# Functions are declared using a keyword  def (from the English define - to determine). The keyword defis followed by the function name, parentheses,  () and a colon :.

def function_name():
    code block
    
# !!!    The first line of a function declaration is called the function header.

# The next line starts with a block of code - the body of the function. 
# It is a set of instructions that form a single unit and are executed every time a function is called.


### Calling a function ###
# To call a function, write its name and parentheses.

# !!! Important: very often novice programmers forget to call a function. Remember that declaring a function does not call it.
# function declaration
def print_message():
    print('I am Arthur,')
    print('king of the british. ')

# function call
print_message()


### Notes ###

# Note 1: 
# Note that declaring a user-defined function is a bit like using the conditional statement if and loops for and while.

# Note 2: 
# A function declaration must precede its call. The following program code:
# function call
print_message()
# function declaration
def print_message():
    print('I am Arthur,')
    print('king of the british. ')
    
# will result in an error:
NameError: name 'print_message' is not defined

# Note 3: 
# When declaring a function, you must ensure that each line of the function body begins with the same number of spaces, otherwise an error will occur. For example, the following function definition will result in an error:

def print_greeting():
    print('Доброе утро!')

print('Сегодня мы будем изучать функции.')
    print('Это очень важная тема!')
    
# Note 4:
# Sometimes, when declaring a function, you need to make a kind of stub so that the function does not perform anything. Then we use the keyword pass:
def do_nothing():
    pass

# We declared a function called do_nothing(). 
# The body of such a function contains a single line of code that does nothing.

# Note 5: 
# Functions are often called subroutines.

# Note 6:
# Dedicated to everyone who forgets to call a function and expects a result from it:
https://ucarecdn.com/ae081f0b-e4c6-4bbb-8326-5e00342e81ff/

# -----------------------------------------------------------------------------------------------
## A separate functionally independent part of a program that solves a specific problem is called ##
# block
# parameter
##function
# expression

## The first line of the function definition is called ##
## title
# body
# initialization
# introduction

## The program code contained in a function is called ##
# introduction
# title
# body
# initialization


## To perform a function, it ##
# a) exports it
## b) calls it
# c) defines it
# d) imports it

## Which names are valid for a function name in Python? ##
##print_numbers
##find_sum_1
#1check_condition
##is_valid
##_myfunction
##draw_triangle

## What is the operator used for pass? ##
# to return a value from a function
# to interrupt a function
##to create a stub

# Nothing happens while the pass statement is executed, 
# so it can be used as a placeholder in places where it is syntactically necessary, 
# such as in statements where the body is required, such as def. 
# Thus, the pass operator is used where the code has not yet appeared, but is planned.

# ------------------------------------------------------------------------------------------------
## Star rectangle 1 ##
# Write a function draw_box() that outputs a star rectangle with dimensions 14×10 according to the sample:
**********
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
*        *
**********

def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*',' '*6,'*')
    print('*' * 10)
    
draw_box()
#########

def draw_box():
    print("*" * 10)
    
    for i in range(12):
        print("*", "*", sep=" " * 8)
    
    print("*" * 10)
    
draw_box()

# -------------------------------------------------------------------------------------------------
## Star triangle 1 ##
# Write a function draw_triangle() that prints a star-shaped right triangle with 
# legs equal to 10 according to the sample:

*
**
***
****
*****
******
*******
********
*********
**********

# function declaration
def draw_triangle():
    for i in range(10+1):
        print('*' * i)

# main program
draw_triangle()  # function call
########
# function declaration
def draw_triangle():
    n = 10
    for i in range(n):
        print("*" * (i + 1))

# main program
draw_triangle()  # function call
draw_triangle()  # function call