##### Nested and cascading conditions #####
# Inside a conditional statement, you can use any Python language instructions, including a conditional statement. We get a nested branch: after one fork, another fork appears during program execution.
if условие1:
    блок кода
else:
    if условие2:
        блок кода
    else:
        if условие3:
            блок кода            
        ...
        
#In the previous lesson, we examined the problem of determining the coordinate quarter of a point. The program can be rewritten using a nested statement: 
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')
        
# Let's consider a program that converts a hundred-point score into a five-point score. To implement it, you need to use a nested conditional operator: 
grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70: 
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)
                

### Cascading conditional operator "elif" ###
# The syntax of a cascading conditional statement is as follows: 

if condition 1:
    code block
elif condition 2:
    code block
...
else:
    code block
    
# if condition 1 false - jumps to elif-block. If that is false, then else

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)
    
# !!!!! else block is optional 
traffic_light_signal = input("Введите сигнал светофора: ")

if traffic_light_signal == "красный":
    print("Стой!")
elif traffic_light_signal == "желтый":
    print("Приготовься...")
elif traffic_light_signal == "зеленый":
    print("Иди!")
    
### Problem solving ###
# Problem 1. Three integers are given. Determine how many of them match. The program should output one of the numbers: 33 (if all match), 22 (if the two match) or 00 (if all numbers are different). 
# Method 1: Using a nested conditional statement. 
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)

# Method 2: Using a cascading conditional statement. 
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)
    
# Method 3: Using the cascading conditional operator and the logical operator or. 
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
    

### Assignments ###
# If Zoom (n) is faster, print "NO"
# If Flash (k) is faster, print "YES"
# If both are same, print "Don't know"
n = int(input()) # Zoom
k = int(input()) # Flash

if n > k:
    print("NO")
elif k > n:
    print("YES")
else:
    print("Don't know")
    
# Write a program that takes three positive numbers and determines the type of triangle whose side lengths are equal to the numbers entered. 
# determine type of triangle
# "Equilateral", "Isosceles", "scalene"
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
    
# Three different integers are given. Write a program that finds the middle number.
# e.g. 67, 100, 54 -> 67
a = int(input())
b = int(input())
c = int(input())

# solution 1
if (a>b and b>c) or (a<b and b<c):
    print(b)
elif (a>b and b<c and a<c) or (a<b and a>c and b>c):
    print(a)
else:
    print(c)
    
# solution 2
#if (b - a) * (c - a) < 0:
#    print(a)
#elif (a - b) * (c - b) < 0:
#    print(b)
#else:
#    print(c)
    
# solution 3
#if a < b < c or a > b > c:
#    print(b)
#elif b < c < a or b > c > a:
#    print(c)
#else:
#    print(a)


## Given the serial number of the month (1, 2,…, 12)( 1 , 2 , … , 12 ) . Write a program that displays the number of days in this month. Assume that the year is not a leap year. 
# not leap year = 365 days (feb = 28 days)
month = int(input())

# if month odd + under 9 and even and above 6
if month == 2:
    print("28")
elif ((month % 2 == 1) and month < 9) or ((month % 2 == 0) and month > 6):
    print("31")
#elif ((month % 2 == 0) and month < 7) or ((month % 2 == 1) and month > 8):
else:
    print("30")
    

## The weight of an amateur boxer is known (integer). It is known that the weight is such that a boxer can be classified into one of three weight categories:

    #Light weight - up to 60 kg (not inclusive);
    #First Half weight - up to 64 kg (not including);
    #Half weight – up to 69 kg (excl.).

weight = int(input())

if weight < 60:
    print("Легкий вес")
elif 60 <= weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")
    
## Write a calculator.
# +, -, *, /. if not this operation print("wrong operator")
# b must be higher than 0, else print "can't divide by 0"
    
a = int(input())
b = int(input())
op = input()

if op == '+':
    total = a + b
    print(total)
