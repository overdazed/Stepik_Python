## Even List ##
# An even number is given as input to the program n≥2. 
# Write a program that prints a list of even numbers
# [2, 4, 6, ..., n].

n = int(input())

list_s = list()
for i in range(2, n+1, 2):
    list_s.append(i)
    
print(list_s)

## Sum of two lists ##
# The program receives two lines of text containing integers as input. Lists of numbers Land are formed from these lines M. 
# Write a program that creates a third list whose elements are the sums of the corresponding list elements Land M. 
# Next, the program should display each element of the resulting list on one line, separated by 1 space.

list_1 = [int(i) for i in input().split()]
list_2 = [int(i) for i in input().split()]
    
n = [list_1[i] + list_2[i] for i in range(len(list_1))]

for num in n:
    print(num, end=' ')
    
    
## Sum of numbers ##
# The input to the program is a string of text containing natural numbers. 
# Write a program that inserts a sign between each number +and then calculates 
# the sum of the resulting numbers.

s = input()

nums = s.split()

expession = '+'.join(nums)

total_sum = 0

for i in nums:
    total_sum += int(i)
    #print(i, sep='+')
    
print(expession, end='=')
print(total_sum)


## Valid number 🌶️🌶️ ##
# A line of text is given as input to the program. 
# Write a program that determines whether the entered 
# string is a valid telephone number. 
# A string of text is a valid phone number if it has the format:
## abc-def-hijk or
## 7-abc-def-hijk,
# where a, b, c, d, e, f, h, i, j, k are numbers from 0 to 9.

seq = input().split('-')
lens = [len(el) for el in seq]

if lens == [1, 3, 3, 4] and ''.join(seq).isdigit() and seq[0] == '7':
    print('YES')
elif lens == [3, 3, 4] and ''.join(seq).isdigit():
    print('YES')
else:
    print('NO')
    

## The longest ##
# A line of text is given as input to the program. 
# Write a program  using a list expression that finds the length of the longest word.

n = input().split()

max_len = max(len(word) for word in n)

print(max_len)


## Youth slang ##
# A line of text is given as input to the program. 
# Write a program  using a list expression that 
# converts each word of the input text into "youth jargon" 
# according to the following rule: 
# 1. the first letter of each word is removed and placed at the end of the word; 
# 2. then the syllable “ki” is added to the end of the word.

s = input().split()

jargon = ' '.join(word[1:] + word[0] + 'ки' for word in s)

print(jargon)


