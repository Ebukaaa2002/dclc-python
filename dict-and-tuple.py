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


# Dictionary Exercise 5 - Merge two dictionaries
dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Forty": 40, "Fifty": 50, "Sixty": 60}

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)



# ==============================
# TUPLE EXERCISES
# ==============================

# Tuple Exercise 1 - Basic tuple operations
my_tuple = (1, 2, 3, 4, 5)
print("My tuple:", my_tuple)

# Access third element
print("Third element:", my_tuple[2])

# Find length
print("Length of tuple:", len(my_tuple))

# Tuple Exercise 2 - Tuple repetition
tuple_1 = (1, 2, 3)
print("Original tuple:", tuple_1)
repeated_tuple = tuple_1 * 3
print("Repeated 3 times:", repeated_tuple)

# Tuple Exercise 3 - Slicing tuples
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Original tuple:", tuple1)

# First 3 elements
print("First 3 elements:", tuple1[:3])

# Last 3 elements
print("Last 3 elements:", tuple1[-3:])

# Middle elements
print("Middle elements:", tuple1[3:7])