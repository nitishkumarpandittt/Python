# strings are immutable in python...

# creation of strings
name = "Rajiv Sharma"

# reading/accessing strings
print(name)
print(name[2]) # even a single character is a string in python type(name[0])
print(name[-2]) # access from last

# length
print(len(name))

# slicing
name[0:10:1]  # start, end, steps

# updating a string using slicing
xyz = "nmopqrs"
updated_xyz = xyz[:3] + "N" + xyz[4:]    # write the index u want to update
print(updated_xyz)
        # replace can also be used but it changes all the occurrences
print(xyz.replace("p", "N"))

# adding / concatenate -> it creates a new name and the update the location
name = name + "Xyz"
print(name)

# removing using slicing
name = name[:12] + name[14:]
print(name)


# split -> converts string to list using a delimeter 
word = "My name is Nitish".split()
print(word)

# join -> converts list to string using a delimeter
print(" ".join(word))