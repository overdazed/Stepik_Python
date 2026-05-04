##### break, continue, else #####

### Loop interrupt operator break ###

# Sometimes it is necessary to terminate a loop prematurely. 
# The operator 'break' interrupts the nearest loop 'for' or 'while'.
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:        #if the original number is divisible by anything other than 1 and itself
        flag = False
        break               #stop the loop if we encounter a divisor of a number

if flag:  # equivalent to if flag == True:
    print('Prime number')
else:
    print('Composite number')
    
# !!! The loop break operator 'break' allows us to speed up programs because we get rid of unnecessary iterations.


# Let's write a program using a 'for loop' that reads 10 numbers and adds them up 
# until it finds a negative number. 
# In this case, the execution of the loop is interrupted by the command 'break':
result = 0
for i in range(10):
    num = int(input())
    if num < 0:
        break
    result += num
print(result)

# !!! The loop interrupt operator break is convenient in conjunction with signal marks: when, after checking a certain condition, it makes no sense for us to continue executing the loop.

# Let's write a program that determines whether the number entered by the user contains the digit 7.
num = int(input())
number = num
flag = False
while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break        #interrupt the loop, since the number is guaranteed to contain the number 7
    num //= 10

if flag:  #equivalent to if flag == True:
    print('Number', number, 'contains the number 7')
else:
    print('Number', number, 'does not contain the number 7')
# As soon as we encounter the number 7, we change the value of the signal label and 
# break the loop using the operator 'break'. 
# We may not interrupt the loop prematurely, but wait for its natural completion 
# (condition 'num != 0', that is, all digits of the number have been processed), 
# but in this case we will do unnecessary work, and if the number is very large, 
# the program will run slower.


### Infinite loops ###

# In previous lessons we talked about a loop that has no way to end and called it 'an infinite loop'. 
# The easiest way to create an infinite loop in Python is to write the following code:

while True:
    print('Python is awesome!')
    
# The result of executing this code will be an infinite number of lines of text:
#Python is awesome!
#Python is awesome!
#.
#.
#.
#Python is awesome!
#Python is awesome!
#Python is awesome!

# You might think that infinite loops don't make sense, but that's not entirely true. For example, you could write a program that starts and runs, constantly accepting service requests. The program code for such a program might look like this:

while True:
    query = get_new_query()     #We receive a new request for processing
    query.process()             #processing the request
    
# Sometimes using an infinite loop can make the code more readable. 
# A simpler approach might be to terminate the loop based on conditions 
# within the loop body rather than conditions in its head:

while True:
    if условие 1:  #condition for stopping the loop
        break
    ...
    if условие 2:  #one more condition to stop the loop
        break
    ...
    if условие 3:  #one more condition to stop the loop
        break

# In cases like this, where there are multiple reasons for loop termination, 
# it is often easier to isolate them from several different places rather than 
# trying to specify all the termination conditions in the loop header.

# !!! Important:  Infinite loops can be very useful. 
# Just remember that you have to make sure that the loop will be interrupted at some point 
# so that it doesn't actually become infinite.


### Continue operator ###

# Another standard looping idiom is skipping individual elements while iterating. 
# The operator 'continue' allows you to move to the next iteration of the 'for' loop 
# or 'while' until all commands in the loop body have completed.

# Let's write a program that prints all the numbers from 1 to 100, except for the numbers 7, 17, 29 and 78.
for i in range(1, 101):
    if i == 7 or i == 17 or i == 29 or i == 78:
        continue  # переходим на следующую итерацию
    print(i)
    

### Notes ###

# Note 1:
# The operator 'break' interrupts the execution of the nearest loop, 
# not the program, that is, the command immediately following the loop will be executed.

# Note 2:
# representation of operators 'break' and 'continue' looks like:
while 'condition':
    break

while 'condition':
    continue

# -------------------------------------------------------------------------------------------------------
## What will the code snippet below show?
for i in range(10):
    print(i, end='*')
    if i > 6:
        break

## What will the code snippet below show?
i = 100
while i > 0:
    if i == 40:
        break
    print(i, end='*')
    i -= 20

## What will the code snippet below show?#
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')
    
