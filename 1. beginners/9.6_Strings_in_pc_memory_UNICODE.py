##### Representation of strings in computer memory, ASCII and Unicode #####

### Representation of strings in computer memory ###
# Any set of data in a computer's RAM must be stored as a binary number. 
# This also applies to strings that consist of characters (letters, punctuation marks, etc.). 
# When a character is stored in memory, it is first converted into a digital code. 
# And then this digital code is stored in memory as a binary number.

# Over the years, various encoding schemes have been developed to represent characters in computer memory. 
# Historically, the most important of these encoding schemes is the ASCII (American Standard Code for Information Interchange) encoding scheme. 


### ASCII character table ###
# ASCII is a set of 128 numeric codes that represent English letters, various punctuation marks, and other characters. 
# For example, the ASCII code for the uppercase English letter "A" (Latin) is 65. 
# When you type the uppercase letter "A" on a computer keyboard, the number 65 is stored in memory (as a binary number, of course).

# 'A' -> 65 -> 01000001

# The ASCII code for an uppercase English “B” is 66, for an uppercase “C” it ​​is 67, etc. 
# There are exactly 7 bits per character in ASCII.


### Notes ###

# Note 1: Character Table website Official Unicode. https://home.unicode.org/

# Note 2 : Unicode is not an encoding. This is exactly a symbol table. How characters with their corresponding codes are stored in computer memory depends on the specific Unicode-based encoding, such as UTF-8.

# Note 3: The first 128 codes of the Unicode character table are the same as ASCII. 


# -------------------------------------------------------------------------------------------
### Function ord ###

# Function ordallows you to determine the code of a certain character in the Unicode character table. 
# The argument to this function is a single character. 
num1 = ord('A')
num2 = ord('B')
num3 = ord('a') 
print(num1, num2, num3)

# Please note that the function ordaccepts just a single character . If you try to pass a string containing more than one character: 
num = ord('Abc')
print(num)

### Function chr ###
# Function chrallows you to determine the symbol itself by the symbol code. 
# The argument of this function is a numeric code. 
chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110) 
print(chr1, chr2, chr3)

# Functions ordand chroften work in pairs. We can use the following code to output all capital letters of the English alphabet: 
for i in range(26):
    print(chr(ord('A') + i))
    

# Calling a function ord('A')returns the code of the character “A”, which is equal to 65. 
# Then, at each iteration of the loop, the value of the variable is added to this code 
# i = 0, 1, 2, ..., 25, and then the resulting code is converted to a symbol using a function call chr. 

### Notes ###
# Functions ord and chr are reciprocal. The following equalities hold for them:

chr(ord('A')) = 'A', ord(chr(65)) = 65.

# ----------------------------------------------------------------------------------------------
## What will the code snippet below show? ##
print(ord('foo'))

## Characters in range ##
# The program is given two numbers as input. a and b. 
# Write a program that, for each code value in the range from aa to bb (inclusive), 
# displays its corresponding character from the Unicode character table. 

a = int(input())
b = int(input())

for i in range(a, b+1):
    print(chr(i), end = ' ')
    
# ----------------------------------------------------------------------------------------------
## Simple cipher ##

# A line of text is given as input to the program. 
# Write a program that translates each of its characters into its corresponding code from the Unicode character table.

s = input()

for i in range(len(s)):
    print(ord(s[i]), end=' ')
    
## Cipher Caesar 🌶️ ##
# Caesar's Legion, created in The 23rd century based on the Roman Empire does not change ancient traditions and uses the Caesar cipher. 
# This let them down, because this cipher is very simple. However, in the post-apocalypse, people do not know all the intricacies of the pre-war world, 
# so scientists from the NKR cannot understand how exactly to decode these messages. Write a program to decode this cipher.

# Input format
# The first line gives the number n (1 ≤ n ≤ 25) – shift, the second line contains the encoded message in the form of a string with lowercase Latin letters.

# Output format
# The program should output one line - the decoded message. Note that you need to decode the message, not encode it. 
n = int(input())
s = input()

decoded_message = ''
# moves letters n to right
for i in s:
    x = ord(i) - n # Shift the character back by n positions
    if x < 97: # If the result is below the lowercase 'a'
        x = 122 - (96-x) # Wrap around to the end of the alphabet
    decoded_message += chr(x) # Convert the shifted character back to a letter and add to the decoded message
    
print(decoded_message, end= '')

s = 'Python rocks!'
print(s[1:6])


s = 'Python rocks!'
print(s.replace('', 3))


s = input()

if s.count('f') == 2:
    print(s.rfind('f'))
elif s.count('f') > 2:
    print(1)
elif s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
    
  
s = input()  
    
if s.count('f') == 1:
    print(-1)
elif s.count('f') >= 2:
    print(s.find('f', s.find('f')+ 1))
else:
    print(-2)
