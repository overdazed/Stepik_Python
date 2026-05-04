##### 6.1 Numeric data types: int, float #####

# 1. Integer data type int
#The following program demonstrates all integer operators:

a = 13
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)

# To make numbers easier to read, you can use the underscore character:

num1 = 25_000_000
num2 = 25000000
print(num1)
print(num2)

# 2. Floating point numbers float
# The following program demonstrates arithmetic operators:

a = 13.5
b = 2.0

total = a + b
diff = a - b
prod = a * b
div = a / b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)
print(a, '**', b, '=', exp)

### min() and max() ###

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)

### function abs() ###
# absolute value
print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))

# -------------------------------------------------------------------
### Assignments ###
# Area of a triangle

#Write a program that reads the lengths of two legs in a right triangle and prints its area.

# S = 1/2 * a * b

a = float(input())
b = float(input())

s = (1/2)*a*b

print(s)
# -------------------------------------------------------------------
# Two old ladies

# Two old ladies walk towards each other at constant speeds IN1 and IN2. km/h Determine after what time (in hours) the old ladies will meet if the distance between them is S km.

s = float(input())
a = float(input())
b = float(input())

x = s / (a+b)

print(x)
# -------------------------------------------------------------------
# Reciprocal number
# Write a program that reads one number from the keyboard and prints its inverse . If the number entered from the keyboard is zero, then print “There is no reciprocal number” (without quotes).

#(x)^^-1 = 1/x

x = float(input())

if x != 0:
    x = 1/x
    print(x)
else:
    print("Обратного числа не существует")
# -------------------------------------------------------------------
# Fahrenheit 451

#Write a program that determines what temperature on the Celsius scale corresponds to a given value on the Fahrenheit scale.

# C = (5/9)*(F-32)
f = float(input())

c = 5/9*(f-32)

print(c)
# -------------------------------------------------------------------
# Dog age
# The number is given as input to the programnn– number of dog years. Write a program that calculates the age of a dog in human years using the following algorithm: for the first two years, a dog year is 10.5 human years, after that each dog year is equal to 4 human years.

age = int(input())

if age <= 2:
    n = age*10.5
    print(n)
else:
    # first 2 years are 10.5 each = 21 years + rest years * 4
    n = ((age-2)*4) + 21
    print(n)
# -------------------------------------------------------------------
# First digit after dot
#A positive real number is given. Print its first digit after the decimal point.

f = float(input())

