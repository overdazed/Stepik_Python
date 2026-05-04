##### common scenarios #####

# 1. Quantity counting
# 2. Calculating sum and product
# 3. Exchange of variable values
# 4. Signal marks
# 5. Definition of maximum and minimum
# 6. Extended assignment operators ( +=, -=, //=etc.)


### Quantity counting ###

# Often we need our programs to count how many times something has happened.
# For example, a video game might count the number of times a character turns, 
# or a math program might count how many numbers have a certain property.
# The key to counting is using 'the counter variable'. 

# Let's write a program that reads 10 numbers and determines how many of them are greater 10.
# counter variable
counter = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        # everytime it is true, counter+1 = new counter
        counter = counter + 1

print('Было введено', counter, 'чисел, больших 10.')

# let's also count the number of zeros among the entered numbers.
counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

# count the number of numbers from a range [1;100], whose square ends in 4.

# cnt
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
        
print(counter)


### Calculating sum and product ###

# calculating the sum. 
# For example, a video game must count the sum of points. 
# In this case, the initial value of the variable will be equal to 0, 
# and then it will increase by a certain number of points earned, say by 10. 

score = 0
...
score = score + 10

total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна',  total)

# 'Calculating the amount' consists of two steps:
# 1. Creating an adder variable and giving it its initial value: total = 0;
# 2. Increase the adder variable by the required number: total = total + num.

# Let's write a program that calculates the sum of natural numbers from 1 to 100:
total = 0
for i in range(1, 101):
    total = total + i

print('Сумма равна', total)

# let's write a program that requests 10 integers and finds their average:
total = 0
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10
print('Среднее значение равно', average)

# When calculating the product, we set the initial value of the 'multiplier variable equal to 1', in contrast to the adder, where it is equal 0.


### Exchange of variable values ###

# Very often we need to exchange the values ​​of two variables xand y. Novice programmers sometimes write code like this:
x = y
y = x

# However it doesn't work. 
# Let's assume that x = 3 and y = 5. 
# The first line will assign x the value to the variable 5 which is correct, 
# however the second line will set the value of the variable y to 5, since the value x is already equal 5. 
# To solve the problem we can use a temporary variable:
temp = x
x = y
y = temp

# Such code is written in almost all programming languages. However, there is an easier way in Python. We can write like this:
x, y = y, x
# As a result of executing such code, Python will swap the values ​​of the variables x and y places.


### Signal marks ###

# A signal label (flag) can be used when one part of the program needs to know what is happening in another part of the program.

# Let's write a program that determines that a natural number is prime:
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  #  if the original number is divisible by anything other than 1 and itself
        flag = False

if num == 1:
    print('This is "one", it is neither simple nor compound') 
elif flag == True:
    print('Prime number')
else:
    print('Composite number')
# The initial value of the flag variable is True, which indicates that the number is prime. 
# Then we iterate through all the numbers from 2 up to num - 1(inclusive). 
# If one of these values ​​happens to be a divisor of the number num, then the number num is composite and we set the value of the flag False. 
# Once the loop is completed, we check whether the flag is set True or not. 
# If so, we know that the divisor was not found and the number is prime. 
# Otherwise the number is composite.

# Flag variables can be named more meaningfully. In the case of checking a number for primality, the name of the flag variable could be 'is_prime'.


### Maximum and minimum ###
# Finding the largest or smallest value in a certain sequence of numbers is also a common problem in programming.

# Let's write a program that reads 10 'positive numbers' and finds the largest number among them.
largest = 0
for _ in range(10):
    num = int(input())    
    if num > largest:
        largest = num

print('The largest number is: ', largest)


# We set the initial value of the variable largest to 0. 
# Next the program reads 10 numbers, and if any of them is greater than the current value largest, reassigns it.

# Let's write a program that reads 10 numbers (not necessarily positive) and finds the largest among them:
largest = int(input())  # take the first number as the maximum
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)

# To find the smallest value of the sequence, change the inequality sign (>) to the opposite one (<). 
# In this case, the variable name 'largest' should be replaced with 'smallest'.


### Extended Assignment Operators ###

