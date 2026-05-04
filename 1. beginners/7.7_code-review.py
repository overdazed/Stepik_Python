##### Code Review #####


### Code review ###

# Code review - checking the source code of a program in order to detect and correct errors and inaccuracies that went unnoticed during initial development. 

# During the code review process the following can be corrected:

# - factual errors;
# - code performance;
# - code readability and code formatting errors.

# The purpose of code review is 'to improve the quality of the program code' and 'improve the programmer's skills'.

# As a rule, code reviews are performed by a programmer with extensive experience.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('code-review.png')
plt.imshow(image)
plt.show()


### Factual errors ###

# Actual errors in the code include errors due to which the code may not work correctly. 
# Essentially, these are errors related to the algorithm that is used in the program to solve the problem.

# Common factual errors include:

# - lack of initial variable initialization;
# - incorrect initialization of the variable;
# - no indentation (in Python, code blocks are indented);
# - incorrect numeric boundary values, for example when using the 'range()';
# - incorrect boundary comparisons (confusion with >, >=or <, <=);
# - confusion of logical operations 'or', 'and' etc.


### Code Performance ###

# In the simplest case, code productivity can be understood as 'how much time the program spends on solving a problem'. 
# When writing a program, the programmer must think about how much time, 'in the worst case', it will take his program to solve the problem.

# Consider a problem that tests a number for primality.

# Version 1: 
# We go through all the numbers from 2 to num-1 and check the divisibility of the number num by i:
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('prime number')
else:
    print('Composite number')
    
# If the program is given a prime number as input num = 1934234249, then it will work approximately 3.59 minutes.

# Version 2:  
# It’s easy to understand that it doesn’t make sense to go through all the numbers from 2 to num - 1. 
# It is enough to check the numbers from 2 to num//2 + 1:

num = int(input())
flag = True

