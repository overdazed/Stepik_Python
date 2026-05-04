##### while loop #####

# There are two main types of loops:
#- cycles repeated a certain number of times ('for' counting loops);
#- loops that repeat until a certain event occurs (conditional 'while' loops)

# until a certain event occurs, and the number of iterations in this case is simply impossible to estimate in advance. 
# And this is where the 'while' loop comes to the rescue.

while 'condition':
    code block (body of loop)

# prints 10 times 'Hello'
i = 0
while i < 10:
    print('Hello')
    i += 1

for i in range(10):
    print('Hello')
    
# Let's write a program that reads numbers and prints their squares 
# until it is entered −1. 
# With this formulation of the problem, we cannot use a cycle for, 
# since we do not know how many numbers will precede the number −1.

num = int(input())
while num != -1:
    # print squared number
    print('The square of your number is:', num * num)
    # count next number
    num = int(input())
    
    
### for vs. while ###

# We can always replace the for loop with a while loop. 
# The following two programs print numbers from 0to 100:

# for
# In the first loop, the variable i sequentially takes values ​​from 0 to 100.
for i in range(101):
    print(i)

# while
# we had to create a variable ourselves iand give it an initial value
i = 0
while i < 101:
    print(i)
    #increase the value of the variable i by 1, 
    #which is done automatically in the case of a for loop
    i += 1
    
# Let's write a program that prints all the numbers that are multiples of 3 using a for loop and while:
#for
for i in range(0, 100, 3):
    print(i)

#while
i = 0
while i < 100:
    print(i)
    i += 3
    
#!!! If the number of iterations is not known in advance, then it is necessary to use a loop whileand only it. !!!#


### Read data to stop value ###

# Often when solving while loop problems, we read data until the user enters some value, 
# which is called a stop value. 
# Let's write a program that reads numbers and finds their sum until the user enters the word 'stop':
text = input()
total = 0
while text != 'stop':
    total += int(text)
    text = input()

print('The sum of the values are', total)


### Endless cycle ###

# Except in rare cases, the while loop must always contain the ability to terminate.
# That is, something in the loop must make the condition being tested false. 
# If a loop has no way of ending, then it is called an 'infinite loop'.

# Example of an infinite loop:
i = 0
total = 0
while i < 10:
    total += i


### Notes ###

# Note 1: 
# A while loop gets its name from the nature of its operation: 
# it performs some task as long as a condition is true. 
# The word while in English means just “for now.”

# Note 2: 
# A while loop is called a loop with 'a precondition' because the execution of the loop body is preceded by a condition check 
# (the condition is checked first, and only then the loop body is executed).

# Note 3: 
# Executing the body of a loop once is called loop 'iteration'.

# Note 4: 
# The while loop may not be executed even once. 
# For example, the following code:
i = -1
while i > 0:
    print('Hello world!')
# will not output text because the condition i>0 is false to begin with.

# Note 5: 
# The graphical representation of the while loop looks like this:
while 'condition':
    code block
    
# Note 6: 
# A condition in a while loop, as in a conditional operator 'if', can contain logical operations 'or', 'and', 'not'.


# ------------------------------------------------------------------------------------------
## When does the while loop check its condition: 
# before or after it iterates?
before

## How many times does the message “Python awesome!” will be printed in the code snippet below?
count = 10
while count < 1:
    print('Python awesome!')
# 0

## How many times does the message “Python awesome!” will be printed in the code snippet below?
count = 1
while count < 10:
    print('Python awesome!')
    count += 1
# 9

## How many times does the message “Python awesome!” will be printed in the code snippet below?
count = 1
while count < 10:
    print('Python awesome!')
# infinitely many times

## What number should be written instead of the ellipsis so that the loop is executed exactly 7 times?
i = 5
while i <= ...:
    print('Python awesome!')
    i += 1
# 11

## What will the code snippet below show?
i = 7
a = 5
while i < 11:
    a = a + i
    i = i + 2
    # 12 = 5 + 7
    # 9 = 7 + 2
    
    # 21 = 12 + 9
    # 11 = 9 + 2
print(a)

# ------------------------------------------------------------
## Till the end 1

