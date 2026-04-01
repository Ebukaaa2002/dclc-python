# Exercise 1 - Create new list from odd and even indexed elements
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

odd_elements = list1[1::2]
even_elements = list2[0::2]

result = odd_elements + even_elements
print("Final list:", result)