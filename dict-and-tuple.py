# ==============================
# DICTIONARY EXERCISES
# ==============================

# Dictionary Exercise 1 - Basic dictionary operations
dict1 = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print("Original dictionary:", dict1)

# Add new key-value pair
dict1['profession'] = 'Doctor'
print("After adding profession:", dict1)

# Modify value
dict1['age'] = 40
print("After modifying age:", dict1)

# Access a key
print("City:", dict1['city'])


# Dictionary Exercise 2 - Perform dictionary operations
dict1 = {'name': 'Alice', 'age': 35, 'city': 'New York'}

# Print all keys
print("Keys:", list(dict1.keys()))

# Print all values
print("Values:", list(dict1.values()))

# Print all key-value pairs
print("Key-value pairs:", list(dict1.items()))

# Dictionary Exercise 3 - Create dictionary from two lists
keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty']
values = [10, 20, 30, 40, 50]

result_dict = dict(zip(keys, values))
print("Dictionary:", result_dict)