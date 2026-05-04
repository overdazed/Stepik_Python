##### Strings #####

### Line slices ###

# In the previous lesson we learned how to work with specific characters in a string using indexes []. 
# Sometimes we need to work with entire parts of a string, in which case we use slices. 
# Slicing is like a combination of indexing and function range().

# Consider the line 
s = 'abcdefghij'

# Positive indices 	    0 	 1 	 2 	 3 	 4 	 5 	 6 	 7 	 8 	 9
# Line 	                a 	 b   c   d   e 	 f   g   h   i   j
# Negative indices 	   -10 	-9 	-8 	-7 	-6 	-5 	-4 	-3 	-2 	-1 

# With a slice we can get multiple characters of the original string by 
# creating a range of indexes separated by a colon s[x:y]. 
print(s[2:5]) # 5 excluded
print(s[0:6]) # 6 excluded
print(s[2:7]) # 7 excluded


### Cut to the end, from the beginning ###

# If you omit the second parameter in the slice s[x:](but put a colon), 
# then the cut is taken to the end of the line. Similarly, 
# if you omit the first parameter s[:y], then you can take a slice from 
# the beginning of the line. Slice s[:]matches the string itself s.
print(s[2:])
print(s[:7])


### Negative indexes in a slice ###

# We can also use negative indices to create slices. 
# As stated earlier, negative row indices start with -1 
# and are counted down until the beginning of the line is reached. 
# When using negative indexes, the first slice parameter must be 
# less than the second, or must be omitted.

print(s[-9:-4])
print(s[-3:])
print(s[:-3])


### Cutting step ###
# We can pass a third optional parameter to the slice, which is 
# responsible for the slice step. For example, a slice s[1:7:2]will create a string bdf, 
# consisting of every second character (indices 1,3,5 , right border is not included in the slice). 
print(s[1:7:2])


### Negative cut step ###
# as the slice step If you specify a negative number, 
# then the characters will go in reverse order.
print(s[::-1])

print(s[1:7:2])
print(s[3::2])
print(s[:7:3])
print(s[::2])
print(s[::-1])
print(s[::-2])


### Summarizing ###
# Program code 	    Result 	        Explanation
# s[2:5] 	        cde 	        a string consisting of characters with indices 2,3,42 , 3 , 4
# s[:5] 	        abcde 	        first five characters of the line
# s[5:] 	        fghij 	        a string consisting of characters with indices from 5 to the end
# s[-2:] 	        ij 	            last two characters of the line
# s[:] 	            abcdefghij 	    the whole line
# s[1:7:2] 	        bdf 	        a string consisting of every second character with indices from 11 to 66
#s[::-1] 	        jihgfedcba 	    the line is in reverse order, since the step is negative 


### Changing a string character by index ###
# Let's say we have a string s = 'abcdefghij' and we want to replace the character with index 44 on 'X'. You can try to write the code:
s = 'abcdefghij'
# s[4] = 'X'

# However, this code doesn't work. In Python, strings are immutable , meaning we cannot change their contents using an indexer. 

# If we want to change any character in the string s, we must create a new row. The following code uses slices and solves the problem:
s = s[:4] + 'X' + s[5:]
print(s)
# We create two slices: from the beginning of the line to 5th character (not inclusive) and with 6th character (inclusive) 
# to the end of the line, and between them we insert the character we need, which will stand on 5th position (4 index). 


### Notes ###
# Note 1: 
# String slicing syntax is very similar to function syntax range().

# Note 2: 
# If the first slice parameter is greater than the second, then the slice creates an empty string. 

# -----------------------------------------------------------------------------------------------------------------
## What will the code snippet below show? 
s = 'abcdefg'
print(s[2:5])

## What will the code snippet below show? 
s = 'abcdefg'
print(s[3:])

## What will the code snippet below show?
s = 'abcdefg'
print(s[:3])

## What will the code snippet below show?
s = 'abcdefg'
print(s[:])

