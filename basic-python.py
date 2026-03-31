
#Exercise 1
num1 = 30
num2 = 70
product = num1 * num2
sum = num1 + num2
if product > 100:
    print ('The product is:', product)
else:
    print ('The sum is:', sum) 



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

