# print() 
# The command print() displays data on the screen.
print("Hello world!")

# input()
# The command input() reads data entered from the keyboard.
print("What's your name")  # output text
name = input()  # input text
print("Hello,", name)  # output text

# sep, end
print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**')

print('a', 'b', 'c', end='@')
print('d', 'e', 'f', end='@@')

print('a', 'b', 'c', sep='*', end='finish')
print('d', 'e', 'f', sep='**', end='^__^')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='#')
print('m', 'n', 'o', sep='/', end='!')

# The sequence of characters \n is called an escape sequence and specifies a line feed. For example, this code
print('a', '\n', 'b', '\n', 'c', sep='*', end='#')

# it should ouput 'Hello, Name!' without whitespace between name_!
name = input()
print('Привет,', name, end='!')

# Sample Input 3 :
#python
#1
#2
#3
# Sample Output 3 :
#1python2python3

sep = input()
one = input()
two = input()
three = input()

print(one, two, three, sep=sep)

# variables
# change the value of multiple variables
name, surname = 'Timur', 'Guev'
print('Имя:', name, 'Фамилия:', surname)

# If you want to read text from the keyboard and assign it as a value to variables, you can write it like this: 
name, surname = input(), input()
print('Имя:', name, 'Фамилия:', surname)

# working with integers
# 1. Exponentiation operation
# 2. Operation of finding the remainder
# 3. Integer division operation
# 4. Processing the digits of a number
# 5. Problem solving

# 1. Exponentiation
# **
# The exponentiation operator a ** n raises the number a to the degree n. Let's look at the work of this operator using examples:
print(2 ** 0)
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** (-1))

print(2 ** 2 ** 3)

# 2. Remainder
# %
# The division with remainder operator returns the remainder of the division of two integers. 
# Let's look at the work of this operator using examples:
print(10 % 3)
print(10 % 4)
print(10 % 5)
print(10 % 6)
print(10 % 12)
print(10 % 20)