counter = counter + 1
# On the right side of the assignment operator, 1 is added to the variable 'counter'. 
# The resulting result is then assigned to the variable 'counter', replacing the original value. 
# Essentially this line of code adds 1 to 'counter'. 
# We saw another example of such an instruction when calculating the amount:
total = total + num
# This instruction assigns the value of an expression 'total + num' to a variable 'total'. 
# As a result of executing this instruction, the number 'num' is added to the value 'total'.


## Various assignment statements (per instruction x = 6)

# Instructions  What is she doing                       The value of x after the instruction
# x = x + 4	    Adds 4 to x	                            10
# x = x - 3	    Subtracts 3 from x	                    3
# x = x * 10	Multiplies x by 10	                    60
# x = x / 4	    Divides x by 4	                        1.5
# x = x // 4	Divides x by 4	                        1
# x = x % 4	    Finds the remainder when divided x by 4	2


# Python offers 'extended assignment operators' for convenience 
total = total + num
total += num

counter = counter + 1
counter += 1


# Operator	Usage example	Equivalent
# +=	    x += 5	        x = x + 5
# -=	    x -= 2	        x = x - 2
# *=	    x *= 10	        x = x * 10
# /=	    x /= 4	        x = x / 4
# //=	    x //= 4	        x = x // 4
# %=	    x %= 4	        x = x % 4


### Notes ###

# Note 1: 
# you can swap the values ​​of three or more variables.
a, b, c, d = b, c, d, a

# Note 2: 
# Very often signal marks are called flag.

# Note 3: 
# Since Python has built-in functions 'max()' and 'min()', giving such names for the maximum and minimum values ​​is not very good. 
# It is much better to use the names 'largest' and 'smallest' or 'mx' and 'mn'.

# Note 4. 
# The sum of numbers from 1 to 100 can be calculated without a loop:
sum = ((1+100)/2)*100
print(sum)

# ---------------------------------------------------------------
## What will the code snippet below show?
num1 = 4
num2 = 6
num1 += num2 
num1 *= num1
print(num1)

## What will the code snippet below show?
total = 0
for i in range(1, 6):
    total += i # i + total = total
    # 1
    # 1 + 2 = 3
    # 3 + 3 = 6
    # 6 + 4 = 10
    # 10 + 5 = 15
print(total) # 15

## What will the code snippet below show?
total = 0
for i in range(1, 6):
    total += i
    print(total, end="") #1361015
# da print im loop ist

# ---------------------------------------------------------------
## Amount of numbers

# The program receives two integers as input a and b (a <= b). 
# Write a program that counts the number of numbers in the range from a to b(inclusive), the cube of which ends in  4 or 9.

# line 42
a = int(input())
b = int(input())

cnt = 0
for i in range(a, b+1):
    cube = i**3
    if (cube%10 == 4) or (cube%10 == 9):
        cnt += 1
print(cnt)

# ---------------------------------------------------------------
## Sum of numbers

# A natural number is given as input to the program n, and then n integers, each on a separate line. 
# Write a program that calculates the sum of the numbers entered (not including the number itself) n).

# in:
# 5
# 3
# 2
# 1
# 0
# -1

# 5
n = int(input())

total = 0
# 1. n = 5
for i in range(n):
    # every loop, new number
    num = int(input())
    # 3 + 0 = 3
    # 2 + 3 = 5
    # 5 + 1 = 6
    # 6 + 0 = 6
    # 6 + -1 = 5
    total += num
print(total)

# ---------------------------------------------------------------
## Asymptotic approximation

# A natural number is given as input to the program n. Write a program that calculates the value of an expression

# (1 + (1/2) + (1/3) + ... + (1/n)) - ln(n).

from math import *

# Taking input from the user
n = int(input())

# Initializing the sum of the series
series_sum = 0
    
# Calculating the sum of the series 1/1 + 1/2 + 1/3 + ... + 1/n
for i in range(1, n+1):
    series_sum += 1/i
    # 0 + 1/1
    # 1/1 + 1/2 = 
    # (1/1 + 1/2) + 1/3
    # ...
    
# Calculating the natural logarithm of n
# ln(n)
ln_n = log(n) # math lib
    
# Calculating the value of the expression
expression_value = series_sum - ln_n
    
# Printing the result
print(expression_value)

# ---------------------------------------------------------------
## Sum of numbers 2

