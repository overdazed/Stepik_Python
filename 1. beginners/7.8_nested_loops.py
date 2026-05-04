##### Nested Loops #####

# A nested loop is nested within another loop. 
# A clock is a good example of how a nested loop works. 
# The second, minute and hour hands rotate around the dial. 
# The hour hand moves only 1 step for every 60 steps of the minute hand. 
# And the second hand must make 60 steps for 1 step of the minute hand. 
# This means that for every full revolution of the hour hand (12 steps), 
# the minute hand makes 720 steps.

# Consider a loop that partially models an electronic clock. It shows seconds from 0 to 59:
for seconds in range(60):
    print(seconds)
    
# You can add a variable minutesand nest the loop above inside another loop that repeats 60 times:
for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)
        
# To complete the model, you can add one more variable to count hours:
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)
            
# The innermost loop will do 60 iterations for each iteration of the middle loop. 
# The middle loop will do 60 iterations for each iteration of the outermost loop. 
# When the outermost loop has completed 24 iterations, the middle one has completed 24*60 = 1440 iterations, 
# and the innermost loop will do 24*60*60= 86400 iterations!

# The clock simulation example brings us to several points relevant to nested loops:
# - the nested loop executes all of its iterations for every single iteration of the outer loop;
# - Nested loops complete their iterations faster than outer loops;
# - In order to get the total number of iterations of a nested loop, you need to multiply the number of iterations of all loops.


### Break and continue statements in nested loops ###

# The operator 'break' interrupts the nearest loop in which it is located. 
# Similarly, the operator 'continue' moves to the next iteration of the nearest loop.

for i in range(3):
    for j in range(3):
        print(i, j)
        
# Let's change the code by adding a conditional statement with the operator to the nested loop break:
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)
        
# Let's change the interrupt operator  break to operator continue:

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)
        

### Examples of problem solving ###

# One interesting way to learn about nested loops is to use them to display combinations of characters. Let's look at one simple example. Let's say we want to print stars on the screen as a rectangular table:
******
******
******
******
******
******
******
******
# The star table consists of 8 rows and 6 columns. The code snippet below can be used to print one line of asterisks:
for i in range(6):
    print ( '*', end='')
# In order to complete the entire star table output, we need to run this loop eight times. 
# We can put this loop inside another loop that iterates eight times, as shown below:
for i in range(8):
    for j in range(6):
        print('*', end='')
    print()
# The outer loop does eight iterations. 
# During each iteration of this loop, the inner loop makes 6 iterations. 
# (Note that on line 4, after all lines have been printed, we call the function print(). 
# We must do this in order to advance the screen cursor to the next line at the end of each line. 
# Without this instruction, all stars will be printed on the screen as one long line.)

# Let's look at another example. Let's say you want to print stars in a combination that looks like the star triangle below:
*
**
***
****
*****
******
*******
********

# Let's imagine this combination of asterisks as a combination of rows and columns. 
# There are only eight lines in this combination. 
# The first row has one column. The second line has two columns. 
# The third line has three. And so it continues until the eighth line, which has eight columns.

# 8 lines
for i in range(8):
    # 1. one column
    # 2. two columns
    # 3. three columns
    # 4. ...
    # 8. eight columns
    for j in range(i + 1):
        print('*', end='')
    print()

# -----------------------------------------------------------
## Set in what order the specified nested loop will output pairs of numbers (i, j). 
for i in range(1, 4):
    for j in range(3, 6):
        print(i, j)

## What will the code snippet below show?
for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')
# 455667

## What will the code snippet below show?
counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
        #print(temp)
print(counter)

#1. Initialize a counter variable counter to 0.
#2. Iterate over the range from 99 to 101 (inclusive).
#3. For each number i in this range:
    # - Assign the value of i to a temporary variable temp.
    # - Enter a while loop that continues as long as temp is greater than 0.
        # - Increment the counter variable by 1.
        # - Integer divide temp by 10 (essentially removing the rightmost digit of temp).
#4. Print the value of the counter variable after the loop.

#Let's analyze how the loop behaves for each number in the range:
# - For 99: The while loop will execute twice (temp becomes 9, then 0), incrementing counter by 2.
# - For 100: The while loop will execute three times (temp becomes 10, then 1, then 0), incrementing counter by 3.
# - For 101: The while loop will execute three times (temp becomes 10, then 1, then 0), incrementing counter by 3.

