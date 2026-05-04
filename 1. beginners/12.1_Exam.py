## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
numbers[2] = 99
print(numbers)

##[1, 2, 99, 4, 5]
# [99, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 99]
# [1, 99, 3, 4, 5]

## What will the code snippet below show? ##
numbers = list(range(3))
print(numbers)

# ['r', 'a', 'n', 'g', 'e', '(', '3', ')']
# [0, 1, 2, 3]
# [3]
# [2]
##[0, 1, 2]

## What will the code snippet below show? ##
numbers = [10] * 5
print(numbers)

##[10, 10, 10, 10, 10]
# [10] [10] [10] [10] [10]
# [10] * 5
# [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

## What will the code snippet below show? ##
numbers = list(range(1, 10, 2))
for i in numbers:
    print(i, end='*')
    
# 1*3*5*7*9
# 2*4*6*8
# 2 4 6 8 10*
# 1 3 5 7 9*
##1*3*5*7*9*

## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
print(numbers[-2])

# 5
# 1
##4
# IndexError: list index out of range
# 2

## What will the code snippet below show? ##
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = numbers1 + numbers2
print(numbers3)

# [11, 22, 33]
# [10, 20, 30, 1, 2, 3]
##[1, 2, 3, 10, 20, 30]
# [1, 2, 3] + [10, 20, 30]

## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:3]
print(my_list)

# [1, 2]
# [2, 3, 4]
##[2, 3]
# [1, 2, 3]

## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:]
print(my_list)

# [1, 2, 3, 4]
##[2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [2]

## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
my_list = numbers[:-1]
print(my_list)

# [1, 2, 3, 4, 5]
##[1, 2, 3, 4]
# [5]
# [2, 3, 4, 5]

## What will the code snippet below show? ##
numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)

# [1, 2, 3, 4]
# [4, 3, 2, 1]
# [5, 4, 3, 2, 1]
##[1, 2, 3, 4, 5]

## What will the code snippet below show? ##
names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
if 'Джасмин' not in names:
    print ('Не могу найти Джасмин.')
else:
    print('Ceмья Джасмин: ', end='')
    print(names)
    
# ['Джим', 'Джилл', 'Джон', 'Джасмин']
## Ceмья Джасмин: ['Джим', 'Джилл', 'Джон', 'Джасмин']
# Не могу найти Джасмин.
# Ceмья Джасмин:

## Which of the following functions returns the length of a list? ##
## len()
# size()
# length()
# lengthof()

## Which of the following functions returns the largest value in the list? ##
# maximum()
# highest()
# greatest()
## max()
# best_of()

## Which of the following methods adds a value to the end of an existing list? ##
## append()
# add_to()
# increase()
# add()

## Fill in the blanks ##
# As a result of application "del instructions" the value at the given index position is removed from the list.

