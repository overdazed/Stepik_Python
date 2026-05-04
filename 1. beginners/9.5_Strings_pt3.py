##### Strings #####

### Character classification ###

## isalnum() method ##
# Method isalnum()determines whether the source string consists of alphanumeric characters. 
# Method returns value True if the source string is non-empty and consists only of alphanumeric characters and False otherwise.
s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())


## isalpha() method ##
# Method isalpha()determines whether the source string consists of alphabetic characters. 
# Method returns value True if the source string is non-empty and consists only of alphabetic characters and False otherwise. 
s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())

## isdigit() method ##
# Method isdigit()determines whether the source string consists of only numeric characters. 
# Method returns value True if the source string is non-empty and consists only of numeric characters and False otherwise.
s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())

## islower() method ##
# Method islower()determines whether all alphabetic characters in the source string are lowercase (lowercase). 
# Method returns value True if all alphabetic characters of the source string are lowercase and False otherwise. 
# All non-alphabetic characters are ignored! 
s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())
print(s2.islower())
print(s3.islower())

## isupper() method ##
# Method isupper()determines whether all alphabetic characters in the source string are capitalized (uppercase). 
# Method returns value True if all alphabetic characters of the source string are uppercase and False otherwise. 
# All non-alphabetic characters are ignored!
s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())
print(s2.isupper())
print(s3.isupper())

## isspace() method ##
# Method isspace()determines whether the source string consists of only whitespace characters. 
# Method returns value True if the string consists only of whitespace characters and False otherwise. 
s1 = '       '
s2 = 'abc1$d'
s3 = 'asd asd'

print(s1.isspace())
print(s2.isspace())
print(s3.isspace())

# --------------------------------------------------------------------------------------------------------------------
## What will the code snippet below show? ##
s = 'aabbAA111ccDDaa'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

## What will the code snippet below show? ##
s = 'aabb!@#$11cc'
print(s.islower())

## What will the code snippet below show? ##
s = 'AAb!@#$11CC'
print(s.isupper())

## What will the code snippet below show? ##
s = '    abbc    '
print(s.isspace())

# --------------------------------------------------------------------------------------------------------------------
##### Formatting Strings #####

# Storing strings in variables is convenient, 
# but it is often necessary to collect strings from other objects (strings, numbers, etc.) and 
# perform the necessary manipulations with them. 
# For this purpose, you can use the string formatting mechanism. 

age = 27
txt = 'My name is Timur, I am ' + age
print(txt)
# This code causes a runtime error because we are trying to add a number and a string. 
# To solve such a problem we can use the function str which converts a numeric value to a string: 
age = 27
txt = 'My name is Timur, I am ' + str(age)
print(txt)

# This code works, but Python's preferred formatting method is format. The previous program can be rewritten as: 
age = 27
txt = 'My name is Timur, I am {}'.format(age)
print(txt)

# We pass the necessary parameters to the method format, and Python formats the specified string and places them in the string in place of the placeholders {}. 
# We can create as many placeholders as we want per line: 
age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
print(txt)

# For clarity and formatting flexibility, we can use a serial number in the placeholder: {0}, {1}, {2},.... 
# This number determines the position of the parameter passed to the method format(numbering starts from zero): 
age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
print(txt)

# Parameter namegets up in {0}placeholder, parameter agegets up in {1}filler, etc. We can use the same number in several placeholders 
name = 'Timur'
txt = 'My name is {0}-{0}-{0}'.format(name)
print(txt)


### f-string ###
# Method formatdoes a good job of formatting strings, but if there are a lot of parameters, the code may seem a little redundant: 
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'
               .format(first_name, last_name, age, profession, affiliation))

# Python 3.6 introduced a new type of string called f-strings. By prefixing the string with f, placeholders can include code, such as a variable name. The previous code can be written as:
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')
# In place of the filler {first_name}the value of the variable appears first_name, in place of the placeholder {last_name}the value of the variable appears last_name etc.


### Notes ###
# Note 1:   Detailed documentation with string formatting.
https://docs.python.org/3/library/string.html#custom-string-formatting

# -------------------------------------------------------------------------------------------------
## Format ##
# Complete the given code using string formatting using the method 'format' so that it outputs the text:

# «In 2010, someone paid 10k Bitcoin for two pizzas.» (без кавычек).
year = 2010
amount = '10k'
coin = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'.format(year, amount, coin)

print(s)


# Complete the given code using string formatting with 'f-strings' so that it outputs the text: 
year = 2010
amount = '10K'
currency = 'Bitcoin'
print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


