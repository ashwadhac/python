# create a list of 20 random integers between 1 and 10, generated using random library, and sort the list


import random
num=[]
for i in range(20):
    num.append(random.randint(1,10))
print(num)
num.sort()
print(num)