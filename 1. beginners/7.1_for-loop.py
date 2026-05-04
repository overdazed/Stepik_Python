##### 7.1 for loop #####

### There are two main types of loops in Python:

# - cycles repeated a certain number of times (forcounting loops);
# - cycles that repeat until a certain event occurs (conditional loopswhile).

## for loop ##

# The loop  for works great if we know in advance how many repetitions (iterations) we need to do.

# The loop structure 'for' in Python looks like this:

for loop_variable_name in range(number_of_repetitions):
    code block

# Let's look at the code that will print 10 times the word "Hello":

for i in range(10):
    print('Привет')
    
# In previous lessons we read several numbers using several commands 'input()'.
# Using a 'for loop', you can read and process as many numbers as you like.

# This program reads 5 numbers and displays their squares on the screen along with an explanatory caption. 
# Because the second and third lines are indented, Python assumes that this is the body of the loop that is being executed 5 times. 
# The fourth line is not indented, so it is not part of the loop and will only be executed once, after the loop has completed.

for i in range(5):
    num = int(input())
    print("The square of your number is:", num * num)

print("The cycle is complete")

## Examples of using for loops ##

# That is, the program will first print the symbols А and  В, then the symbols C and D five times, 
# and then print the symbol E once. 
# The body of the loop consists of two lines: 
# the fourth and fifth; they are the ones that will be repeated.

print("A")
print("B")
for i in range(5):
    print("C")
    print("D")
print("E")

# A program can have any number of loops. 
# For example, if we first want 5 times the symbol С, and then 5 times symbol D, we can use 2 cycles:

print('A')
print('B')
for i in range(5):
    print('C')
for i in range(5):
    print('D')
print('E')

## Note 1: Executing the body of a loop once is called loop iteration.

# ---------------------------------------------------------------------------------------
# Python is awesome

# Write a program that outputs the words "Python is awesome!" (we quote) 10 times.
for sentence in range(10):
    print('Python is awesome!')
    
# ---------------------------------------------------------------------------------------
# Repeat after me

# A sentence is given and the number of times it must be repeated. Write a program that repeats this sentence the required number of times.
sentence = input()
times = int(input())

for i in range(times):
    print(sentence)

# ---------------------------------------------------------------------------------------
# Character sequence

# Write a program that uses exactly three for loops to print the following sequence of characters:

for x in range(6):
    print('AAA')
for x in range(5):
    print('BBBB')
print('E')
for x in range(9):
    print('TTTTT')
print('G')

# ---------------------------------------------------------------------------------------
# Star rectangle

# A natural number is given as input to the programnn.

# Write a program that prints a star rectangle with dimensionsn \times 19n×19.

n = int(input())
star = '*'*19

for i in range(n):
    print(star)
# ---------------------------------------------------------------------------------------

### Loop variable ###
# Let's take another look at the basic loop structure for:

for loop_variable_name in range(number_of_repetitions):
    code block
    
# It is not entirely clear what the loop variable is for and how it works.
#e.g.
for i in range(10):
    print(i)

# Python sets the value of the loop variable  i = 0.
# Each time we repeat the body of the loop, Python increments the value of the variable by 1.
# Since the loop variable iis incremented by 1 each time, it can be used to keep track of the iteration number we are at in the iterative process.
for i in range(10):
    print(i, '-- Привет')
    
## !! If we want to start with 1, then we can write the code:

for i in range(10):
    print(i + 1, '-- Привет')
    
# ----------------------------------------------------------------
### Loop Variable Names ###

# In programming, the letters are usually used for loop variables. i j k
# The following two programs are absolutely identical.
for i in range(10):
    print(i)
for number in range(10):
    print(number)
    
# !!!  If a loop variable is not used in the loop body, use an underscore instead _.
for _ in range(5):
    print('Python - awesome!')
    
# -----------------------------------------------------------------
## Repeat after me

# Write a program that reads one line of text and outputs 10 lines, numbered 0 to 9, each with the specified line of text.
text = input()

for i in range(10):
    print(i, text)
    
# -----------------------------------------------------------------
## Number square

# A natural number is given as input to the programnn. Write a program that for each of the numbers from00tonn(inclusive) displays the phrase: “The square of [number] is [number]” (without quotes).

from math import *

n = int(input())

for i in range(n+1):
    print("Квадрат числа", i,"равен", int(pow(i, 2)))
    
# -------------------------------------------------------------------
## Star triangle
# A natural number is given as input to the programn \, (n \ge 2)n(n≥2)– leg of a right isosceles triangle.

# Write a program that prints a star triangle as shown in the example.

n = int(input())

#leg = n*(n>=2)

for i in range(n):
    print((n-i)*'*')
    
# -------------------------------------------------------------------
## Population

# The program is given three natural numbers as input.m, \, p, \, nm,p,n:

# m: starting number of organisms;
# p: average daily increase in %;
# n:number of days for reproduction.

# Write a program that predicts the population size of organisms. The program should output the population size for each day starting from 1 and ending n-th day.

# starting number of organisms
m = int(input())
# average daily increase in %
p = float(input())
# number of days for reproduction
n = int(input())

# beginnt mit Tag 1
for i in range(1, n+1):
    # zuerst das was eingegeben wurde,
    # deswegen ist print oben
    print(i, m)
# population = population * (1 + prozent/100)
# 25 wird zu 1.25
# 120 * 1.25 -> 150
    m = m * (1 + p/100)