# The input to the program is a sequence of words, each word on a separate line.

# Let's write a program that reads numbers and finds their sum until the user enters the word 'stop':
# total = 0
text = input()
total = ''
while text != 'END':
    total = total + text + '\n'
    text = input()

print(total)

# oder
text = input()
while text != 'END':
    print(text)
    text = input()

# ------------------------------------------------------------
## Till the end 2

#The input to the program is a sequence of words, each word on a separate line. The end of the sequence is the word END  or end  (in capital or small letters, without quotes). Moreover, the words “ END ” and “ end ” themselves are not included in the sequence, only symbolizing its ending. Write a program that prints the members of a given sequence.
# and
text = input()
while text != 'КОНЕЦ' and text !='конец':
    print(text)
    text = input()

# ------------------------------------------------------------
## Number of members

# The input to the program is a sequence of words, each word on a separate line. The end of the sequence is one of three words: stop , enough , enough  (in small letters, without quotes). These words themselves are not included in the sequence, only symbolizing its ending. Write a program that prints the total number of terms of a given sequence.
text = input()
cnt = 0
while not (text == 'стоп' or text =='хватит' or text =='достаточно'):
    # print(text)
    text = input()
    cnt = cnt +1
print(cnt)

# ------------------------------------------------------------
## While we're sharing

# The input to the program is a sequence of integers divisible by 7, 
# each number on a separate line. 
# The end of the sequence is any number that is not divisible by 7 
# (this number itself is not included in the sequence, only symbolizing its end). 
# Write a program that prints the members of a given sequence.

inp = int(input())

while inp%7 == 0:
    print(inp)
    inp = int(input())

# ------------------------------------------------------------
## Sum of numbers

# The input to the program is a sequence of integers, each number on a separate line. 
# A sign of the end of a sequence is any negative number, although it is not included in the sequence itself. Write a program that prints the sum of all terms of a given sequence.

# 1. input first
n = int(input())
cnt = 0

# 2. if first input is greater then 0, then..
# 5. if the new number is greater than 0, begin loop again 
while n >= 0:
    # 3. 0 + first = cnt
    cnt = cnt + n
    # 4. ask for next number and 
    n = int(input())
# 6. if num negative, then print cnt
print(cnt)

# ------------------------------------------------------------
## Number of fives

# The input to the program is a sequence of integers from 1 to 5, characterizing the student’s grade, each number on a separate line. 
# The end of the sequence is any non-positive number or a number greater 5. 
# Write a program that prints the number of fives.

# 1. input
n = int(input())

cnt = 0
# if number 1-5, go ahead
# if number under 1 or over 5, end loop and print
# 2. if input is between 1-5
while 1 <= n <= 5:
    # 3. if n is 5
    if n == 5:
        # 4. cnt + 1
        cnt = cnt + 1
    # 5. get new number
    n = int(input())
# print the count of the numer 5
print(cnt)
# 1, 4, 5, 3, 4, 5 -> 2

# ------------------------------------------------------------
## Pay the Witcher with a minted coin

# Everyone knows that a witcher is capable of defeating any monster, but his services will not come cheap.
# In addition, the witcher does not accept banknotes, he only accepts minted coins.
# In the world of the Witcher there are coins with denominations 1, 5, 10, 25.
# Write a program that determines the minimum number of minted coins to be paid to the witcher.

n = int(input())

cnt = 0
# 1. wenn Zahl nicht negativ
while n > 0:
    # 2. Wenn Zahl größer/gleich 25 ist,
    # input - 25 und counter + 1
    while n >= 25:
        cnt += 1
        n = n-25
    # 3. Wenn Zahl größer/gleich 10 ist,
    # input - 10 und counter + 1
    while n >= 10:
        cnt += 1
        n = n-10
    # 4. Wenn Zahl größer/gleich 5 ist,
    # input - 5 und counter + 1
    while n >= 5:
        cnt += 1
        n = n-5
    # 4. Wenn Zahl größer/gleich 1 ist,
    # input - 1 und counter + 1
    while n >= 1:
        cnt += 1
        n = n-1
print(cnt)