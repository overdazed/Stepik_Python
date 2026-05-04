##### Strings #####

### Methods and functions ###

# We are already familiar with some built-in functions: min(),  max(),  len(),  int(),  float() etc. 
# A method is a specialized function that is closely associated with an object. 
# Like a function, a method is called to perform a separate task, 
# but it is called on a specific object and “knows” about its target object at run time.

# Thus: a method is a function applied to an object. In this case, to the line. 
# The method is called as object.method(parameter).

# For example,  s.find('e') this is applying  s a method  find with one parameter  to a string 'e'.

# Methods of the string data type can be divided into three groups:

# 1. Register conversion;
# 2. Search and replace;
# 3. Classification of symbols.


### Case conversion ###

# Methods in this group perform case conversion for strings.


## capitalize() method ##
# The method capitalize()returns a copy of the string sin which the first character is uppercase and all other characters are lowercase.
s = 'foO BaR BAZ quX'
print(s.capitalize())
# Foo bar baz qux

# Characters that are not letters of the alphabet remain unchanged. The result of executing the following code:
s = 'foo123#BAR#.'
print(s.capitalize())
# Foo123#bar#.

## swapcase() method ##
# The method swapcase()returns a copy of the string sin which all uppercase characters are converted to lowercase characters and vice versa.
s = 'FOO Bar 123 baz qUX'
print(s.swapcase())
# foo bAR 123 BAZ Qux

## title() method ##
# The method title() returns a copy of the string swith the first character of each word converted to uppercase.
s = 'the sun also rises'
print(s.title())
# The Sun Also Rises

# This method uses a fairly simple algorithm: it does not try to distinguish between important and unimportant words and does not handle abbreviations and apostrophes. 
# The result of executing the following code:
s = "what's happened to ted's IBM stock?"
print(s.title())
# What'S Happened To Ted'S Ibm Stock?

## lower() method ##
# The method lower()returns a copy of the string sin which all characters are lowercase.
s = 'FOO Bar 123 baz qUX'
print(s.lower())
# foo bar 123 baz qux

## upper() method ##
# The method upper()returns a copy of the string sin which all characters are uppercase.
s = 'FOO Bar 123 baz qUX'
print(s.upper())
# FOO BAR 123 BAZ QUX

# !!!! One very important note about methods in this category is that they do not change the original string. 
# If you want to change the string s, you need to write the code:  
# s = s.lower(). 
# In fact, here you are creating a completely different object in the computer’s memory, it’s just with the old name s.

# ------------------------------------------------------------------------------------
## What will the code snippet below show? ##
s = 'i Learn Python language'
print(s.capitalize())

## What will the code snippet below show? ##
s = 'i LEARN Python LAnguaGE'
print(s.lower())

## What will the code snippet below show? ##
s = 'i LEARN Python LAnguaGE'
print(s.lower())

## What will the code snippet below show? ##
s = '$12344%^$#@!'
print(s.lower())

## What will the code snippet below show? ##
s1 = 'a'
s2 = s1.upper()
print(s1, s2)

## What will the code snippet below show? ##
s = 'i LEARN Python LAnguaGE'
print(s.upper())

## What will the code snippet below show? ##
s = 'i LEARN Python LAnguaGE'
print(s.swapcase())

# ------------------------------------------------------------------------------------
## Capital letters ##
# The input to the program is a string consisting of the person’s first and last name, separated by one space. 
# Write a program that checks that the first and last names begin with a capital letter.
s = input()
r = s.title()

if s == r:
    print('YES')
else:
    print('NO')

# ------------------------------------------------------------------------------------
## sWAP cASE ##
# A string is given as input to the program. 
# Write a program that changes the case of characters, in other words, replace all lowercase characters with uppercase ones and vice versa.
s = input()
print(s.swapcase())

# ------------------------------------------------------------------------------------
## Nice shade ##
# A line of text is given as input to the program. Write a program that determines whether the shade of a text is good or not. The text has a good connotation if it contains the substring “good” in all possible cases.
s = input()

if 'хорош' in s.lower():
    print('YES')
else:
    print('NO')

# ------------------------------------------------------------------------------------
## lower case ##
# A string is given as input to the program. 
# Write a program that counts the number of lowercase letter characters.

# Read the input string
s = input()

# Initialize a variable to count lowercase characters
low_cnt = 0

# Convert the entire string to lowercase
all_low = s.lower()

# Iterate through each character of the string
for i in range(0, len(s)):
    # Check if the character in the original string is equal to the corresponding character in the lowercase string
    # Also, ensure that the character is not a digit
    if s[i] == all_low[i] and s[i] not in '0123456789':
        # If the character is lowercase, increment the count
        low_cnt += 1
        
# Print the count of lowercase characters
print(low_cnt)

#####
# Read the input string
s = input()

# Initialize a variable to count lowercase characters
cnt_al_lower = 0

# Iterate through each character in the string
for el in s:
    # Check if the character is not equal to its uppercase version
    # This implies the character is lowercase
    if el != el.upper():
        # If the character is lowercase, increment the count
        cnt_al_lower += 1
        
# Print the count of lowercase characters
print(cnt_al_lower)
