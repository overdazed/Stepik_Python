##### 7.2 The for loop: range function #####
## range() function with one parameter ##

# Let's look at the program code:
for i in range(10):
    print('Привет', i)
# The value that we indicate in parentheses for the function range()indicates the number of iterations of the loop, with the variable itaking sequential values:  0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

# the function range(n) generates a sequence of numbers from 0 to n-1, and the loop  forsequentially iterates through this sequence.


## Overloading range() with two parameters ##
# If we want to start the sequence not with 0, but with some other number, then we can use a function overload range() that takes two parameters.
# For example, calling the function range(1, 5)will generate a sequence of numbers  1, 2, 3, 4.
# If we need numbers from 1 to 5 inclusive, then we use range(1, 6).

#Thus:

# - range(n): creates a sequence of numbers 0, 1, 2, 3, ..., n - 1;
# - range(n, m): creates a sequence of numbers n, n + 1, n + 2, ..., m - 2, m - 1.

# Let's write a program that displays those numbers from the interval [100;999], which end in 7.
for i in range(100, 1000):  # sorting through numbers from 100 to 999
    if i % 10 == 7:         # use the remainder of division by 10 to get the last digit
        print(i)
        

## Overloading range() with 3 parameters ##

# What if we want to generate a sequence of numbers 5, 10, 15, 20, 25?
# three parameters: range(n, m, k)

# The first parameter - start of the sequence
# the second parameter - the stop of the sequence
# the third –  the number generation step

# range(start, stop, step)

# range(1, 10, 2)
# 1, 3, 5, 7, 9

# range(5, 30, 5)
# 5, 10, 15, 20, 25

# Let's write a program that prints all even numbers from the interval [56;170].
for i in range(56, 171, 2):
    print(i)

for i in range(56, 171):
    if i % 2 == 0:
        print(i)
    

## Negative generation step ##

# We can specify a negative generation step, which will generate a decreasing sequence.
# In case of a negative step, we must ensure that the start of the sequence (first parameter) is greater than the end of the sequence (second parameter).

# range(20, 16, -1)
# 20, 19, 18, 17

# range(20, 10, -3)
# 20, 17, 14, 11

for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!!!')


## Examples of using the range() function ##

# Calling a function  	 Sequence of numbers   
# range(10)	             0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# range(1, 10)	         1, 2, 3, 4, 5, 6, 7, 8, 9
# range(3, 7)	         3, 4, 5, 6
# range(7, 3)	         empty sequence
# range(2, 15, 3)	     2, 5, 8, 11, 14
# range(9, 2, -1)	     9, 8, 7, 6, 5, 4, 3
# range(3, 10, -2)	     empty sequence


## Notes ##

# Note 1. The function range() can take from one to three parameters: range(n), range(n, m), range(n, m, k)
# - the first parameter is the start of the sequence (inclusive);
# - the second parameter is the stop sequence (not inclusive);
# - the third parameter is the step size.

# Note 2: The function range() can only generate integers, including negative ones.

# Note 3: The step size cannot be zero. The following code:

for i in range(1, 10, 0):
    print(i)
    
# ------------------------------------------------------------------------------------------

## What sequence of numbers will the function call give you range(8)?
# 0, 1, 2, 3, 4, 5, 6, 7

## What sequence of numbers will the function call give you  range(1, 8)?
# 1, 2, 3, 4, 5, 6, 7

## What sequence of numbers will the function call give you  range(3, 11, 2)?
# 3, 5, 7, 9

## What sequence of numbers will the function call give you  range(10, 0, -2)?
# 10, 8, 6, 4, 2

## How many iterations will the loop make?
for _ in range(1, 6):
   print('Python rocks!')
# 5

# --------------------------------------------------------------------
## Number sequence 1
# Given two integers m and n (m ≤ n). Write a program that prints all the integers from m to n inclusive.
m = int(input())
n = int(input())

for i in range(m, n+1):
    print(i)
    
# --------------------------------------------------------------------
## Number sequence 2
# Given two integers m and n. 
# Write a program that prints all the integers from m to n inclusive in ascending order, 
# if m<n, or in descending order otherwise.

m = int(input())
n = int(input())

if m < n:
    for i in range(m, n+1):
        print(i)
elif m > n:
    for i in range(m, n-1, -1):
        print(i)
elif m == n:
    print(m)
    
# --------------------------------------------------------------------
## Number sequence 3
# Given two integers m and n (m > n). 
# Write a program that prints all odd integers from m to n inclusive in descending order.

m = int(input())
n = int(input())

if m > n:
    if (m%2 == 0):
        m = m-1
        for i in range(m, n-1,-2):
            print(i)
    else:
        for i in range(m, n-1,-2):
            print(i)
else:
    print("nahuiiii")
    
# --------------------------------------------------------------------
## Number sequence 4
# Given two natural numbers m and n (m ≤ n). 
# Write a program that prints all the integers from m to n inclusive, satisfying at least one of the conditions:
# - a multiple of a number 17;
# - number ends in 9;
# - a multiple of a number 3 and 5 simultaneously.

m = int(input())
n = int(input())

for i in range(m, n+1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif (i % 3 == 0 and i % 5 == 0):
        print(i)
        
# --------------------------------------------------------------------
## Multiplication table
# Given a natural number n. 
# Write a program that displays the multiplication table by n (from 1 to 10 inclusive).

n = int(input())

for i in range(1, 11):
    m = n * i
    print(n, 'x', i, '=', m)
    