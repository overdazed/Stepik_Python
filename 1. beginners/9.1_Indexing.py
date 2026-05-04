##### Strings #####

### Repetition of material ###

# Creating a line. To create strings, we use double quotes ''or "":
s1 = 'Python'
s2 = "Pascal"

# Reading a line. To read text data into a string variable, we use the function input():
s = input()  # считали текст
num = int(input())  # считали текст и преобразовали его в целое число

# Line length. To determine the length of a string (number of characters), we use the built-in function len():
s = 'Hello'
n = len(s)  # значение переменной равно 5
print(n)

# Concatenation and multiplication by number.+ The and operators *can be used for strings. The operator +concatenates two or more strings. This is called string concatenation. The * operator repeats a string a specified number of times. 

Expression	    Result
'AB' + 'cd'     'ABcd'
'A' + '7' + 'B'	'A7B'
'Hi'* 4	        'HiHiHiHi'

# Membership operator in.
s = 'All you need is love'
if 'love' in s:
    print('❤️')
else:
    print('💔')
    
    
##### String indexing #####

# Very often it is necessary to refer to a specific character in a string. To do this, Python uses square brackets [], which indicate the index (number) of the desired character in the string.

# Let s = 'Python'. The table below shows how indexing works:

# Expression	Result	Explanation
# s[0]	        P	    first character of line
# s[1]	        y	    second character of the line
# s[2]	        t	    third character of the line
# s[3]	        h	    fourth character of the line
# s[4]	        o	    fifth character of the line
# s[5]	        n	    sixth character of the line

# Negative indexing

# Thus, we get
# Positive indices	 0	 1	 2	 3	 4	 5
# Line	             P	 y	 t	 h	 o	 n
# Negative indices	-6	-5	-4	-3	-2	-1

# For example, if s = 'Python', and we try to access s[17], we will get an error:
IndexError: string index out of range


### Iterating Strings ###

#Very often you need to scan the entire string, processing each character. It is convenient to use a loop for this for. Let's write a program that prints each character of a string on a separate line:
s = 'abcdef'
for i in range(len(s)):
    print(s[i])
#We pass range() the length of the string to the function len(s). 
# In our case, the length of the string s is equal to 6. 
# Thus, the function call range(len(s)) has the form range(6) and 
# the loop variable is equentially iterates through all the values ​from 0 to 5. 
# This means that the expression s[i] will sequentially return all characters of the string s. 
# This method of iterating a string is convenient when we need not only the element itself s[i], but also its index i.

# If we don't need the index of the symbol itself, then we can use a shorter iteration method:
s = 'abcdef'
for c in s:
    print(c)
    
# ---------------------------------------------------------------------------------------
## What will the code snippet below show?
s = 'abcdefg'
print(s[0] + s[2] + s[4] + s[6])

## What will the code snippet below show?
s = 'abcdefg'
print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

## What will the code snippet below show?
s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
    
## Complete the given code using the indexer so that it outputs the comma character.
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-10])

### In column 1 ###
# One line is given as input to the program. Write a program that displays the elements of a string with indexes 0, 2, 4, ...in a column.
s = input()

for i in range(0, len(s),2):
    print(s[i])
    
### In column 2 ###
# One line is given as input to the program. Write a program that displays the elements of a string in reverse order in a column.
s = input()
for i in range(len(s)-1,-1,-1):
    print(s[i])
    
### Full name ###
# The program receives three lines as input: first name, last name and patronymic (in that order). Write a program that prints a person's initials.
first_name = input()
last_name = input()
patronymic = input()

print(last_name[0], first_name[0], patronymic[0], sep='')

### Digit 1 ###
# The input to the program is one line consisting of numbers. Write a program that calculates the sum of the digits of a given string.
n = input()

total = 0
for i in range(len(n)):
    total += int(n[i])
print(total)

### Digit 2 ###
# One line is given as input to the program. Write a program that prints the message "Number" (without quotes) if a string contains a number. Otherwise, display the message “No numbers” (without quotes).
s = input()

cnt = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        cnt += 1
        break
    
if cnt >= 1:
    print('Цифра')
else:
    print('Цифр нет')
######
s = input()

for i in s:
    if i in '0123456789':
        print('Цифра')
        break
else:
    print('Цифр нет')


### How many times? ###
# One line is given as input to the program. Write a program that determines how many times the characters +and appear in a string *.
s = input()

cnt_plus = 0
cnt_ast = 0
for i in range(len(s)):
    if s[i] == '+':
        cnt_plus += 1
    if s[i] == '*':
        cnt_ast += 1
print('Символ + встречается', cnt_plus, 'раз')
print('Символ * встречается', cnt_ast, 'раз')


### Same neighbors ###
# One line is given as input to the program. 
# Write a program that determines how many identical adjacent symbols it contains.

# Read the line and write it to the 's' variable
s = input()
# The neighbor count of these... 'counter' is equal to 0
cnt = 0
# Loop 'i' range from 0 because positive indexing starts from 0, 
# and the stop limit 'line length' is minus one, because again the code will not work indexing is positive!
for i in range(0, len(s)-1):
    # Condition if the line with the loop index is equal to the same line but index + 1
    if s[i] == s[i+1]:
        # Counter + 1
        cnt += 1
# Counter and output
print(cnt)

### Vowels and consonants ###
# The input to the program is one line with letters of the Russian language. 
# Write a program that determines the number of vowels and consonants.
s = input()

txt = s.lower()

cnt1 = 0
cnt2 = 0
for i in range(len(s)):
    if txt[i] in 'ауоыиэяюе':
        cnt1 += 1
    if txt[i] in 'бвгджзйклмнпрстфхцчшщ':
        cnt2 += 1
print('Количество гласных букв равно', cnt1)
print('Количество согласных букв равно', cnt2)
######
sentence = input()

vocalic = "ауоыиэяюе"
consonants = "бвгджзйклмнпрстфхцчшщ"

counter_voc = 0
counter_con = 0
for i in sentence.lower():
    if i in vocalic:
        counter_voc += 1
    elif i in consonants:
        counter_con += 1
print("Количество гласных букв равно", counter_voc)
print("Количество согласных букв равно", counter_con)

### Vowels and consonants ###
# The input to the program is a natural number written in the decimal number system. 
# Write a program that converts a given number to the binary number system .

128:2 = 64 Rest:0
64:2 = 32  Rest:0
32:2 = 16  Rest:0
16:2 = 8   Rest:0
8:2 = 4    Rest:0
4:2 = 2    Rest:0
2:2 = 1    Rest:0
1:2 = 0    Rest:1

from bottom to top: 10000000