elif op == '-':
    total = a - b
    print(total)
elif op == '*':
    total = a * b
    print(total)
elif (op == '/') and b == 0:
    print("На ноль делить нельзя!")
elif (op == '/') and (a > 0 or b > 0):
    total = a / b
    print(total)
else:
    print("Неверная операция")
    
    
##Red, blue and yellow are called primary colors because they cannot be created by mixing other colors. When two primary colors are mixed, a secondary color is obtained:

#    if you mix red and blue, you get purple;
#    if you mix red and yellow, you get orange;
#    If you mix blue and yellow, you get green.

#Write a program that reads the names of two primary colors to mix. If the user enters anything other than “red,” “blue,” or “yellow,” the program should display an error message. Otherwise, the program should print the name of the secondary color that will be the result.

#Input format
#The program receives two lines as input, each on a separate line.

#Output format
#The program should display the resulting mixture color or a “color error” message if the wrong color was entered. 

a = input()
b = input()

if (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
    print(a)
elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
    print("фиолетовый")
elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
    print("оранжевый")
elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
    print("зеленый")
elif (a != 'красный' or 'синий' or 'желтый') or (b != 'красный' or 'синий' or 'желтый'):
    print("ошибка цвета")
    
## Roulette wheel colors ##
# On the roulette wheel, the pockets are numbered from 0 to 36 . Below are the pocket colors:

#    pocket 0 green;
#    1 to 10 red = odd, black = even
#    11 to 18 red = even, black = odd
#    19 to 28 red = odd, black = even
#    29 to 36 red = even, black = odd

# Write a program that reads a pocket number and shows whether the pocket is green, red or black. The program should display an error message if the user enters a number that is outside the range of 00 to 3636 .

# The program should display the color of the pocket or an “input error” message if the entered number is outside the range from 0 to 36.
num = int(input())

if num == 0:
    print("зеленый")
elif 1 <= num <= 10:
    if (num % 2 == 0):
        print("черный")
    else:
        print("красный")
elif 11 <= num <= 18:
    if (num % 2 == 0):
        print("красный")
    else:
        print("черный")
elif 19 <= num <= 28:
    if (num % 2 == 0):
        print("черный")
    else:
        print("красный")
elif 29 <= num <= 36:
    if (num % 2 == 0):
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")
    
    
## Intersection of segments ##
#There are two segments on the number line: [a1; b1][ and 1 ; b 1 ] and [a2;  b2][ a 2 ;   b 2 ] . Write a program that finds their intersection.

#The intersection of two segments can be:

#   - line segment;
#   - point;
#   - empty set.

# Input format
# The input to the program is 4 integers a1, b1, a2, b2, each on a separate line. It is guaranteed that a1<b1 and a2<b2. 

# Output format
# The program should display the boundaries of the segment that is the intersection, or a common point, or the text “empty set.” 

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# a1 < b1 and a2 < b2

if a1 < b1 and a2 < b2:
    

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if b1<a2 or b2>a1:
    print("пустое множество")
elif b1 == a2 or a1 == b2:
    print(b1 or a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 == a2 or b1 == b2:
    print(a1, b1)
    
#####
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# 1
if a1 == a2 and b1 == b2:
    print(a1, b1)
# 2
elif (a1 < a2 < b2 and b1 == a2):
    print(b1)
elif (a2 < a1 < b1 and b2 == a1):
    print(b2)
# 3
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
# 4
elif a1 == a2 and (b1 < b2):
    print(a1, b1)
elif a1 == a2 and (b2 < b1):
    print(a1, b2)
# 6
elif (a2 < a1 and b1 == b2):
    print(a1, b1)
elif (a1 < a2 and b1 == b2):
    print(a2, b1)
# 5
elif (a2 < a1 < b1 < b2):
    print(a1, b1)
elif (a1 < a2 < b2 < b1):
    print(a2, b2)
else:
    print("пустое множество")