# 3. Integer
# //
# For positive numbers, the integer division operator behaves like normal division, except that it discards the decimal part of the result. Let's look at the work of this operator using examples:
print(10 // 3)
print(10 // 4)
print(10 // 5)
print(10 // 6)
print(10 // 12)
# When dividing negative numbers, remember that the result of integer division does not exceed the quotient. 
# In other words, rounding is taken downwards (number -4 less than number-3).
print(-10 // 3)

###### Integer Arithmetic ######

# Sample Input 1 : 8
# Sample Output 1 :
#8
#9
#10
# Sample Input 2 : -341
# Sample Output 2 :
#-341
#-340
#-339
# Sample Input 3 : -1
# Sample Output 3 :
#-1
#0
#1

num = int(input())
print(num, num+1, num+2, sep='\n')

# addiere alles zusammen
# Sample Input 1:
#9
#11
#2
# Sample Output 1:
#22
# Sample Input 2:
#-1
#10
#1
# Sample Output 2:
#10
# Sample Input 3:
#-7
#-10
#-3
# Sample Output 3:
#-20


### Volume, Surface Area ###
# V = a^3
# S = 6*a^2

# Sample Input 1 :
#25
# Sample Output 1 :
#Volume = 15625
#Total surface area = 3750

inp = int(input())

volume = inp**3
surface_area = 6*(inp**2)

print("Volume =", volume)
print("Total surface area =", surface_area)

# Write a program to calculate the value of a function f ( a ,b ) = 3(a + b)^3 + 275b^2 - 127a - 41 by entered integer values a and b.

# Sample Input 1 :
#1
#1
# Sample Output 1 :
#131

a = int(input())
b = int(input())

x = 3*(a+b)**3 + 275*b**2 - 127*a - 41

print(x)

# Write a program that reads an integer and then displays the next and previous integer with explanatory text.

# Sample Input 1 :
#20
# Sample Output 1 :
#The next number after 20 is: 21
#For the number 20 the previous number is: 19

num = int(input())

num_above = num + 1
num_below = num - 1

print("Следующее за числом", num, "число:", num_above)
print("Для числа", num, "предыдущее число:", num_below)

# Calculate cost of three computers (monitor, system, keyboard, mouse)

monitor = int(input())
system = int(input())
keyboard = int(input())
mouse = int(input())

cost_total = monitor + system + keyboard + mouse
cost_three = cost_total*3

print(cost_three)

#Write a program that calculates the sum, difference, and product of two integers entered from the keyboard.

num1 = int(input())
num2 = int(input())

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(num1, "+", num2, "=", addition) 
print(num1, "-", num2, "=", subtraction) 
print(num1, "*", num2, "=", multiplication) 

# An arithmetic progression
# e.g. − 6 ,− 3 ,0 ,3 ,6 ,9 ,12
# a_n = a1 + d (n−1)

a = int(input())
d = int(input())
n = int(input())

a_n = a + d * (n-1)

print(a_n)

# Write a program that reads a positive integer x and displays a sequence of numbers x,2x,3x,4x and 5x, separated by three dashes.


##### Integer Arithmetic pt.2 #####

23 // 7 = 

20 // 5 = 

2 // 5 = 

123 // 10 = 

-123 // 10 = 

# calculate the remainder
23% 7 = 

20% 5 = 

2% 5 = 

123% 10 = 


# result?
a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

# result?
a = 82 // 3 ** 2 % 7
print(a)

# A geometric progression
# b_n = b1*q**(n−1)

b_1 = int(input())
q = int(input())
n = int(input())

b_n = b_1 * q ** (n-1)
print(b_n)

#Write a program that finds the total number of meters given the number of centimeters

cm = int(input())

m = cm // 100

print(m)

# divide mandarines per children
children = int(input())
mandarines = int(input())

mandarines_per_child = mandarines // children
mandarines_left = mandarines % children

print(mandarines_per_child, mandarines_left, sep='\n')


# round up, odd number

n = int(input())

print((n + 1) // 2)

# The compartment car has 9 compartments with four seats each. Write a program that determines the compartment number in which the seat with the given number is located (the numbering of seats is continuous, starting from 1).
seat_num = int(input())
seats_comp = 4
compartment = (seat_num + seats_comp - 1) // seats_comp
print(compartment)

# Write a program to convert the value of a time interval specified in minutes into a value expressed in hours and minutes.
# Sample Input 1 :
#150
# Sample Output 1 :
#150 minutes is 2 hours 30 minutes.

minutes = int(input())
min_in_hr = 60

hrs = (minutes // min_in_hr)
mins = minutes % 60

print(minutes, "мин - это", hrs, "час", mins, "минут.")


# !Remember: the last digit of a number is always determined as the number is divided by 10 ( % 10). To remove the last digit from a number, you need to divide it by 10( // 10).

num = 17
a = num % 10
b = num // 10

print(a)
print(b)

num = 754

# last character of the number with % 10
a = num % 10

# first we get rid of the last digit, we then get 75
# next we take the last digit of 75 and remainder %10
b = num // 10 % 10

# get rid of the two last digits with //100
c = num // 100

print(a)
print(b)
print(c)

##### general formula for finding any digit of a number: 
# n is the number of characters
(num // 10 ** (n - i)) % 10

# get last digit
num = 34565

a = (num // 10**0) % 10

print(a)

# Penultimate digit: (num // 10**1) % 10;
# Penultimate digit: (num // 10**2) % 10;
# ....
num = 34565

a = (num // 10**1) % 10
b = (num // 10**2) % 10

print(a)
print(b)

# Second digit: (num // 10**(n - 2)) % 10;
num = 34565
n = 5
a = (num // 10**(n - 2)) % 10

print(a)

# First digit: (num // 10**(n - 1)) % 10
num = 34565
n = 5
a = (num // 10**(n - 1)) % 10

print(a)


#Task 1. Write a program that determines the number of tens and units in a two-digit number.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('first digit =', first_digit)
print('last digit =', last_digit)

#Task 2. Write a program that calculates the sum of the digits of a two-digit number.

num = int(input())
last_digit = num % 10
first_digit = num // 10

print('total of the first and last digit =', last_digit + first_digit)

#Task 3. Write a program that prints the number formed by rearranging the digits of a two-digit number.
num = int(input())
last_digit = num % 10
first_digit = num // 10

print('rearranged =', last_digit * 10 + first_digit)

#Task 4. Write a program into which a three-digit number is entered and which displays its digits (separated by commas).

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(digit1, digit2, digit3, sep=',')

#### Write a program that calculates the sum and product of the digits of a positive three-digit number.
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

total = digit1 + digit2 + digit3
product = (digit1 * digit2)* digit3

print("Сумма цифр =", total)
print("Произведение цифр =", product)


#### Given a three-digit abc, in which all numbers are different. Write a program that prints six numbers formed by rearranging the digits of a given number.
 
#Sample Input 1 :
#123
#Sample Output 1 :
#123
#132
#213
#231
#312
#321

num = int(input())
#a = num // 100
#b = (num // 10) % 10
#c = num % 10

a = (num // 10 ** 2) % 10
b = (num // 10 ** 1) % 10
c = (num // 10 ** 0) % 10

print(a,b,c, sep='')
print(a,c,b, sep='')
print(b,a,c, sep='')
print(b,c,a, sep='')
print(c,a,b, sep='')
print(c,b,a, sep='')


## Write a program to find the digits of a four-digit number.

num = int(input())
a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

#a = (num // 10 ** 3) % 10
#b = (num // 10 ** 2) % 10
#c = (num // 10 ** 1) % 10
#d = (num // 10 ** 0) % 10

print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)

#### A five-digit number is given and stored in the variable n. The variables a, b, c, d, e store:
# a – number of tens of thousands (first digit),
# b – number of thousands (second digit),
# c – number of hundreds (third digit),
# d – number of tens (fourth digit),
# e – number of units (fifth digit).

a = n // 10000
b = n% 10000 // 1000
c = n% 1000 // 100
d = n% 100 // 10
e = n% 10

print('Поэма "Мёртвые души" одна из самых интересных')

a = 17 // (23 % 7)
# remainder first!
b = (34 % a) * 5 - (29 % 4) * 3
print(a * b)


print("*", "*", sep="***************")
print("*", "*", sep="               ")
print("*", "*", sep="               ")
print("*", "*", sep="***************")

## Write a program that reads two integers a and b and displays the square of the sum(a+b)^2
## and the sum of squares a^2+b^2a these numbers.

a = int(input())
b = int(input())

sqr_sum = (a + b)**2
sum_squares = a**2 + b**2

print("Квадрат суммы", a, "и", b, "равен", sqr_sum)
print("Сумма квадратов", a, "и", b, "равен", sum_squares)

### As you know, integers in Python do not have the restrictions that are found in other programming languages. 
# Write a program that reads four positive integers a, b, c, d and displays the value of the expression a^b + c^d.

# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = (a**b) + (c**d)

print(x)


### Write a program that reads a positive integer n, n∈[1 ;9] and displays the value of the number n+nn+nnn.
# Зачем усложнять, если можно упрощать?
# n + 10*n + n + 100*n + 10+n + n = 123*n
n = int(input())

res = 123 * n

print(res)
