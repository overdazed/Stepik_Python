##### Lists #####

# In previous lessons, we worked with sequences of numbers, symbols, and strings, 
# but we did not save the entire sequence in the computer’s memory, 
# but processed it element by element, reading a new element over and over again. 
# However, in many tasks it is necessary to preserve the entire sequence. 
# For example, the classic task of sorting (ordering) a certain sequence requires storing all the data in computer memory. 
# Unfortunately, without saving, it is impossible to sort them. 
# And here a data structure comes to the rescue, which in most programming languages ​​is called an array. 
# In Python it's called a list.

# !!!! Data structure is a software unit that allows you to store and process a variety of similar and/or logically related data.
# A list is a sequence of elements, numbered from 0, like characters in a string.


### Creating a list ###
# To create a list, you need to list its elements separated by commas in square brackets:
numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
# The list 'numbers' consists of 5 elements, and each of them is an integer.
numbers[0] == 2
numbers[1] == 4
numbers[2] == 6
numbers[3] == 8
numbers[4] == 10

# The list 'languages' consists of 4 elements, each of which is a string.
languages[0] == 'Python'
languages[1] == 'C#'
languages[2] == 'C++'
languages[3] == 'Java'

# !!! Values ​​enclosed in square brackets and separated by commas are called list elements .

# The list can contain values ​​of different data types :
info = ['Timur', 1992, 61.5]

# The list info contains a string value, an integer value, and a floating point number.
info[0] == 'Timur'
info[1] == 1992
info[2] == 61.5

# !!! Typically, list items contain the same type of data, and in practice it is rarely necessary to create lists that contain elements of different data types.

### Empty list ###
# There are two ways to create an empty list:

# Use empty square brackets []
# Use a built-in function called list()
mylist = []  # пустой список
mylist = list()  # тоже пустой список

### List output ###
# To display the entire list, you can use the function print():
numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
print(numbers)
print(languages)

# The function print() displays the elements of a list, in square brackets, separated by commas:
[2, 4, 6, 8, 10]
['Python', 'C#', 'C++', 'Java']

# !!! Note that the list output contains square brackets. Later we will learn how to display list elements in a more convenient form using loops or using unpacking.

### Built-in list function ###
# Python has a built-in function list() that, in addition to creating an empty list, can convert some types of objects into lists.

# For example, we know that a function range() produces a sequence of integers in a given range. To convert this sequence into a list, we write the following code:
numbers = list(range(5))

# When this code runs, the following happens:
# 1. The function is called range(), to which the number 5 is passed as an argument;
# 2. This function returns a sequence of numbers 0, 1, 2, 3, 4;
# 3. A sequence of numbers 0, 1, 2, 3, 4 is passed as an argument to the function list();
# 4. The function list()returns a list [0, 1, 2, 3, 4];
# 5. The list [0, 1, 2, 3, 4]is assigned to a variable numbers.

# Here's another example:
even_numbers = list(range(0, 10, 2))  # 0, 2, 4, 6, 8
odd_numbers = list(range(1, 10, 2))  # 1, 3, 5, 7, 9

# Similarly, using a function, list() we can create a list from the characters of a string. 
# To convert a string to a list, we write the following code:
s = 'abcde'
chars = list(s)  # список содержит символы 'a', 'b', 'c', 'd', 'e'
# When this code runs, the following happens:
# 1. The function is called list(), to which the string is passed as an argument 'abcde';
# 2. The function list()returns a list ['a', 'b', 'c', 'd', 'e'];
# 3. The list ['a', 'b', 'c', 'd', 'e']is assigned to a variable chars.

### Notes ###
# Note 1: 
# As already mentioned, lists in Python are similar to arrays in other programming languages. 
# However, there is still a difference between lists and arrays. 
# Array elements always have the same data type and are located in the computer memory as a continuous block, 
# while list elements can be scattered throughout memory as desired and can have different data types.

# Note 2. 
# Please note that when displaying the contents of a list using the function print(), 
# all string elements of the list are surrounded by single quotes. 
# If you want to output in double quotes, you need to write the output code yourself.

# ----------------------------------------------------------------------------------------------
## Values ​​in lists enclosed in square brackets and separated by commas are called ##
# numbers
# values
# terms
# indexers
## elements

## How many elements does the list have numbers? ##
# 5
## 4
# 3
# 9

## What is the index of number 17 in the list numbers? ##
# 6
# 3
# 5
## 4

## Can a list in Python contain values ​​of different data types? ##
# No
# Yes

## What will be the output of the following code? ##
numbers = [0, 1, 3, 14, 2, 7, 9, 8, 10]
print(numbers)
# ['0', '1', '3', '14', '2', '7', '9', '8', '10']
# [0, 1, 3, 14, 2, 7, 9, 8, 10]
# 0, 1, 3, 14, 2, 7, 9, 8, 10
# 0 1 3 14 2 7 9 8 10

## What will be the output of the following code? ##
names = ['Michael', 'John', 'Freddie']
print(names)
# ["Michael", "John", "Freddie"]
# 'Michael', 'John', 'Freddie'
# [Michael, John, Freddie]
# ['Michael', 'John', 'Freddie']

# ----------------------------------------------------------------------------------------------
## List of numbers ##
# The program is given one number as inputnn. Write a program that displays a list [1, 2, 3, ..., n].
n = int(input())

x = list(range(1, n+1))
print(x)

# ----------------------------------------------------------------------------------------------
## List of numbers ##
# The program is given one number as input n. 
# Write a program that prints a list of n letters of the English alphabet  ['a', 'b', 'c', ...] in lower case.
n = int(input())

y = 97 + n
characters = []
for i in range(97, y):
    characters += chr(i),

print(characters)
########
n = int(input())

s = ''
for i in range(n):
    s += chr(ord('a')+i)
    
print(list(s)) 