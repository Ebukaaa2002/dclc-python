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