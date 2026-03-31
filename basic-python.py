
#Exercise 1
num1 = 30
num2 = 70
product = num1 * num2
total = num1 + num2
if product > 100:
    print ('The product is:', product)
else:
    print ('The sum is:', total) 



#Exercise 2
for i in range(1, 11):
    print(i, '+', (i-1), '=', i + (i-1))



#Exercise 3
str1 = "Python"
for i in range(0, len(str1)):
    if i % 2 == 0:
        print(str1[i])



#Exercise 4
str1 = 'Python'
n = 2
print(str1[n:])


#Exercise 5
num = 10
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")

#Exercise 6
# Exercise 6 - Display numbers divisible by 5
numbers = [10, 20, 33, 46, 55, 75, 81]
for divisible_num in numbers:
    if divisible_num % 5 == 0:
         print(divisible_num)

# Exercise 7 - Count occurrences of a digit in a number
num = 25144803677215547
digit = 5

count = str(num).count(str(digit))
print("The digit", digit, "appears", count, "times")

# Exercise 8 - Check if a number is a perfect square
import math

num = 625

sqrt = math.sqrt(num)

if sqrt == int(sqrt):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")


# Exercise 9 - Display reversed string
str1 = "Python"

print("Original string:", str1)
print("Reversed string:", str1[::-1])

# Exercise 10 - Check if a number is a palindrome
num = 121

if str(num) == str(num)[::-1]:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")

# Exercise 11 - Merge two lists and sort them
list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]

merged = list1 + list2
merged.sort()

print("List 1:", list1)
print("List 2:", list2)
print("Merged and Sorted:", merged)


# Exercise 12 - Find the intersection of two lists
list1 = [10, 20, 30, 40, 50]
list2 = [20, 30, 60, 70]

intersection = [x for x in list1 if x in list2]
print("Intersection:", intersection)

# Exercise 13 - Count occurrences of each element in a list
list1 = [10, 20, 30, 10, 50, 10, 20]

count_dict = {}

for num in list1:
    count_dict[num] = list1.count(num)

print("Element counts:", count_dict)

# Exercise 14 - Calculate the sum of digits of a number
num = 1234
sum_of_digits = sum(int(x) for x in str(num))
print("Sum of digits of", num, "=", sum_of_digits)

# Exercise 15 - Print a multiplication table
num = 5

for i in range(1, 11):
    print(num, 'x', i, '=', num * i)