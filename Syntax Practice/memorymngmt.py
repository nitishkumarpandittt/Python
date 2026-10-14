# a = 5

# print(a)
# print(id(a))


# # same value 
# b=10
# c=10
# d=10
# print(id(b))
# print(id(c))
# print(hex(id(d)))


# INTERNING : Memory optimization technique...
# Object interning in Python is a memory optimization technique that stores only 
# one copy of immutable objects in memory, reusing them across variables to save space and improve performance

# Python automatically interns small integers (typically in the range -5 to 256) and short strings 
# (often those resembling identifiers or under a certain character limit, such as 4096 characters in modern versions). 

# String interning allows Python to replace identical string literals with references to 
# the same memory location, meaning the is operator returns True for identical literals.  
# While short strings and compile-time constants are interned automatically, dynamically generated strings 
# (e.g., via runtime concatenation or user input) are not interned by default. 


# # Immutabte Object ———> int, float, str, boot, tuple, None        (memory location changes when manipulating data)
# a = 5
# b = a

# print(a, id(a))       # 5 140733613947448
# print(b, id(b))       # 5 140733613947448


# print()

# a = a+1
# print(a, id(a))      # 6 140733613947480
# print(b, id(b))      # 5 140733613947448

# print()

# # Mutable Object ———> list, dict, set       (memory location remains same when manipulating data)
# c = {1, 2, 3}
# d = c

# print(c, id(c))
# print(d, id(d))

# print()
# c.add(4)
# print(c, id(c))
# print(d, id(d))


# size

# import sys

# # integer => 28 bytes
# print(f"Integer 0: {sys.getsizeof(0)} bytes")
# print(f"Integer 5: {sys.getsizeof(5)} bytes")
# print(f"Integer 1000: {sys.getsizeof(1000)} bytes")
# print(f"Integer 10**1000: {sys.getsizeof(10**1000)} bytes")   # Takes larger bytes  468

# # float => 24 bytes
# print(f"float 5.0: {sys.getsizeof(5.0)} bytes")
# print(f"float 3.14: {sys.getsizeof(3.14)} bytes")

# # bool => 28 bytes
# print(f"True 1: {sys.getsizeof(True)} bytes")
# print(f"False 0: {sys.getsizeof(False)} bytes")

# # None => 16 bytes
# print(f"None: {sys.getsizeof(None)} bytes")

# print()
# # strings => (49 in old python /  41 in new python versions) + characters in the string
# # 41 is the size of empty string 
# str = ["", "a", "aa", "a"*100, "a"*1000]

# for s in str:
#     display = s if len(s) <= 40 else s[:37] + "..."
#     print(f"'{display}'")
#     print(f"Length: {len(s)} characters, Size: {sys.getsizeof(s)}")
#     print()


# size of empty list -> 56       (List does not stores element in the list... it stores address pointing to the element)
# L = [1, 2, 3, 4, 5]
# print(sys.getsizeof(L))    # this gives shallow size meaning it gives the size of the addresses (usually 8 bytes) of the element stored

# In Python, over-allocation is a memory management strategy primarily used by lists to optimize append performance.  
# When a list grows, Python allocates slightly more memory than immediately needed to avoid the cost of frequent reallocations 
# and data copying, providing amortized O(1) time complexity for append operations


# size of empty tuple -> 40   (with every element addition 8 bytes are added)
# T = (1,2,3, "Hello world", "teri maa ka bhosda")
# print(sys.getsizeof(T))

# size of empty dict -> 64 bytes
# D = {"name": "nitish"}
# print(sys.getsizeof(D))

# # size of empty set -> 64 bytes
# S = {1,2}
# print(sys.getsizeof(S))

