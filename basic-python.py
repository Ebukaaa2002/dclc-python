
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