# import array
# val = array.array('i', [1,2,3,4,5,6])
# import array as arr
# val = arr.array('i', [1,2,3,4,5,6])

from array import *
val = array('i', [1,2,3,4,5,6])

# len(val) is used to get the length of the array val

# normal for loop
for i in range(0,len(val)):
    print(val[i], end = " ")

print()

# enhanced for loop (For each/ For in)... here we don't need index
for x in val:
    print(x, end= ", ")

print()

print(val.typecode)       # i for integer

val.reverse()  # reverse the array

for i in range(0,len(val)):
    print(val[i], end = " ")
print()

# insertion
val.insert(0, 50)     # (index, value)

# insert in last position
val.append(100)     # add the value at last
for x in val:
    print(x, end= " ")
print()

# update
val[2] = 200
for x in val:
    print(x, end= " ")
print()

# making copy
copyArray = array(val.typecode, (x for x in val))
# (x for x in val) will create a list
for x in copyArray:
    print(x, end = " ")
print()

# removing array
copyArray.pop(2)   # removes the element in 2nd index
copyArray.pop()    # removes the last element
for x in copyArray:
    print(x, end = " ")
print()
# remove using remove
copyArray.remove(50)    # removes the value -> 50 and error if value is not present
for x in copyArray:
    print(x, end = " ")
print()
# slicing -> creates a new array (subarray) 
abc = copyArray[2:4]    # first included and second excluded
for x in abc:
    print(x, end = " ")
print()
# reverse using slicing
abc = copyArray[::-1]
for x in abc:
    print(x, end = " ")
print()

#          USER INPUT ARRAY
# arr = array('i', [])

# n = int(input("Enter the number: "))

# for i in range(0,n):
#     arr.append(int(input('> ')))

# for x in arr:
#     print(x, end=" ")

# searching an element
arr = array('i', [12,43,53,55,32])
i = arr.index(53)        # returns the index of the value, if value not present (ERROR)
print(i)


