##### Strings #####

### Search and replace ###

# Methods for finding and replacing strings within other strings.

# Each method in this group supports optional arguments <start> and <end>. 
# As with string slices, the method's effect is limited to the part of the source string starting at the character position <start> and continuing up to the character position <end>, but not including it. 
# If the parameter <start>specified, a parameter <end>no, then the method is applied to part of the source string from <start>to the end of the line. 
# If parameters are not specified, it is assumed that <start> = 0 , <end> = len(s). 

### count() method ###
# Method count(<sub>, <start>, <end>) counts the number of non-overlapping occurrences of a substring <sub> to the original line s. 
s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

### startswith() method ###
# Method startswith(<suffix>, <start>, <end>)determines begins whether the source line ssubstring <suffix>. 
# If the source string begins with the substring <suffix>, the method returns True, and if not, then False. 
s = 'foobar'
print(s.startswith('foo'))
print(s.startswith('baz'))

### endswith() method ###
# Method endswith(<suffix>, <start>, <end>) determines ends whether the source string s substring <suffix>. 
# Method returns value True if the original string ends with a substring <suffix> and False otherwise. 
s = 'foobar'
print(s.endswith('bar'))
print(s.endswith('baz'))

### Methods find(), rfind() ###
# Method find(<sub>, <start>, <end>)finds the index of the first occurrence of a substring <sub>in the original line s. 
# If the line s does not contain a substring <sub>, then the method returns the value -1. 
# We can use this method along with the operator into check whether a given string contains some substring or not. 
s = 'foo bar foo baz foo qux'
print(s.find('foo'))
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))
# Method rfind(<sub>, <start>, <end>) identical to method find(<sub>, <start>, <end>), 
# except that it looks for the first occurrence of the substring <sub> starting from the end of the line s. 

### Methods index(), rindex() ###
# Method index(<sub>, <start>, <end>) identical to method find(<sub>, <start>, <end>), except that it throws an error 
# ValueError: substring not found 
# during program execution, if the substring <sub>not found.

# Method rindex(<sub>, <start>, <end>) identical to method index(<sub>, <start>, <end>), except that it looks for the first occurrence 
# of the substring <sub> starting from the end of the line s.

### strip() method ###
# Method strip()returns a copy of the string sin which all spaces at the beginning and end of the line have been removed. 
s = '     foo bar foo baz foo qux      '
print(s.strip())

### lstrip() method ###
# Method lstrip()returns a copy of the string sin which all spaces at the beginning of the line have been removed. 
s = '     foo bar foo baz foo qux      '
print(s.lstrip())

### rstrip() methods ###
# Method rstrip()returns a copy of the string sin which all spaces at the end of the line have been removed. 
s = '      foo bar foo baz foo qux      '
print(s.rstrip())

# !!!!! Methods strip(), lstrip(), rstrip()can take an optional argument as input <chars>. Optional argument <chars>is a string that specifies the set of characters to delete. 

### replace() method ###
# Method replace(<old>, <new>) returns a copy s with all occurrences of the substring <old>, replaced by <new>. 
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))
# Method replace()can take an optional third argument <count>, which determines the number of replacements. 
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))

# -----------------------------------------------------------------------------------------------------------------
## What will the code snippet below show? ##
s = 'aabbAAccDDaa'
s = s.lower()
print(s.count('a'))

## What will the code snippet below show? ##
s = 'www.stepik.org'
print(s.startswith('www'))

## What will the code snippet below show? ##
s = 'www.stepik.org'
print(s.endswith('.ru'))

## What will the code snippet below show? ##
s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))

## What will the code snippet below show? ##
s = '     I learn Python language               '
print(s.strip())

## What will the code snippet below show? ##
s = 'abcdababa'
print(s.replace('ab', '123'))

# --------------------------------------------------------------------------------------------------------------------
## Word count ##
# The input to the program is a string of text consisting of words separated by exactly one space. 
# Write a program that counts the number of words in it. 

s = input()
print(s.count(' ') + 1)

# --------------------------------------------------------------------------------------------------------------------
## A minute of genetics ##
# The input to the program is a string of genetic code consisting of the letters A (adenine), G (guanine), C (cytosine), T (thymine). 
# Write a program that calculates how much adenine, guanine, cytosine and thymine are in a given line of genetic code. 

s = input().lower()

adr = s.count('а')
gua = s.count('г')
cyt = s.count('ц')
tim = s.count('т')

print('Аденин:', adr)
print('Гуанин:', gua)
print('Цитозин:', cyt)
print('Тимин:', tim)

# --------------------------------------------------------------------------------------------------------------------
## Stranger Things ##
# Jim Hopper uses the radio to try to get Odie's message. The receiver receives n different Morse code sequences. 
# Having decoded them, he receives sequences of numbers and letters of the lowercase Latin alphabet. 
# Moreover, only Odie’s messages contain the number 11 , with a minimum 3 times. 
# Help Jim determine the number of messages from Odie.

n = int(input())
cnt = 0

for i in range(n):
    s = input()
    if s.count('11') >= 3:
        cnt += 1
    
print(cnt)

# --------------------------------------------------------------------------------------------------------------------
## Stranger Things ##
# A line of text is given as input to the program. 
# Write a program that counts the number of digits in a given string. 

s = input()

cnt = 0
for i in range(10):
    cnt += s.count(str(i))
    
print(cnt)
###########
cnt = 0
for c in input():
    if '0'<= c <='9':
        cnt += 1
print(cnt)
# --------------------------------------------------------------------------------------------------------------------
## .com or .ru ##
# A line of text is given as input to the program. 
# Write a program that checks that a string ends with a substring .comor .ru. 

s = input()

if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')
    
# --------------------------------------------------------------------------------------------------------------------
## Most Frequent Symbol ##
# A line of text is given as input to the program. 
# Write a program that displays the symbol that appears most frequently. 

s = input()

max_cnt = 0
line_cnt = 0
for i in s:
    if s.count(i) >= max_cnt:
        max_cnt = s.count(i)
        line_cnt = i
        
print(line_cnt)
#######
s = input()

most_common = s[0]
for el in s:
    if s.count(el) >= s.count(most_common):
        most_common = el
        
print(most_common)

# --------------------------------------------------------------------------------------------------------------------
## First and last occurrence ##
# A line of text is given as input to the program. If the letter “f” appears only once in this line, print its index. 
# If it occurs two or more times, print the indices of its first and last occurrence on the same line, separated by a space character. 
# If the letter "f" does not appear in this line, "NO" should be printed. 

s = input()

for el in s:
    if s.count('f') == 1:
        print(s.find('f'))
        break
    elif s.count('f') > 1:
        print(s.find('f'), s.rfind('f'))
        break
else:
    print('NO')
    
# --------------------------------------------------------------------------------------------------------------------
## Deleting a fragment ##
# The input to the program is a line of text in which the letter “h” appears at least twice. 
# Write a program that removes the first and last occurrence of the letter "h" from this string, 
# as well as all the characters between them.
s = input()

first = s.find('h')
last = s.rfind('h')
whut = s[:first] + s[last+1:]

print(whut)