# #So, in total, the counter will be incremented by 2 + 3 + 3 = 8.

# Therefore, the answer is 8, as the code snippet counts the total number of digits in the numbers from 99 to 101, inclusive.

# -------------------------------------------------------------------------------------------------
## Table-1 ##

# Given a natural number n (n≤ 9). 
# Write a program that prints a table of size n×3, 
# consisting of a given number (numbers are separated by one space).

n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
        
# -------------------------------------------------------------------------------------------------
## Table-2 ##

# Given a natural numbern n≤9. 
# Write a program that prints a table of size n×5, where in 'i' the line contains the number i (numbers are separated by one space).

# 3
n = int(input())

# iteration from 1 to n
# 1, 4
for i in range(1, n+1):
    for j in range(5):
        # 1 1 1 1 1
        # 2 2 2 2 2
        # 3 3 3 3 3
        print(i, end=' ')
    print()
    
# -------------------------------------------------------------------------------------------------
## Table-3 ##

# Given a natural number n (n≤9). 
# Write a program that prints an addition table for all numbers from 1 to n (inclusive) according to the example.

# 3
n = int(input())

# iteration from 1 to n
# 1, 4
for i in range(1, n+1):
    # iteration from 1 to 9
    for j in range(1, 10):
        x = i + j
        print(i, '+', j, '=', x)
    print()

# -------------------------------------------------------------------------------------------------
## Star Triangle 🌶️🌶️ ##

# Given an odd natural number n. 
# Write a program that prints an isosceles star triangle with base equal to n according to the example:
*
**
***
****
***
**
*

n= int(input())