x = f / 0.10
x = int((x // 10 ** 0) % 10)

print(x)
# -------------------------------------------------------------------
# Fraction
# A positive real number is given. Print its fractional part.

f = float(input())

#x = f - int(f)
#x = f % 1
x = f-(f*100//100)

print(x)
# -------------------------------------------------------------------

# What number will be displayed on the screen as a result of executing the following code?
num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
print(num)
# -------------------------------------------------------------------
# Largest and smallest
# Write a program that finds the smallest and largest of five numbers.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_num = min(a, b, c, d, e)
max_num = max(a, b, c, d, e)

print ("Наименьшее число =", min_num)
print ("Наибольшее число =", max_num)
# -------------------------------------------------------------------
# Sorting three
# Write a program that orders three numbers from largest to smallest.
a = int(input())
b = int(input())
c = int(input())

min_num = min(a, b, c)
max_num = max(a, b, c)

sum = a+b+c
middle_num = sum - min_num - max_num

print(max_num)
print(middle_num)
print(min_num)
# -------------------------------------------------------------------
# Interesting number
# Let's call a number interesting if the difference between the maximum and minimum digits is equal to the average digit. Write a program that determines whether a number is interesting or not. If the number is interesting, you should output “Number interesting”, otherwise - “Number uninteresting”.

# interesting = difference between the maximum and minimum digits is equal to the average digit

num = int(input())
# to list those three numbers
# e.g. 945
a = (num // 10 ** 2) % 10
b = (num // 10 ** 1) % 10
c = (num // 10 ** 0) % 10

# min and max
min_num = min(a, b, c)
max_num = max(a, b, c)

# x = 9 - 4 = 5
i_num = max_num - min_num

# 9 + 4 + 5 = 18
sum = a+b+c
# 18 - 4 - 9 = 5
middle_num = sum - min_num - max_num

if i_num == middle_num:
    print("Число интересное")
    #print(i_num, b)
else:
    print("Число неинтересное")
    #print(i_num, b)
# -------------------------------------------------------------------
# Absolute amount
# Given five numbers a1, a2, a3, a4, a5. 
# Write a program that calculates the sum of their modules|a1| + |a2| + |a3| + |a4| + |a5|.

a1 = abs(float(input()))
a2 = abs(float(input()))
a3 = abs(float(input()))
a4 = abs(float(input()))
a5 = abs(float(input()))

x = a1 + a2 + a3 + a4 + a5

print(x)
# -------------------------------------------------------------------
# Manhatten distance
# https://de.wikipedia.org/wiki/Manhattan-Metrik
# Walking around Manhattan, you can't get from point A to point B by taking a shortcut. Unless you know how to walk through walls, you will definitely have to walk along its parallel-perpendicular streets.
# On a plane, the Manhattan distance between two points (p1; p2) and(q1;q2) defined like this |p1 - q1| + |p2 - q2|.

#Write a program that determines the Manhattan distance between two points whose coordinates are given.

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

x = abs((p1 - q1)) + abs((p2 - q2))

print(x)
# -------------------------------------------------------------------



##### 6.2 String data type #####

# Let's talk about the string data type and learn how to use the built-in functions len(), str()and also work with the operators +, *, in.

## 1. String data type
s1 = 'Python rocks!'
s2 = "Python rocks!"

s = input() #is by default a str

# To specify an empty string, we use two quotes of the same type:
s1 = ''   # пустая строка
s2 = ' '  # строка состоящая из одного символа пробела

## String length
s1 = 'abcdef'
length1 = len(s1)               # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)
print(length2)

## Converting numbers to string
# To convert a string to a number, we used the int()and functions float(). For the reverse conversion, that is, from a number to a string, we use the function str():

num1 = 1777    # целое число
num2 = 17.77   # число с плавающей точкой
s1 = str(num1) # преобразовали целое число в строку '1777'
s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

## String concatenation
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)

# Using string concatenation, you can emulate data output, which we previously did using the optional parameters  sepand  end. The following two lines of code do the same thing:
print('a', 'b', 'c', sep='*', end='!')
print()  # переход на новую строку
print('a' + '*' + 'b' + '*' + 'c' + '!')

## Multiplying a string by a number
# In Python you can also multiply a string by a number. 
s = 'Hi' * 4
print(s)

#The operator for multiplying a string by a number (repetition) is very convenient in practice. For example, we want to print a string consisting of 75 characters -. We can do this with code:
print('-' * 75)


## Notes ##
# Note 1: Triple quotes in Python are used for multiline text. For example,
text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''

# Note 2: At first glance, it may seem strange that you can use both single and double quotes, but this approach makes it very easy to add the necessary quotes to the string:
s1 = 'Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"'
s2 = "Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'"
print(s1)
print(s2)

# -------------------------------------------------------------------------

### PRACTICE ###
## What will the code snippet below show?
mystr = 'да'
mystr = mystr + 'нет'
mystr = mystr + 'да'
print(mystr)
# --------------------------------------------------------------------------------------------------
## What will the code snippet below show?
str1 = '1'
str2 = str1 + '2' + str1
str3 = str2 + '3' + str2
str4 = str3 + '4' + str3
print(str4)
# --------------------------------------------------------------------------------------------------
## What will the code snippet below show?
mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)

# --------------------------------------------------------------------------------------------------
## Write a program that displays text:

# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."

print('"Python is a great language!"'+ ", said Fred.", '"I don'+"'t", 'ever remember having this much fun before."')
# --------------------------------------------------------------------------------------------------
## What's your name?
# Write a program that reads two lines from the keyboard - the user's first and last name and prints the phrase:

# “Hello [entered first name] [entered last name]! You have just delved into Python."
first = input()
last = input()

print("Hello", first, last + "! You have just delved into Python")

# --------------------------------------------------------------------------------------------------
# Football team
# Write a program that reads the name of a football team from the keyboard and prints the phrase:

# "Football team [entered string] has length [length of entered string] characters."

team = input()

print("Футбольная команда", team, "имеет длину", len(team), "символов")

# --------------------------------------------------------------------------------------------------
# Three cities
# The names of three cities are given. Write a program that determines the shortest and longest name of a city.

a = input()
b = input()
c = input()

min_city = min((len(a)), (len(b)), (len(c)))

if (min_city == len(a)):
    print(a)
elif (min_city == len(b)):
    print(b)
elif (min_city == len(c)):
    print(c)
    
max_city = max((len(a)), (len(b)), (len(c)))

if max_city == len(a):
    print(a)
elif max_city == len(b):
    print(b)
elif max_city == len(c):
    print(c)
    
# --------------------------------------------------------------------------------------------------
# Arithmetic strings
# Introduced 3 lines in random order. Write a program that finds out whether an arithmetic progression can be constructed from the lengths of these strings.

# Sample Input 3:
#aaaaaaaaaa10
#1111111Nm
#22222r
# Sample Output 3:
#YES

# 12
a = len(input())
# 9
b = len(input())
# 6
c = len(input())

# 12
max = max(a, b, c)
# 6
min = min(a, b, c)

# (12+9+6) - 6 - 12
# 9
middle = (a + b + c) - min - max

# 12 - 9 = 9 - 6
# 3 == 3
if max - middle == middle - min:
    print("YES")
else:
    print("NO")
# -----------------------------------------------------------------

## Operator in ##

# Python has a special operator inthat allows you to check that one string is inside another.

# Consider the following code:
s = input()
if 'a' in s:
    print("The input text contains 'a'")
else:
    print("The input text doesn't contain 'a'")

#We can use the operator intogether with the logical operator not. For example

s = input()
if '.' not in s:
    print('There is no dot in the text.')
else:
    print("There is a dot in the text.")
    
#Using the operator, in we can simplify the following code to check that a variable  s is equal to one of the five characters 'a', 'e', 'i', 'o', 'u':

s = input()

if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')
else:
    print('NO')
    
# bye:
if len(s) == 1 and s in 'aeiou':
    print('YES')
    

## What values ​​can a string variable take sso that the word “YES” is printed as a result of executing the code?

if s in 'abc123abc':
    print('YES')
else:
    print('NO')

s = 'a'

s = '23'

s = '1'

s = '123abc'

s = '3ab'

# ----------------------------------------------------------------
# Mood color blue
#Write a program that reads one line and then prints “YES” if the input line contains the substring “blue” and “NO” otherwise.

x = input()

if 'синий' in x:
    print("YES")
else:
    print("NO")
    
# ----------------------------------------------------------------
# Are we resting?
# Write a program that reads one line and then prints “YES” if the input line contains the substring “Saturday” or “Sunday”, and “NO” otherwise.

x = input()

if 'суббота' in x or 'воскресенье' in x:
    print('YES')
else:
    print('NO')
    
# ----------------------------------------------------------------
# Correct email
# We will consider an email address to be correct if it contains a dog symbol ( @) and a dot ( .). Write a program that checks the validity of an email address.
x = input()

if '@' in x and '.' in x:
    print('YES')
else:
    print('NO')
# ----------------------------------------------------------------


##### 6.3 Module math #####

## The lesson is dedicated to the module  math, which contains mathematical functions for working with real numbers.

## Modules ##
# As already mentioned, one of the advantages of the Python language is the many different functions that are already implemented and ready to be used. 
# Such functions are packaged in modules. 
# In Python, a module is a library of functions that you can connect to your programs.

## math module ##
# This module provides extensive functionality for performing calculations with real numbers (floating point numbers).

# To use these functions, you need to include the module at the beginning of the program, which is done with the import command :
import math

#After connecting the module, we can use its functions. Let us want:

# - calculate \sqrt2 (square root of two);
# - round the number 3.8 up and down to the nearest whole number

import math

num1 = math.sqrt(2)     # calculating the square root of two
num2 = math.ceil(3.8)   # rounding a number up
num3 = math.floor(3.8)  # rounding a number down

print(num1)
print(num2)
print(num3)

## Features of connecting modules
# In order not to specify the module name and the dot character when calling functions, we write the following code:
from math import *

num1 = sqrt(2)     # calculating the square root of two
num2 = ceil(3.8)   # rounding a number up
num3 = floor(3.8)  # rounding a number down

print(num1)
print(num2)
print(num3)

# If we only need to use some module functions, then we can import only them like this:
from math import sqrt, ceil

print(sqrt(25))
print(ceil(34.7))

print(floor(12.8))  # will result in an error since the floor function is not connected


## List of math module functions ##
# Function      Description

# Rounding
# int()	        Rounds a number towards zero
# round(x)	    Rounds a number xto the nearest integer. If the fractional part of a number is 0.5, then the number is rounded to the nearest even number
# round(x, n)	Rounds a number xto n digits after a period
# floor(x)	    Rounds a number xdown (“floor”)
# ceil(x)	    Rounds a number xup (“ceiling”)
# abs(x)	    Module of number x(absolute value)

# Roots, logarithms, powers and factorial
# sqrt(x)	    Square root of a number x
# pow(x, n)	    Raising a number x to a power n (x**n)
# log(x)	    Natural logarithm of a number x. The base of the natural logarithm is equal to the numbere
# log10(x)	    Decimal logarithm of a number x. The base of the decimal logarithm is equal to the number 10
# log(x, b)	    Logarithm of a number xto the baseb
# factorial(n)	Factorial of a natural numbern

# Trigonometry
# degrees(x)	Converts an angle xspecified in radians to degrees
# radians(x)	Converts an angle xspecified in degrees to radians
# cos(x)	    Cosine of the angle x, specified in radians
# sin(x)	    Sine of the angle x, specified in radians
# tan(x)	    Tangent of the angle x, specified in radians
# acos(x)	    Returns the angle in radians from 0 to Pi, cos which is equal to x
# asin(x)	    Returns the angle in radians from -(pi/2) to (pi/2), sin which is equal to x
# atan(x)	    Returns the angle in radians from -(pi/2) tp (pi/2), tan which is equal to x
# atan2(y, x)	Polar angle (in radians) of a point with coordinates(x, y)

# !!! To extract the square root n ** 0.5, you can use the code instead of math.sqrt(n)


## List of math module constants ##

# A constant   	Description
# pi	        Number Pi=3.141592653589793
# e	            Number It is= 2.718281828459045 (Euler's constant)

# --------------------------------------------------------------------------------------------
# Euclidean distance

# On a plane, the Euclidean distance between two points (x1; y1) and (x2; y2) defined like this r = \sqrt{(x1-x2)^2 + (y1-y2)^2}

from math import *

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

r = sqrt((pow((x1-x2), 2)) + (pow((y1-y2), 2)))

print(r)

# --------------------------------------------------------------------------------------------
# Area and length

# Write a program to determine the area of ​​a circle and the circumference of a circle along a given radius r.

# S = pi * r**2
# C = 2*pi*r

from math import *

r = float(input())

circle_area = pi * pow(r, 2)
circle_length = 2 * pi * r

print(circle_area, circle_length, sep='\n')

# --------------------------------------------------------------------------------------------
# Average values

# In mathematics, the following average values ​​are distinguished:

# - arithmetic mean of numbers a and b: (a+b)/2;
# - geometric mean of numbers a and b:\sqrt{(a*b)};
# - harmonic mean of numbers a and b: 2*(a*b)/(a+b);
# - mean square of numbers a and b: \sqrt{((a**2) + (b**2))/2}.

from math import *

a = float(input())
b = float(input())

# arithmetic mean of numbers a and b
arith = (a+b)/2

# geometric mean of numbers a and b
geom = sqrt(a*b)

# harmonic mean of numbers a and b
harm = (2*(a*b))/(a+b)

# mean square of numbers a and b
mean = sqrt((pow(a,2)+pow(b,2))/2)

print(arith, geom, harm, mean, sep='\n')

# --------------------------------------------------------------------------------------------
# Trigonometric expression

# Write a program to calculate the value of a trigonometric expression

# sin(x) + cos(x) + tan(x)^2

# by a given number of degrees x.

# degrees to radians
# r = (x⋅π)/180

from math import *

angle_degrees = float(input())

# convert angle to radians
r = radians(angle_degrees)

# Calculate the value of the trigonometric expression (example expression used: sin(angle) + cos(angle))
result = sin(r) + cos(r) + pow((tan(r)), 2) # tan(r)**2

print(result)

# --------------------------------------------------------------------------------------------
# Floor and ceiling

# Write a program to calculate the value ⌈x⌉ + ⌊x⌋ by given real number x.

from math import *

x = float(input())

result = ceil(x) + floor(x)

print(result)

# --------------------------------------------------------------------------------------------
# Quadratic Equation

# Given three real numbers a, b, c. 
# Write a program that finds the real roots of a quadratic equation:

# (a*x)**2 + b*x + c = 0

#If an equation has two roots, then they should be derived in ascending order .

# a != 0, b, c

from math import *

# Input coefficients
a = float(input())
b = float(input())
c = float(input())

# Calculate discriminant
d = b**2 - 4*a*c

# Check if roots are real
if d > 0:
    # Two real roots
    x1 = (-b - sqrt(d)) / (2*a)
    x2 = (-b + sqrt(d)) / (2*a)
    # are used to print the roots of the quadratic equation in ascending order
    print(min(x1, x2))
    print(max(x1, x2))
elif d == 0:
    # One real root (repeated)
    x = (-b / (2*a))
    print(x)
elif d < 0:
    # No real roots
    print('Нет корней')
    
# -------------------------------------------------------------------------------
# Regular polygon

# A regular polygon is a convex polygon in which all sides and all angles between adjacent sides are equal.
# Area of ​​a regular polygon with side length a and number of sides n calculated by the formula: 

# S = (n*a**2)/ 4*tan(pi/n)

# two numbers are given: natural number n, real number a

from math import *

# number of sides of the regular polygon
n = int(input())
# length of one side of the polygon
a = float(input())

area = (n*a**2) / (4*tan(pi/n))

#area = n*pow(a,2) / (4*tan(pi/n))

print(area)