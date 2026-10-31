# Hashing itself is a technique or concept, not an algorithm.
# The tool that does the hashing is an algorithm, specifically called a hash function or hashing algorithm (such as SHA-256 or MD5).

# Hash table -> key-value pair
# Hash function -> data to numbers
# box -> hash(key) % total_boxes
# store(box, "value") 

# using dictionary for key-value store
users = {}     

# insert
users["nitish@gmail.com"] = 'Nitish Pandit'
users["rajbabu@gmail.com"] = 'Raj Babu'
users["nitin@gmail.com"] = 'Nitin Babu'

# fetch -> internally uses hash function 0(1)
print(users['nitish@gmail.com'])
print('nitish@gmail.com' in users)

# update
users['nitish@gmail.com'] = "Nitish Kumar Pandit"
print(users)

# delete
del users['nitish@gmail.com']
print(users)


# using set -> only keys are there and allows only unique values
online_users = set()

# insert
online_users.add("Ravi")
online_users.add("Kisan")
online_users.add("Om")
online_users.add("Om")

# fetch
print("Ravi" in online_users)
print(online_users)

# remove
online_users.remove("Om")

print(online_users)

# count frequency

orders = [
    "Biryani", "Dosa", "Burger", 
    "Biryani", "Burger", 
    "Biryani", "Burger", 
    "Biryani", "Dosa"
]

def count_frequency(orders):
    freq = {}

    for dish in orders:
        if dish in freq:
            freq[dish] += 1
        else:
            freq[dish] = 1
    return freq

print(count_frequency(orders))