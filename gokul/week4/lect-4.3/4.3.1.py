# create a list of 10 random numbers between 0 and 1, generated using random library
import random

nums = []

for i in range(10):
    nums.append(random.random())

print(nums)
