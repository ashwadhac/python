## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list

import random

num = []
for i in range(1000):
    num.append(random.randint(1, 1000))

num.sort()
print(num)

# Smallest and second smallest 
smallest = num[0]
second_smallest = None
for n in num:
    if n > smallest:
        second_smallest = n
        break

print("Smallest number:", smallest)
print("Second smallest distinct number:", second_smallest)

# Largest and second largest 
largest = num[-1]
second_largest = None
for n in reversed(num):
    if n < largest:
        second_largest = n
        break

print("Largest number:", largest)
print("Second largest distinct number:", second_largest)