# A natural number is given as input to the program n. 
# Write a program that calculates the sum of those numbers from 1 to n (inclusive), 
# the square of which ends in 2, 5 or 8.

# Get input n from user
n = int(input())

# Initialize total to 0
total = 0

# Run a loop from 0 to n with variable i
for i in range(1, n+1):
    # Check if i squared ends in 2, 5 or 8
    # if (i**2)%10 in [2, 5, 8]:
    if (i**2)%10 == 2 or (i**2)%10 == 5 or (i**2)%10 == 8:  
        # If yes, add i to total
        total += i

# After the loop, print 0 if total is still 0, otherwise print the value of total
if total == 0:
    print(0)
else:
    print(total)
    
# ---------------------------------------------------------------
## Factorial

# A natural number is given as input to the program n. 
# Write a program that calculates n!.

# n! = 1*2*3* ... * n

n = int(input())

total = 1
for i in range(n):
    # count from 1
    cnt = i+1
    total = total * cnt
    # 1 * 1 = 1
    # 1 * 2 = 2
    # 2 * 3 = 6
    #print(cnt)
print(total)
# ________
n = int(input())

res = 1
for i in range(1, n+1):
    res *= i # res = res * i
    # 1 * 1 = 1
    # 1 * 2 = 2
    # 2 * 3 = 6
print(total)

# ------------------------------------------------------------
## No zeros

# Write a program that reads 10 numbers and prints the product of non-zero numbers.

# When calculating the product, we set the initial value of the 'multiplier variable equal to 1'
# in contrast to the adder, where it is equal 0.
total = 1
for _ in range(10):
    num = int(input())
    if num != 0:
        total = total * num
print(total)

# ------------------------------------------------------------
## No zeros

# A natural number is given as input to the program n. 
# Write a program that calculates the sum of all its divisors.

n = int(input())

total = 0
for i in range(1, n+1):
    if n%i == 0:
        total = total + i
        # 10%1 = 0 -> 1
        # 10%2 = 0 -> 2
        # 10%3 = 1
        # 10%4 = 2
        # 10%5 = 0 -> 5
        # 10%6 = 4
        # 10%7 = 3
        # 10%8 = 2
        # 10%9 = 1
        # 10%10 = 0 -> 10
# 1 + 2 + 5 + 10
print(total)

# ------------------------------------------------------------
## Alternating sum

# A natural number is given as input to the program n. 
# Write a program to calculate the sign-alternating sum:

# 1 - 2 + 3 - 4 + 5 - 6 + ... + (-1)^n+1 * n

n = int(input())

total = 0
for i in range(1, n+1):
    # when number is even then
    if i%2 == 0:
        total = total - i
    # if number is off
    elif i%2 != 0:
        total = total + i
print(total)

# ------------------------------------------------------------
## Largest numbers

# A natural number is given as input to the program n, 
# and then n different natural numbers in a sequence, each on a separate line. 
# Write a program that prints the largest and second largest numbers in a sequence.

n = int(input())

# highest num
max1 = 0
# second highest num
max2 = 1
for i in range(1, n+1):
    # each loop prompt a num
    num = int(input())
    ### for highest ###
    # if num higher than max1
    if num > max1:
        # then max1 is new max2
        max2 = max1
        # the entered num is now max1
        max1 = num
    ### for second highest ###
    elif num > max2:
        max2 = num
print(max1)
print(max2)

# ------------------------------------------------------------
## Only even numbers

# Write a program that reads a sequence from 10 integers and 
# determines whether each of them is even or not.

cnt = 0
for i in range(1, 11):
    n = int(input())
    if (n%2 == 0):
        cnt = cnt + 1
if cnt == 10:
    print("YES")
else:
    print("NO")
    
# ------------------------------------------------------------
## Fibonacci Sequence

# Write a program that reads a natural numbernnand displays the firstnnFibonacci sequence numbers.

n = int(input())

a = 1
b = 0

for i in range(n):
    c = a + b
    a = b
    b = c
    # c = 1 + 0
    # 1 = 1
    # 1 = 1
    
    # c = 1 + 1
    # 1 = 1
    # 1 = 1
    
    # c = 1 + 
    print(b, end=" ")
