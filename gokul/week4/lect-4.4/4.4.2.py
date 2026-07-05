## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
## findout the index of number 21 in the generated list, if the number is not present in the list print -1

import random

num = []
for i in range(1000):
    num.append(random.randint(1, 1000))

num.sort()
print(num)

if 21 in num:
    print(num.index(21))
else:
    print(-1)

