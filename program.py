
# list comprehension
# create a list of power 2 of numbers between 1..10
# [1, 4, 9, 16, 25, ... 100]
# 1², 2², 3², 4², 5², ... 10²

#          append      for loop
squares = [x**2       for x in range(1, 11)]

#squares = []
#for x in range(1, 11):
#    squares.append(x**2)

print(squares)

# create a list using comprehension for modulus of 3
[1 % 3, 2 % 3, ...]