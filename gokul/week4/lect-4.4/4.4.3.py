## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list

import random
num=[]
for i in range(100):
    num.append(random.randint(1, 1000))

num.sort()
print(num)
even = []
odd = []

for n in num:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even numbers list:", even)
print("Odd numbers list:", odd)