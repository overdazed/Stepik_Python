limit = 1000

for a in range(1, limit):
    for b in range(a + 1, limit):
        sum_of_cubes = a**3 + b**3
        c = int(sum_of_cubes ** (1/3))
        if c <= limit and c**3 == sum_of_cubes:
            print(sum_of_cubes, ":", a, "^3 +", b, "^3 =", c, "^3 =", c, "^3")
            

# 8.
previous_y = 0
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a != b and a != c and a!= d and b != c and b != d and c != d:
                    if a**3 + b**3 == c**3 + d**3:
                        y = a**3 + b**3
                        if y > 1728 and y != previous_y and (a, b) != (c, d):
                            previous_y = y
                            print(y)

                    #if a**3 + b**3 == c**3 + d**3:
                        #print(a**3 + b**3)
                        
                        
previous_y = set()  # Initialize a set to store previously printed numbers
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                        y = a ** 3 + b ** 3
                        if y > 1728 and y not in previous_y and (a, b) != (c, d):
                            previous_y.add(y)  # Add the current number to the set
                            print(y)


# Read the number and write it to the variable 'n' 
n = int(input())

# Create a variable with an empty string, to it we will add the resulting numbers converted to string format 
b = ''

# Create a conditional loop, number greater than 0 
while n > 0:
    # find the remainder of n bdividing by 2
    remainder = n % 2
    # add it to our empty string
    # turn the remainder into a string using str()
    b = str(remainder) + b
    # Also, don’t forget to leave the number already divided by 2 at the end of the loop ( n//=2)
    n = n // 2

print(b)