## What will the code snippet below show?
result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
    # 1
    # 1 + 3 = 4
    # 4 + 5 = 9
    # 9 + 7 = 16
    # 16 + 9 = 25
print(result)

## What will the code snippet below show?
mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
   # 1*1 = 1
   # 1*3 = 3
   # 3*5 = 15
   # 15*7 = 105
print(mult)

# -------------------------------------------------------------------------------------------------------
## Least divisor

# The number is given as input to the program 'n > 1'. 
# Write a program that prints its smallest difference from 1 divider.
n = int(input())

for i in range(2, n+1):
    #x = n%i
    #print(n, i, x)
    #print(x)
    if n%i == 0:
        print(i)
        break

# -------------------------------------------------------------------------------------------------------
## Follow the rules

# A natural number is given as input to the program n. 
# Write a program that prints numbers from 1 to n inclusive except for:

# - numbers from 5 to 9 inclusive;
# - numbers from 17 to 37 inclusive;
# - numbers from 78 to 87 inclusive.

n = int(input())

for i in range(1, n+1):
    if (5 <= i <= 9) or (17 <= i <= 37) or (78 <= i <= 87):
        continue
    else:
        print(i)
        
# -------------------------------------------------------------------------------------------------------
##### The else block in loops #####

# Python allows an optional block 'else' at the end of 'while' and 'for' loop. 
# This is a unique feature of Python that is not found in most other programming languages. 
# The syntax for this construction is as follows:

while 'condition':
    code block 1
else:
    code block 2

# or

for i in range(10):
    code block 1
else:
    code block 2

# 'code block 2', specified in 'else', will be executed when the loop is completed.

# “How can this be useful?” 
# After all, we can do the same thing by placing 'code block 2' immediately after the 'while' loop or for without else:
while 'condition':
    code block 1
code block 2

# or

for i in range(10):
    code block 1
code block 2


### What is the difference? ###

# If the word 'else' is not in the loop description, 'code block 2' will be executed after the loop ends, no matter what. 
# If the word 'else' is present, it 'code block 2' will be executed only if the loop ends normally. 
# Normal loop termination means its completion without using an interrupt operator 'break'.
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('The cycle is complete.')
# This loop is repeated until the condition is true 'n > 0'. 
# Since the loop has completed normally, the block of code in the instruction 'else' will be executed.

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('The cycle is complete.')
# This loop terminates prematurely with an interrupt statement 'break', 
# so the block of code in the statement 'else' will not be executed.


# Let's write a program that determines whether the number entered by the user contains the number 7. 
# Instead of the program code written earlier:
num = int(input())
n = num
flag = False
while n != 0:
    last = n % 10
    if last == 7:
        flag = True
        break        #interrupt the loop, since the number is guaranteed to contain the number 7
    n //= 10

if flag is True:
    print('Number', num, 'contains the number 7')
else:
    print('Number', num, 'does not contain the number 7')
    
##
num = int(input())
n = num
while n != 0:
    last = n % 10
    if last == 7:
        print('Number', num, 'contains the number 7')
        break
    n //= 10
else:
    print('Number', num, 'does not contain the number 7')
    
    
### Notes ###

# Note 1: 
# The operator 'continue' does not affect the execution of the block 'else' in loops.

# Note 2: 
# A block 'else' in loops is often used to handle missing elements.

# Note 3: 
# A block of code 'else' in loops is not very common in practice. 
# However, if you find a situation where it is 'else' justified, then don't hesitate to use it. 
# This can add clarity to your code!

# -------------------------------------------------------------------------------------------------------
## Will the block of code 'else' in the code snippet below be executed?
n = 0
while n < 10:
    n += 2
    print(n)
else:
    print('The cycle is complete.')
# Yes

## Will the block of code 'else' in the code snippet below be executed?
n = 0
while n < 10:
    n += 2
    if n == 8:
        break
    print(n)
else:
    print('The cycle is complete.')
# No

## Will the block of code 'else' in the code snippet below be executed?
n = 0
while n < 10:
    n += 2
    if n == 7:
        break
    print(n)
else:
    print('The cycle is complete.')
# Yes