## What will the code snippet below show?
s = 'abcdefg'
print(s[::-3])

## Complete the given code using slices so that it outputs the first 12 line characters s.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

## Complete the above code using slices so that it prints the last 9 characters of the line s. 
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

## Complete the given code using slices so that it outputs each 7 line character s(beginning with 0th index). 
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(::7)

## Complete the given code using slices so that it outputs the string sin reverse order. 
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# -----------------------------------------------------------------------------------------------------------------
## A palindrome ##
# The input to the program is one word, written in lowercase. Write a program that determines whether it is a palindrome.

# put your python code here

s = input()

print(len(s))
print((len(s)//2)+1)

first = s[:(len(s)//2)]
second = s[((len(s)//2)+1):]

#if 
print(s[:(len(s)//2)])
print(s[((len(s)//2)+1):])


# Read the string and write it to the variable 'n'
# Create a variable equal to the length of the string, call it 'j'
# Create a flag equal to 'NO'
# Create a condition if n in the positive index is equal to n in reverse order
# The flag changes to YES my god
# Output the flag

# Read the input word
s = input()

# Get the length of the word
j = len(s)
# Initialize a flag to 'NO'
flag = 'NO'

# Iterate through each index of the word
for i in range(1, j+1):
    # Check if the word is equal to its reverse with a step of -i
    if s == s[::-i]:
        # If it is, update the flag to 'YES'
        flag = 'YES'

# Print the flag indicating whether the word is a palindrome or not
print(flag)

# ------------------------------------------------------------------------------------
## Making cuts 1 ##
# One line is given as input to the program. Write a program that prints:
s = input()

# 1. the total number of characters in the line
num_chars = len(s)
print(num_chars)

# 2. original line repeated 3 times
three_times = s * 3
print(three_times)

# 3. first character of line
first_char = s[0]
print(first_char)

# 4. the first three characters of the line
first_three_chars = s[:3]
print(first_three_chars)

# 5. last three characters of the line
last_three_chars = s[-3:]
print(last_three_chars)

# 6. the string in reverse order
reverse = s[::-1]
print(reverse)

# 7. a string with the first and last characters removed.
first_last_char_removed = s[1:-1]
print(first_last_char_removed)

# ------------------------------------------------------------------------------------
## Making cuts 2 ##
# One line is given as input to the program. Write a program that prints:
# 1. third character of this line;
# 2. second last character of this line;
# 3. the first five characters of this line;
# 4. the entire line except the last two characters;
# 5. all symbols with even indexes;
# 6. all characters with odd indexes;
# 7. all characters in reverse order;
# 8. all characters of the string one after another in reverse order, starting from the last one.
s = input()

# 1. third character of this line;
print(s[2:3])

# 2. second last character of this line;
print(s[-2:-1])

# 3. the first five characters of this line;
print(s[:5])

# 4. the entire line except the last two characters;
print(s[:-2])

# 5. all symbols with even indexes;
print(s[::2])

# 6. all characters with odd indexes;
print(s[1::2])

# 7. all characters in reverse order;
print(s[::-1])

# 8. all characters of the string one after another in reverse order, starting from the last one.
print(s[::-2])

# ------------------------------------------------------------------------------------
## Making cuts 2 ##
# A line of text is given as input to the program. Write a program that will cut it into two equal parts, rearrange them and display them on the screen.

# Read the input string
s = input()
n = len(s)
# Check if the length of the string is even
if len(s)%2 == 0:
    # If it's even, calculate the first half and last half accordingly
    first_half = s[:(n//2)]
    last_half = s[(n//2):]
else:
     # If it's odd, calculate the first half with one more character
    first_half = s[:(n//2)+1]
    # Calculate the last half accordingly
    last_half = s[((n//2)+1):]

# Rearrange the halves and print them
print(last_half + first_half)
#####
s = input()
n = len(s)

a = s[:(n + 1) // 2]
b = s[(n + 1) // 2:]

print(b + a)