for i in range(2, num//2 + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('prime number')
else:
    print('Composite number')
# 1m 30s

# Version 3: 
# The right boundnum // 2 + 1 of the check can be improved by noting that any composite number has a divisor (other than 1) 
# that does not exceed the square root of the number . 
# Thus, it makes sense to iterate over the divisors from 2 to \sqrt{on one} + 1 
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')
    
# 2.4s

# Version 4: 
# Previous optimizations concerned the case when the number being tested is prime. 
# If the number is composite and we have found its first divisor (other than 1), we interrupt the loop using the operatorbreak:
num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')


### Code readability ###

# We should remember that our code should be easy to read by other programmers. 
# To achieve this, you must adhere to the PEP 8 standard. 
# Pay attention to the following points:

#1. 'indentations and spaces': use 4 spaces per indentation level and never mix tabs and spaces;
#2. 'variable names': use descriptive names for variables (total, counter, product) and follow the lower_case_with_underscores style (lowercase words with underscores);
#3. 'empty lines': additional indentation with empty lines can occasionally be useful to highlight a group of logically related parts of the program: initialization of variables, main algorithm, final check, etc.;
#4. 'Comments': Comments must be complete sentences. And remember, comments that contradict the code are worse than no comments. Always correct comments if you change the code!


### Notes ###

# Note 1:
# Good articles about code review can be read on Habré: 
# https://habr.com/ru/articles/340550/ 
# https://habr.com/ru/articles/342244/

# Note 2: 
# Software errors are often called bugs

# Note 3: 
# All programmers create bugs, especially at the beginning of their career. This is the norm.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
image = mpimg.imread('bug.png')
plt.imshow(image)
plt.show()


# ----------------------------------------------------------------------------------------------

##### Examples #####

# Example 1.
# It was necessary to write a program that prints the symbol A 10 times. You review the following code:
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
print('A')
# Review.
# The above code does the job, but it can be improved. 
# Since the actions in the lines are the same, a loop can be used. 
# Since we know the number of repetitions (iterations), the loop is suitable for us 'for':
for _ in range(10):
    print('A')
    
# Example 2.
# You needed to write a program that should print all numbers from 1 to 100 multiples of 7. 
# You review the following code:
i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
        i += 1
# Review.
# The above code contains a fairly common error: 
# incorrect indentation. 
# Since the loop 'while' is controlled using the variable i, it must be incremented (increased) each iteration. 
# In the code above, it is incremented only if a condition is true i % 7 == 0  that is false for the initial value i = 1. 
# Thus, we get an infinite loop. 
# To fix the error, you need to remove the indentation from the line i += 1:
i = 1
while i < 101:
    if i % 7 == 0:
        print(i)
    i += 1
# In this case, it is better to use a 'for' loop with a step equal to 7.
# This will make the code more visual and reduce the execution time of the program, 
# since there is no need to view and check all numbers for divisibility by 7:
for i in range(7, 101, 7):
    print(i)
    
# Example 3.
# It was necessary to write a program that displays all numbers from 100 to 1 in descending order. 
# You review the following code:
for i in range(1, 100):
    print(101 - i)
# Review.
# The above code contains a fairly common error: 
# an incorrect right 'for' loop boundary. 
# Remember that the right boundary in a 'for' loop is always non-inclusive. 
# Thus, to correct the error, you need to replace the number 100 with 101:
for i in range(1, 101):
    print(101 - i)
# In this case, it is better to use a 'for' loop with a step equal to -1:
for i in range(100, 0, -1):
    print(i)
    
# Example 4.
# You needed to write a program that finds the sum of all odd numbers from 1 to 1000. 
# You review the following code:
a = 1
for i in range(1, 1000):
    if i % 2 == 1:
        a = a + 1
print(a)
# Review. 
# The above code contains fairly common errors:
#1. incorrect initialization of variable a;
#2. invalid right 'for' loop boundary;
#3. incorrectly recorded operation of accumulating a sum value.
a = 0
for i in range(1, 1001):
    if i % 2 == 1:
        a = a + i
print(a)
# To improve the readability of the code, change the name of the variable 'a' to 'total' and use the extended assignment operator:
total = 0
for i in range(1, 1001, 2):
    total += i
print(total)

# Example 5.
# It was necessary to write a program that calculates the factorial of a number.
# You review the following code:
n = input()
a = 0
for i in range(n):
    a = a * i
print(a)
# Review.
# The above code contains fairly common errors:
#1. no conversion of a text string to an integer;
#2. incorrect initialization of variable 'a'; 
#3. incorrect operation with iteration boundaries: the variable i takes values ​​from 0 to n - 1.
n = int(input())
a = 1
for i in range(1, n + 1):
    a = a * i
print(a)
# To improve the readability of the code, change the variable name 'a' to 'factorial' and use the extended assignment operator:
n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# !!! The module 'math' has a function 'factorial()' that calculates the factorial of a number. 
# Therefore, instead of implementing your own version, it is much more correct and convenient to use a ready-made one.

# ----------------------------------------------------------------------------------------------
## Code review-1 🌶️🌶️ ##

# A sequence of 10 integers (each on a separate line). 
# You need to write a program that displays the 'number of non-negative numbers' in a sequence and their product. 
# If there are no non-negative numbers, you need to display “NO”. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 4 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

count = 0
# error 1, before p = 0
p = 1
# error 2, before range(1, 10)
for i in range(1, 11):
    x = int(input())
    # error 3, before x > 0
    # the 0 is a non-negative number
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    # error 4, before print(x)
    print(count)
    print(p)
else:
    print('NO')
    
# ----------------------------------------------------------------------------------------------
## Code review 2 🌶️🌶️ ##

# A sequence of 10 integers (each on a separate line). 
# It is known that the entered numbers in absolute value do not exceed 10^6.
# We need to write a program that displays the sum of all negative numbers in a sequence 
# and the maximum negative number in the sequence. 
# If there are no negative numbers, you need to display “NO”. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 5 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note
# If necessary, you can add the necessary lines of code.

# error 1 > does not exceed 10^6, before max_n = 0
mx = -10**6 - 1
s = 0
# error 2, before range(11)
for i in range(10):
    x = int(input())
    if x < 0:
        # error 3, before sum_all_negative = n
        s += x
    # error 4 THE BIGGEST NEGATIVE NUM, before x > 0
    if x < 0 and x > mx:
        mx = x
# error 5
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')
    
# ----------------------------------------------------------------------------------------------
## Code review-3 ##

# A sequence of 7 integers (each on a separate line). 
# You need to write a program that calculates and displays the sum of all even numbers in a sequence or 0,
# if there are no even numbers in the sequence. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 4 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note
# If necessary, you can add the necessary lines of code.

# error 1, before s = 1
s = 0
# error 2, before range(1, 7)
for i in range(1, 8):
    # error 3, before input()
    n = int(input())
    # error 4, before i
    if n % 2 == 0:
        s = s + n
print(s)

# ----------------------------------------------------------------------------------------------
## Code review-4 🌶️🌶️ ##

# A natural number is received for processing. 
# We need to write a program that displays the maximum digit of a number that is a multiple of 3. 
# If the number does not contain multiple digits 3, you need to display “NO” on the screen. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 5 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# Note 1
# Number 0 divisible by any natural number.

# Note 2
# You can add the required lines of code if necessary.


# A natural number is received for processing.
n = int(input())

# error, before max_digit = n % 10
max_digit = 0
# additional line
cnt = 0
while n > 0:
    # last digit
    digit = n % 10
    # if digit is divisible by 3
    if digit % 3 == 0:
        # additional line
        cnt += 1
        # error, before <
        if digit >= max_digit:
            # error, before digit = max_digit
            max_digit = digit
    # error, before n = n % 10
    n = n // 10
# error, before if max_digit == 0:
if cnt == 0:
    print('NO')
else:
    print(max_digit)
    
# ----------------------------------------------------------------------------------------------
## Code review-5 🌶️ ##

# A natural number is received for processing. 
# You need to write a program that displays its first (most significant) digit. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 2 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

n = int(input())
while n > 0:
    # error 1, before n%= 10
    digit = n%10
    n = n // 10
# error 2, before print(n)
print(digit)

# ----------------------------------------------------------------------------------------------
## Code review-6 ##

# A natural number is received for processing. 
# You need to write a program that displays the product of the digits of the entered number. 
# The programmer was in a hurry and wrote the program incorrectly.

# Find all the errors in this program (there are exactly 3 of them). 
# It is known that each error affects only one line and can be corrected without changing other lines.

# error 1, before n = input()
n = int(input())
# error 2, before n%10
product = 1
# error 3, before >= 10
while n > 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)