##### while loop #####

# 1. Using a while loop to process the digits of a number
# 2. Problem solving

### Processing the digits of a number ###

# When studying integers, we talked about the operation of integer division '//' 
# and the operation of finding the remainder of dividing one integer by another '%'. 
# Using a 'while loop' and two data operations, you can process the digits of a number 
# with an arbitrary number of digits.

# - the result of the operation 'n % 10' is the last digit of the number;
# - the result of the operation 'n // 10' is a number with the last digit removed.
n = int(input())
while n != 0:  # as long as there are numbers in the number
    last_digit = n % 10  # get last digit
    # last digit processing code
    n = n // 10  # remove last digit from number
    

# outputting numbers
# finding a sum
# products of numbers 
# finding the largest or smallest number
# counting numbers that satisfy some condition
# etc.


# Let's write a program that determines whether a number contains the number 7.

num = int(input())
has_seven = False  # flag

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')
    
# ------------------------------------------------------------
## What will the code snippet below show?

num = 12345
product = 1
while num != 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10
    # 12345 % 10 = 5
    # 1 * 5 = 5
    # 12345 // 10 = 1234
    
    # 1234 % 10 = 4
    # 5 * 4 = 20
    # 1234 // 10 = 123
    
    # 123 % 10 = 3
    # 20 * 3 = 60
    # 123 // 10 = 12
    
    # 12 % 10 = 2
    # 60 * 2 = 120
    # 12 // 10 = 1
    
    # 1 % 10 = 1
    # 120 * 1 = 120
    # 1 // 10 = 0
    
    # 0 % 10 = 0
    # 120 * 0 = 0
    # 0 // 10 = 0
    
    # 0 % 10 = 0
    # 
    #print(product)
print(product)


## What will the code snippet below show?
num = 123456789
total = 0
while num != 0:
    last_digit = num % 10 
    # 9
    # 8
    # 7
    if last_digit > 4: 
        # 9 > 4
        # 8 > 4
        # 7 > 4
        # 6 > 4
        # 5 > 4
        # 4 !> 4
        total += 1 
        # total = 1
        # total = 2
        # total = 3
        # total = 4
        # total = 5
    # num = 12345678
    # num = 1234567
    # num = 123456
    # num = 12345
    # num = 1234
    num = num // 10

# print '5'
print(total)

# ------------------------------------------------------------
## Reverse order 1

# A natural number is given. 
# Write a program that displays its numbers in a column in reverse order.
num = int(input())

while num != 0:
    last_digit = num % 10 
    print(last_digit)
    num = num // 10
    
# ------------------------------------------------------------
## Reverse order 2

# A natural number is given. 
# Write a program that reverses the order of the digits of a number.
num = int(input())

while num != 0:
    last_digit = num % 10 
    num = num // 10
    print(last_digit, end='')
#print(last_digit)

# ------------------------------------------------------------
## max and min

# Given a natural number n,(n≥10). 
# Write a program that determines its maximum and minimum digits.
n = int(input())

# counter will check last digit
total = 0
# create max num variable
max_n = 0
# minimum num variable of the highest num possible
min_n = 9 
# if num above 0
while n > 0:
    # get last digit
    total = n % 10
    # when last digit is greater than the max_n digit
    if total > max_n:
        # set it to new biggest counter
        max_n = total 
    # if counter is smaller than the smallest digit
    if total < min_n:
        min_n = total
    # get new last digit
    # e.g. input: 12345
    # 1234
    # 123
    # 12
    # 1
    n = n // 10

print("Максимальная цифра равна", max_n) # print max
print("Минимальная цифра равна", min_n) # print min

# ------------------------------------------------------------
## Together

# A natural number is given. 
# Write a program that calculates:

# - the sum of its digits;
# - the number of digits in it;
# - the product of its digits;
# - the arithmetic mean of its digits;
# - its first digit;
# - the sum of its first and last digits.

num = int(input())

sum_digits = 0
num_of_digits = 0
product = 1
# gets the last digit of input
digit = num%10
while num != 0:
    # gets the last digit
    last_digit = num % 10
    # last dig + last dig ...
    sum_digits += last_digit
    # adds up every loop
    num_of_digits += 1
    # last dig * last dig * ...
    product *= last_digit
    # 1. add up all nums, 2. devide by number of values/digits
    arithm = sum_digits / num_of_digits
    num = num // 10
    # 5678 .. 567 .. 56 .. 5
    
print(sum_digits)
print(num_of_digits)
print(product)
print(arithm)
print(last_digit)
sum_first_last = last_digit + digit
print(sum_first_last)

# ------------------------------------------------------------
## Second digit

# Given a natural number n (n>9). 
# Write a program that determines its second (from the beginning) digit.
# 10 .. 11 .. 12 ..

n = int(input())

while n > 9:
    second_digit = n % 10
    # n = n // 10
    # does no print the last, because one digit number can't be divided by 10!!!
    n //= 10
print(second_digit)

# ------------------------------------------------------------------------
## Same numbers

# A natural number is given. 
# Write a program that determines whether a given number consists of identical digits.

# 888858
num = int(input())

cnt = 0

# check if the num is greater than 10
# because we can't compare just one number
while num // 10 != 0: 
    last = num % 10 # The last digit of the number # 8
    num = num // 10 # a number without the last digit # 888885
    last1 = num % 10 # the remainder of the number without the last digit # 5
    if last1 != last: # if last1 is not last
        cnt += 1 # count up
if cnt > 0: # when counter is more than 0
    print("NO")
else:
    print("YES") # if cnt == 0
    
# ------------------------------------------------------------------------
## Ordered numbers

# A natural number is given. 
# Write a program that determines whether the sequence of its digits, 
# when viewed from right to left, is ordered in non-decreasing order.

n = int(input())

cnt = 0
while n > 9: 
    last = n % 10
    n = n//10
    last1 = n % 10
    if last <= last1:
        cnt += 0 # count up
    else: 
        cnt += 1
if cnt == 0: # when counter is more than 0
    print("YES")
else:
    print("NO") # if cnt == 0