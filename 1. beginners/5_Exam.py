##### 1. #####
# Beginning of the century

# Write a program that determines whether a year with a given number ends with two zeros. If the year is ending, print "YES", otherwise print "NO".
# 1. Input: 2000
# 1. Output: YES
# 2. Input: 1999
# 2. Output: NO

year = int(input())

if year % 100 == 0:
    print("YES")
else:
    print("NO")
    
# ----------------------------------------------
##### 2. #####
# Chess board

# Two squares of a chessboard are given. Write a program that determines whether the given cells have the same color or not. If they are painted the same color, then print the word “YES”, and if they are painted in different colors, then print “NO”.
# 1. Input: 
#1
#1
#2
#6
# 1. Output: YES
# 2. Input:
#2
#2
#2
#5
# 2. Output: NO

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 + a2 + b1 + b2) % 2 == 0:
    print('YES')
else:
    print('NO')
    
# ------------------------------------------------
##### 3. #####
# Girls only

#The football team recruits girls from 10 to 15 years old inclusive. Write a program that queries the age and gender of an applicant using the gender symbols m (for male) and f (for female) and determines whether the applicant is eligible to join the team or not. If the applicant is suitable, then print “YES”, otherwise print “NO”.
# 1. Input: 
#10
#f
# 1. Output: YES
# 2. Input:
#11
#m
# 2. Output: NO
age = int(input())
sex = input()

if (10 <= age <= 15) and sex == 'f':
    print("YES")
else:
    print("NO")

#-----------------------------------------------------
##### 4. #####
# Roman numerals

# Write a program that reads an integer and prints its corresponding Roman numeral. If the number is out of range1-101−10, then the program should display the text “error”.

# The table shows Roman numerals for numbers from11before1010.

#Number	Roman numeral
#  1	     I
#  2	     II
#  3	     III
#  4	     IV
#  5         V
#  6	     VI
#  7	     VII
#  8	     VIII
#  9	     IX
#  10	     X

num = int(input())

if (1 <= num <= 10):
    if num == 1:
        print("I")
    elif num == 2:
        print ("II")
    elif num == 3:
        print ("III")
    elif num == 4:
        print ("IV")
    elif num == 5:
        print ("V")
    elif num == 6:
        print ("VI")
    elif num == 7:
        print ("VII")
    elif num == 8:
        print ("VIII")
    elif num == 9:
        print ("IX")
    elif num == 10:
        print ("X")
else:
    print("error")
    
# ------------------------------------------------
##### 5. #####
# YES or NO that is the question

#Write a program that takes a number as input and, depending on the conditions, displays the text “YES” or “NO”.

#Conditions:

#if the number is odd, then output “YES”;
#if the number is even in the range from 2 to 5 (inclusive), then print “NO”;
#if the number is even in the range from 6 to 20 (inclusive), then print “YES”;
#if the number is even and greater than 20, then print “NO”.

num = int(input())

if num % 2 == 0:
    if 2 <= num <= 5:
        print('NO')
    elif 6 <= num <= 20:
        print('YES')
    elif num > 20:
        print('NO')
else:
    print('YES')

# ---------------------------------------------------
##### 6. #####
# Bishop move#

#Given two different squares of a chessboard. Write a program that determines whether a bishop can get from the first square to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. The program should output “YES” if the bishop’s move from the first cell can get to the second, or “NO” otherwise.

#Sample Input 1 :
#4 
#4 
#5 
#5
#Sample Output 1 :
#YES

#Sample Input 2 :
#4 
#4 
#5 
#4
#Sample Output 2 :
#NO

#Sample Input 3 :
#4 
#4 
#5 
#3
#Sample Output 3 :
#YES

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

# 1. the sum is the same -> 8=8
# 2. the indifference is the same
if a1 + b1 == a2 + b2 or b1 - a1 == b2 - a2:
    print('YES')
else:
    print('NO')
    
# -------------------------------------------------------------
##### 7. #####
# Knight's move

#Given two different squares of a chessboard. Write a program that determines whether a knight can get from the first square to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. The program should output “YES” if the knight’s move from the first cell can get to the second, or “NO” otherwise.

#Sample Input 1 :
#1
#1
#8
#8
#Sample Output 1 :
#NO

#Sample Input 2 :
#2
#4
#3
#2
#Sample Output 2 :
#YES

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 + b1 + a2 + b2) % 2 != 0 and a1 != a2 and b1 != b2:
    print('YES')
else:
    print('NO')
    
# ---------------------------------------------------------
##### 8. #####
# Queen move

# Given two different squares of a chessboard. Write a program that determines whether the queen can get from the first square to the second in one move. The program receives as input four numbers from 1 to 8 each, specifying the column number and row number first for the first cell, then for the second cell. The program should output “YES” if the queen’s move from the first cell can get to the second, or “NO” otherwise.

#Sample Input :
#1
#1
#2
#2
#Sample Output :
#YES

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if (a1 == a2 or b1 == b2) or (a1 + b1 == a2 + b2 or b1 - a1 == b2 - a2):
    print("YES")
else:
    print("NO")