for i in range(n//2 + 2):
    print('*' * i)
for j in range(n//2, 0 ,-1):
    print('*' * j)
    
# other
n = int(input())

for i in range(n):
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    for j in range(cur_cnt):
        print("*", end="")
    print()
    
# other
n = int(input())

for i in range(n):
    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    print(cur_cnt * "*")
    
# -------------------------------------------------------------------------------------------------
## Numerical triangle 1 ##

#Given a natural number n. 
# Write a program that prints a numerical triangle as per the example:
1
22
333
4444
55555
...

n = int(input())
# 8 lines
for i in range(1, n+1):

    for j in range(i):
        print(i, end='')
    print()
    
# -------------------------------------------------------------------------------------------------

### Using Nested Loops to Solve Equations ###

# Nested loops can be used to solve equations with multiple variables. 
# Knowing that the solutions (roots) of the equation are natural (integer) numbers, 
# it is easy to write a program containing a nested loop and iterating through all possible values ​​of the variables.


### Problem solving ###

# Problem 1
# Find all pairs of natural numbers (and their number) that are solutions to the equation 12x + 13y = 777.

# Solution 1
# Since by condition the number 'x' and 'y' are natural, then x≤64, y≤59 (at x= 65,12 * 65 = 780, which is more than 777. 
# That's why x≤64, because 'y' cannot be negative by condition; 
# similarly it turns out that y≤59). 
# Let's write a program that iterates through all possible pairs of numbers (x;y) and checks that the condition is met for them 12x+13y=777.
total = 0
for x in range(1, 65):
    for y in range(1, 60):
        if 12 * x + 13 * y == 777:
            total += 1
            print('x =', x, 'y =', y)
print('Total number of natural solutions =', total)


# Problem 2
# Find all pairs of natural numbers (and their number) that are solutions to the equation x^2+y^2+z^2 = 2020.

# Solution 2
# Since by condition the number x, y and z are natural, 
# then x, y, z < \sqrt{2020}≈45. 
# Let's write a program that iterates through all possible triplets of numbers(x; y; z) and 
# checks the condition for them x^2 + y^2 + z^2 = 2020.

total = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Total number of natural solutions =', total)

# ------------------------------------------------------------------------------------
## 12 months ##

# Solve the equation in natural numbers 28n + 30k + 31m = 365.

# Note
# Use a nested loop 'for'. 
# Write down the solution with the smallest value first n.

total = 0
for x in range(1, 14):
    for y in range(1, 13):
        for z in range(1, 12):
            if 28*x + 30*y + 31*z == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Total number of natural solutions =', total)

# ------------------------------------------------------------------------------------
## An ancient problem ##

# Available 100 rubles.
# How many bulls, cows and calves can be bought with all this money, if the price for the 
# bull is 10 rubles, 
# cow 5 rubles, 
# calf 0.5 ruble 
# and need to buy 100 heads of cattle?

# Note
# Use a nested loop 'for'.

total_money = 100  # Общая сумма денег в рублях
price_bull = 10    # Цена быка в рублях
price_cow = 5      # Цена коровы в рублях
price_calf = 0.5   # Цена теленка в рублях

# Перебираем возможные значения быков, коров и телят
for bulls in range(int(total_money // price_bull) + 1):
    for cows in range(int(total_money // price_cow) + 1):
        for calves in range(int(total_money // price_calf) + 1):
            # Проверяем, соответствует ли общая стоимость 100 рублям
            if (bulls * price_bull + cows * price_cow + calves * price_calf == total_money) and (bulls + cows+ calves == total_money):
                print("Количество быков:", bulls)
                print("Количество коров:", cows)
                print("Количество телят:", calves)
                exit()  # Выходим после нахождения первого решения
                

# ------------------------------------------------------------------------------------
## Euler's Sum of Powers Conjecture 🌶️🌶️ ##

# https://stepik.org/lesson/298795/step/13?unit=280622

# Set the upper limit for the numbers
limit = 150

# Iterate through possible values for a, b, c, and d
for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                # Calculate the sum of fifth powers of a, b, c, and d
                sum_of_powers = a**5 + b**5 + c**5 + d**5
                
                # Iterate over possible values for e and check if it's a fifth power
                for e in range(1, 151):
                    if e**5 == sum_of_powers:
                        # Output the solution
                        print("Numbers:", a, b, c, d, e)
                        print("Sum of the numbers:", a + b + c + d + e)
                        # Break out of the innermost loop to avoid unnecessary iterations
                        break


# Set the upper limit for the numbers
limit = 150

# Dictionary to store the sums of fifth powers
sums_of_powers = {}

# Compute and store the sums of fifth powers
for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            for d in range(c, limit + 1):
                sum_of_powers = a ** 5 + b ** 5 + c ** 5 + d ** 5
                sums_of_powers[sum_of_powers] = (a, b, c, d)

# Iterate through possible values for e and check if it's a fifth power
for e in range(1, limit + 1):
    e_power = e ** 5
    if e_power in sums_of_powers:
        a, b, c, d = sums_of_powers[e_power]
        print("Numbers:", a, b, c, d, e)
        print("Sum of the numbers:", a + b + c + d + e)
        break

# ------------------------------------------------------------------------------------
## Numerical triangle 2 ##

# Given a natural number n. 
# Write a program that prints a numerical triangle with height equal to n, according to the example:

n = int(input())

cnt = 0
for i in range(n):
    for j in range(i+1):
        cnt += 1
        print(cnt, end=' ')
    print()
    
# ------------------------------------------------------------------------------------
## Numerical triangle 3 ##

# Given a natural number n. 
# Write a program that prints a numerical triangle with height equal to n, according to the example:

1
121
12321
1234321
123454321
...

n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    for j in range(i-1, 0, -1):
            print(j, end="")
    print()
    

# ------------------------------------------------------------------------------------
## Divisors-1 🌶️ ##

# The program is given two natural numbers as input a and b (a<b). 
# Write a program that finds a natural number from a segment [a;b] 
# with the maximum sum of divisors and the sum of its divisors. 
# If there are several such numbers, print the largest of them.

a = int(input())
b = int(input())

# Initialize variables to store the maximum number and its sum of divisors
max_num = -1
max_sum = -1

# Iterate through each number in the range [a, b]
for cur_num in range(a, b+1):
     # Initialize the sum of divisors for the current number 'cur_num'
    cur_sum = 0
     # Iterate through all numbers from 1 to 'cur_num'
    for j in range(1, cur_num+1):
         # If 'j' is a divisor of 'cur_num', add it to the sum of divisors
        if cur_num % j == 0:
            cur_sum += j
    
    # If the sum of divisors for the current number is greater than or equal to
    # the maximum sum of divisors found so far 
    if cur_sum >= max_sum:
        max_num = cur_num # Update the maximum number
        max_sum = cur_sum # Update the maximum sum of divisors

# Print the maximum number with its sum of divisors
print(max_num, max_sum)

# ------------------------------------------------------------------------------------
## Divisors-2 ##

# A natural number is given as input to the program n. 
# Write a program that displays a graphical representation of the divisibility of 
# numbers from 1 to n inclusive. 
# In each line you need to print the next number and as many “+” symbols as there are divisors for this number.

# A natural number is given as input to the program n.
n = int(input())

# Loop through each number from 1 to n inclusive
for i in range(1, n+1):
    # Initialize a counter for the number of divisors of the current number i
    cnt = 0
    # Loop through each number from 1 to i inclusive to check for divisors of i
    for j in range(1, i+1):
        # Check if j is a divisor of i
        if i%j == 0:
            # If j is a divisor, increment the counter
            cnt += 1
    # Print the current number i followed by '+' symbols representing the number of divisors
    print(i, '+'*cnt, sep='')
    
# ------------------------------------------------------------------------------------
## Digital root ##

# A natural number is given as input to the program n.
# Write a program that finds the digital root of a given number. 
# Digital root of a number n it turns out as follows: 
# if you add all the digits of this number, 
# then all the digits of the found sum and 
# repeat this process until the result is a single-digit number (digit), 
# which is called the digital root of the original number.

n = int(input())

# Continue looping until n is reduced to a single-digit number
while n > 9:
     # Initialize a variable to store the sum of digits
    cnt = 0
    # Loop through each digit of the number
    while n > 0:
        # Extract the last digit of the number
        last_digit = n % 10
        # Add the last digit to the sum
        cnt += last_digit
        # Remove the last digit from the number
        n = n//10
    # Update the value of n with the sum of digits
    n = cnt
# Once the loop exits, n will contain the digital root of the original number
print(n)

# ------------------------------------------------------------------------------------
## Sum of factorials ##

# Given a natural number n. 
# Write a program that prints the value of the 
# sum 1! + 2! + 3! + … + n!.

# Note 1. 
# Factorial of a natural number n, is called the product of all natural numbers from 1 to n, that is
# n! = 1⋅2⋅3⋅…⋅n

n = int(input())

# Initialize a variable cnt to store the total sum of factorials
cnt = 0

# Loop through each number from 1 to n
for i in range(1, n+1):
    
    # Initialize a variable factorial to store the factorial of the current number i
    factorial = 1

    # Calculate the factorial of the current number i
    for j in range(1, i+1):
        factorial *= j
        
    # Add the factorial of the current number to the total sum
    cnt += factorial
    
# Print the total sum of factorials
print(cnt)

# ------------------------------------------------------------------------------------
## Prime numbers ##

# The program is given two natural numbers as input a and b (a<b). 
# Write a program that finds all prime numbers from a to b inclusive.

# Prompt the user to input two natural numbers a and b
a = int(input())
b = int(input())

found_prime = False 
start = a

# Set the starting point of the range
if a < 2:
    start = 2
else:
    a

# Iterate through the range from start to b
for num in range(start, b+1):
    is_prime = True
    
    # Check if the current number is prime
    if num > 1:
        for i in range(2, int(num**0.5)+ 1):
            if num % i == 0:
                is_prime = False
                break
            
    # If the number is prime, print it
    if is_prime:
        if found_prime:
            print(end='')
        print(num)
        found_prime = True

# Print a message if no prime numbers are found
#if not found_prime:
#    print("There are no prime numbers in the specified range.")

#
# Prompt the user to input two natural numbers a and b
a, b = int(input()), int(input())

# Iterate through the range from a to b inclusive
for cur_num in range(a, b + 1):
    # Check if the current number is equal to 1
    if cur_num == 1:
        # If it's equal to 1, skip to the next iteration
        continue
    
    # Iterate through numbers from 2 to the square root of the current number + 1
    for i in range(2, int(cur_num ** 0.5 + 1)):
        # Check if the current number is divisible by any number from 2 to the square root
        if cur_num % i == 0:
            # If it's divisible, break out of the loop
            break
    else:
        # If the loop completes without finding a divisor, the current number is prime, so print it
        print(cur_num)
