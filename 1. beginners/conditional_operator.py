### if-else statement ###
# In Python, condition testing is done using the keyword if.
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
    
# The program asks the user to enter text and checks the result of the input. If the entered text is equal to the string "Python", then displays the text to the user:

# A colon (:) at the end of a statement line tells the Python interpreter that a block of commands if follows. The command block includes all indented lines below the instruction line, up to the next unindented line.

if "condition":
    "block of code"
    
## In the new program, we handle two cases at once: if the condition is true (the user entered “Python”), and if the condition is false (the user entered anything except “Python”).    
answer = input('Какой язык программирования мы изучаем?')

if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')
    
if "condition":
    "block of code"
else:
    "block of code"
    
    
### Comparison Operators ###
# Assign operator
=
# The assignment operator (=) assigns values ​​to variables:
num = 1992
s = 'I love Python'

# Conditional operator
==
#Python uses double equals (==) to test whether two elements are equal. Like this:
if answer == 'Python':
    ...

if name == 'Gvido':
    ...

if temperature == 40:
    ...
    
    
## 6 Basic Comparison Operators
if x > 7	If x greater than 7
if x < 7	If x less than 7
if x >= 7	If x greater than or equal to 7
if x <= 7	If x less than or equal to 7
if x == 7	If x equals 7
if x != 7	If x not equal 7

num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'less than', num2)
if num1 > num2:
    print(num1, 'greater than', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'equals', num2)
if num1 != num2:
    print(num1, 'does not equal', num2)
    

## Comparison chains ##
# comparison operators can be chained
a == b == c
1 <= x <= 10

# check if age is in the range of 3 to 6
age = int(input())
if 3 <= age <= 6:
    print('You are a kid')
    
# check if three numbers are the same
if a == b == c:
    print('same numbers')
else:
    print('not same numbers')
    

## Transivity ##
#The equality operator is transitive. This means that if a == b and b == c, then it follows that a == c.
# Order relation: if a>b and b>c, then a>c;
# Parallelism of lines: if a||b and b||c, then a||c;
# Divisibility: if a/b and b/c, then a/c.

## The inequality operator (!=), unlike the equality operator (==), is intransitive.
#That is, from the fact that it does not follow a != bat b != c all that a != c. Indeed, if your name is different from the neighbor on the left and not the same as the neighbor on the right, then there is no guarantee that both neighbors will not have the same names.

# Thus, the following code does not check at all for the fact that all three variables are different:
if a != b != c:
    print('числа не равны')
else:
    print('числа равны')
    
##### Problem solving #####
# check if string is 'Python'
word = input()

if word == 'Python':
    print('ДА')
else:
    print('НЕТ')
    
# does the number have the same two digits?
num = int(input())

last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')
    
# how many even numbers did you input?
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1

print(counter)


#Which code fragments correctly determine whether the number contained in the variable is even or odd i?
# even
if i % 2 == 0:
    print(i, 'чётное')
else:
    print(i, 'нечётное')

#odd
if i % 2 != 0:
    print(i, 'нечётное')
else:
    print(i, 'чётное')
    
    
### Check if passwort is correct ###
pw1 = input()
pw2 = input()

if pw1 == pw2:
    print("Пароль принят")
else:
    print("Пароль не принят")
    
# Write a program that determines whether a number is even or odd.
num = int(input())

if num % 2 == 0:
    print("even")
else:
    print("odd")
    
#Write a program that checks that for a given four-digit number the following relation holds: the sum of the first and last digits is equal to the difference of the second and third digits.
# e.g. 1614 -> 1+4 = 6-1 
num = int(input())

#a = (num // 10 ** 3) % 10
#b = (num // 10 ** 2) % 10
#c = (num // 10 ** 1) % 10
#d = (num // 10 ** 0) % 10

a = num // 1000
b = (num // 100) % 10
c = (num // 10) % 10
d = num % 10

if a+d == b-c:
    print("ДА")
else:
    print("НЕТ")
    

#Write a program that determines whether a user is allowed to access an Internet resource or not.
#e.g. 16 -> Access denied
# 18 -> Access allowed

age = 18

if age >= 18:
    print("accept")
else:
    print("no")
    
    
#Write a program that determines whether three given numbers (in the given order) are consecutive terms of an arithmetic progression.
a = int(input())
b = int(input())
c = int(input())

if a-b == b-c:
    print("YES")
else:
    print("NO")
    
#Write a program that determines the smaller of two numbers.
a = int(input())
b = int(input())

if a > b:
    print(b)
else:
    print(a)
    
#Write a program that determines the smallest of four numbers.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<=b and a<=c and a<=d:
    print(a)
elif b<=a and b<=c and b<=d:
    print(b)
elif c<=a and c<=b and c<=d:
    print(c)
else:
    print(d)
    
#Write a program that, based on the user’s age entered, tells which age group he belongs to:
age = int(input())

if age <= 13:
    print("детство")
elif age > 13 and age <= 24:
    print("молодость")
elif age > 24 and age <= 59:
    print("зрелость")
else:
    print("старость")
    
#Write a program that reads three numbers and calculates the sum of only positive numbers.
a = int(input())
b = int(input())
c = int(input())

if (a < 0):
    a = 0
if (b < 0):
    b = 0
if (c < 0):
    c = 0
print(a + b + c)

##### Logical operators #####

# and — logical multiplication;
# or - logical addition;
# not - logical negation.

## and
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))

