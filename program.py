
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

# create a list using comprehension for modulus of 3 for 10 items
#[1 % 3, 2 % 3, ...]
#[1, 2, 0, 1, 2, 0 , 1, 2, 0 ...]
modulus_3 = [x % 3 for x in range(1, 11)]
print(modulus_3)

zugi = [x for x in range(1, 21) if x % 2 == 0]
#zugi = []
#for x in range(1, 21):
#    if x % 2 == 0:
#        squares.append(x)
print(zugi)

# create a list with 10 random numbers (1-100) using comprehension
#   (import does not count as a line)
# given this list :
#    _lst1 = [1, -5, -100, 2, 0, 3, 4]
#    create a list with the positive numbers only using comprehension
# given this list:
#    _lst2 = ['hello', 'of', 'python', 'world', 'best']
#    1. create a list with the first letter only. make it upper case
#        only for words longer than 2 characthers
#    2. create a list with the reversed words
#       ['olleh', 'nohyyp', 'dlrow', 'tseb']
# given this list:
#    _lst3 = [1, 2, 5, 8, 17, 19, 29]
#    create a list with booleans , each value indicates
#      if the original one was prime or not
#    i.e.
#    _lst3 = [1,      2,       5, 8,        17, 19, 29]
#            [False, True, True, False ...]
#    you can use this funcion to detect if number is prime or not:
# def is_prime(a):
#    x = True
#    for i in range(2, a):
#       if a % i == 0:
#           return False
#    return True
