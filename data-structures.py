# Exercise 1 - Create new list from odd and even indexed elements
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd_elements = list1[1::2]
even_elements = list2[0::2]

result = odd_elements + even_elements
print("Final list:", result)

# Exercise 2 - Remove item at index 4, add to 2nd position and end
sample_list = [34, 54, 67, 89, 11, 43, 94]
print("Original list:", sample_list)

element = sample_list.pop(4)
print("List after removing index 4:", sample_list)

sample_list.insert(2, element)
print("List after adding at index 2:", sample_list)

sample_list.append(element)
print("List after adding at end:", sample_list)



# Exercise 3 - Slice list into 3 chunks and reverse each
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list:", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

for i in range(3):
    chunk = sample_list[start:end]
    print("Chunk", i+1, ":", chunk)
    print("Reversed:", list(reversed(chunk)))
    start = end
    end += chunk_size


# Exercise 4 - Count occurrences of each element in a list
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list:", sample_list)

count_dict = {}
for item in sample_list:
    count_dict[item] = sample_list.count(item)

print("Count of each element:", count_dict)


# Exercise 5 - Check if first and last elements are the same
def first_last_same(number_list):
    print("Given list:", number_list)
    first = number_list[0]
    last = number_list[-1]
    if first == last:
        print("Result: True")
    else:
        print("Result: False")

first_last_same([10, 20, 30, 40, 10])
first_last_same([75, 65, 35, 75, 30])

# Exercise 6 - Remove duplicates from a list
sample_list = [1, 2, 3, 4, 1, 5, 6, 1, 3, 2]
print("Original list:", sample_list)

unique_list = list(set(sample_list))
print("List after removing duplicates:", unique_list)

# Exercise 7 - Merge two dictionaries
dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
dict2 = {"Forty": 40, "Fifty": 50, "Sixty": 60}

merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)