if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# The operator andcan combine an arbitrary number of conditions:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')

if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# Truth Table "and"
# As the table shows, for the value of an expression with an operator to be true, both (all) conditions combined by it and must be true .
#  a	  b	   a and b
#False	False	False
#False	True	False
#True	False	False
#True	True	True

## and
# The operator 'or' is also used to combine conditions. However, unlike 'and', to execute a block of code it is enough to satisfy at least one of the conditions.
# Access will be allowed if at least one of the conditions is met.
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

# Truth Table "or"
# at least one condition of the operator must be true
#  a	  b	    a or b
#False	False	False
#False	True	True
#True	False	True
#True	True	True

# !!!!!!!!!!!
# A Boolean expression  X and Y is true if both values X ​​and Y are true.
# A logical expression  X or Y is true if at least one of the values  X​ ​is Y true.

#We can use both logical operators at the same time:
#This code verifies that the students are twelve years of age and are at least in school.77th class and live in Moscow or St. Petersburg.

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')

if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
## "not"
# The operator not allows you to invert (i.e. replace with the opposite) the result of a logical expression.

age = int(input('Сколько вам лет?: '))

if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
#is completely equivalent to the code:
age = int(input('Сколько вам лет?: '))

if age >= 12:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# Truth table for "not"

# a	    not a
#False	True
#True	False


### execution priority
# 1. not
# 2. and
# 3. or

if age >= 7 and age <= 9:
    ...
#is completely equivalent to the code:
if 7 <= age <= 9:
    ...
# !!!! The last option is preferable.


### Problem solving ###

# Task 1. Write a program that determines whether a given natural number is three-digit.
num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('the number has three digits')
else:
    print('the number dont have three digits')
    
# Task 2. Write a program that checks that all three digits of a natural three-digit number are distinct.
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('number consists of different digits')
else:
    print('number has the same digits')
    
# Task 3. Write a program that, based on the coordinates of a point not lying on the coordinate axes, determines the number of the coordinate quarter in which it is located.
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')
    
#                   y
#                   ^
#                   |
#                   |
#   2 quarter       |   1 quarter
#                   |
#                   |
#----------------------------------------> x
#                   |
#                   | 
#   3 quarter       |   4 quarter
#                   |
#                   |

c = 6

if not (c <= 10):
    print('true')
else:
    print('false')
    

#Write a program that accepts an integerxxand determines whether the given number belongs to the specified interval. 
# 0 - 16
num = int(input())

if 0 <= num <= 16:
    print("Принадлежит")
else:
    print("Не принадлежит")
    
#Write a program that accepts an integerxxand determines whether the given number belongs to the specified intervals.
# under and equal -3
# abover and equal 7
num = int(input())

if num <= -3 or num >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")
# or
n = int(input())
if not (-3 < n < 7):
    print('Принадлежит')
else:
    print('Не принадлежит')
    
    
# Write a program that accepts an integerxxand determines whether the given number belongs to the specified intervals.
# -29 - -2
# 8 - 25
num = int(input())

if (-29 <= num <= -2) or (8 <= num <= 25):
    print("is in interval")
else:
    print("is not in interval")
    
# Let's call a number beautiful if it is four-digit and divisible by77or at1717. Write a program to determine whether the entered number is a beautiful number. The program should output "YES" if the number is beautiful, or "NO" otherwise.

num = int(input())

if (1000 <= num <= 9999) and ((num % 7 == 0) or (num % 17 == 0)):
    print("YES")
else:
    print("NO")
    
#Write a program that takes three positive numbers and determines whether a non-degenerate triangle with those sides exists.
# a + b > c
# a + c > b
# b + c > a

# e.g. 5, 2, 3 -> NO
# e.g. 3, 4, 6 -> YES

a = int(input())
b = int(input())
c = int(input())

if ((a+b) > c) and ((a+c)>b) and ((b+c)>a):
    print("YES")
else:
    print("NO")
    
# Write a program that determines whether a given year is a leap year. If the year is a leap year, then print "YES", otherwise print "NO".
# A year is a leap year if its number is a multiple of 4, but not a multiple 100, or if it is a multiple 400.
year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
    

# Given two different squares of a chessboard. Write a program that determines whether a rook can get from the first square to the second in one move. The program receives four numbers as input from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. The program should output “YES” if the rook can move from the first square to the second one, or “NO” otherwise.
# Four numbers from 1 to 8.
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")
    
    
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

#even-even / odd-odd => white square

#even-odd / odd-even => black square

#black
if ((a1%2==0 and b1%2==0) and (a2%2==1 and b2%2==1)):
    print("YES")
elif ((a1%2==0 and b1%2==1) and (a2%2==1 and b2%2==0)):
    print("YES")
else:
    print("NO")
    
#-----
# turm
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 == a2 or b1 == b2:
    print("YES")
else:
    print("NO")
    
    
if a1 + b1 == a2 + b2 or b1 - a1 == b2 - a2:
    print('YES')
else:
    print('NO')