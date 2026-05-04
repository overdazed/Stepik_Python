## The first index in a string value is ##
# 1
# -1
## 0
# длина строки минус один 


## The last index in a string value is  ##
## line length minus one
# 1
# 0
# 99 


## If you try to use an index that is outside the range of the string value, then ##
# nothing will happen - the invalid index will be ignored
## an IndexError will occur
# a ValueError will occur
# the string value will be erased and the program will continue running 

## Which operator determines whether one string value is contained within another? ##
## in
# ==
# contains
# is_in 


## Which string method returns the index of the first occurrence of a substring in a string? ##
# first_index_of()
# locate()
## find()
# index_of() 


## Which string method returns a copy of a string value with all leading whitespace characters removed? ##
## lstrip()
# remove()
# rstrip()
# strip_leading() 

## Which string method returns a copy of a string value with all leading and trailing whitespace characters removed? ##
# rstrip()
# clean()
# remove_whitespace()
## strip() 


## Which string method returns a copy of a string value with all leading and trailing whitespace characters removed? ##
# rstrip()
# clean()
# remove_whitespace()
## strip()


## Which string method returns true if the string value contains only letters and has at least one character? ##
## isalpha()
# alpha()
# isletters()
# alphabetic()

## Which string method returns true if the string value contains only numbers and has at least one character? ##
##  isdigit()
# numeric()
# digit()
# isnumber() 

## What will the code snippet below show? ##
name = 'джо'
print(name.lower())
print(name.upper())
print(name)

# ------------------------------------------------------------------------------------
## Complete the code below so that the program outputs the length of the string s. ##
s = 'Python rocks!'
print(len(s))

## Complete the code below so that the program outputs the fourth character of the line s. ##
s = 'Python rocks!'
print(s[3])

## Complete the code below so that the output of the program is the characters of the string swith 2nd on 5th inclusive. ##
s = 'Python rocks!'
print(s[1:5])

## Complete the code below so that the output of the program is: swithout leading or trailing whitespace characters. ##
s = '    Python rocks!     '
print(s.strip())

## Complete the code below so that the output of the program is: sin capital letters (upper case). ##
s = 'Python rocks!'
print(s.upper())

## Complete the code below so that the output of the program is: sin which the “o” symbol is replaced by the “@” symbol. ##
s = 'Python rocks!'
print(s.replace('o', '@'))

### Every third ###
## A line of text is given as input to the program. Write a program that removes from it all characters with indices that are multiples of 33 , that is, symbols with indices 0, 3, 6, .... ##
s = input()
filtered_s = ""

for i in range(len(s)):
    if i%3 != 0:
        filtered_s += s[i]

print(filtered_s)

### Replace me completely ###
## A line of text is given as input to the program. Write a program that replaces all occurrences of a digit 1 of word «one». ##
s = input()

for i in s:
    x = s.replace('1', 'one')

print(x)

### Delete me completely ###
## A line of text is given as input to the program. Write a program that removes all occurrences of the "@" symbol. ##
s = input()

print(s.replace('@', ''))

### Second occurence ###
## A line of text is given as input to the program. Write a program that prints the index of the second occurrence of the letter "f". If the letter "f" appears only once, print the number −1− 1 , and if it does not occur even once, print the number −2− 2 . ##
s = input()  
    
if s.count('f') == 1:
    print(-1)
elif s.count('f') >= 2:
    print(s.find('f', s.find('f')+ 1))
else:
    print(-2)

### Coup ###
## The input to the program is a line of text in which the letter “h” appears at least twice. Write a program that returns the original string and reverses the sequence of characters between the first and last occurrence of the letter "h". ##
s = input()

first = s.find('h')
last = s.rfind('h')

print(s[:first+1] + s[last-1:first:-1] + s[last:])
