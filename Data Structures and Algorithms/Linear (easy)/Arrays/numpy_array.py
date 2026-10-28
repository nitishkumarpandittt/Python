# NORMAL array module does not allow us to create multi dimensional array
# numpy array allows heterogeneous elements

# * Normal functions

# import numpy 
# numpy.array()
# import numpy as np
# np.array()

from numpy import *   # allows heterogeneous elements

arr = array([1,2,3,4,"Hello"]) # no need of type code

for x in arr:
    print(x, end = " ")
print()

arr2 = array([1,2,3,4,5], float)  # type casting the entire list
# throws error if the element can't be converted -> string to int (ERROR)
for x in arr2:
    print(x, end=" ")
print()

# linspace -> for arithematic progression (a pattern)
# arange -> arranges the elements acc to the diff provided
# zeros -> initializes the elements to 0, similarly ones
# full -> (size, value)

a = linspace(10, 20, 5)  # (start included, end included, no. of partions)
for x in a:
    print(x, end=" ")
print()

b = arange(10, 20, 4)  # (start included, end excluded, difference)
for x in b:
    print(x, end=" ")
print()

c = zeros(10, int)   # default gives float... so we can give second argument as int for type conversion
# (size, type)
for x in c:
    print(x, end=" ")
print()
# same we have for 1's 
c = ones(10, int)   # default gives float... so we can give second argument as int for type conversion
for x in c:
    print(x, end=" ")
print()

d = full(10, 5)   # (size, value)
for x in d:
    print(x, end=" ")
print()

# * MULTIDIMENSIONAL ARRAY

# zero Dimension
zero = array(10)
print(zero)

# one Dimension
one = array([1,2,3,4,5])
print(one)

# two Dimension
two = array([
        [1,2,3],
        [4,5,6]
    ])
print(two)

# three Dimension
three = array([
    [[1,2],[3,4]], 
    [[5,6],[7,8]]
    ])
print(three)
