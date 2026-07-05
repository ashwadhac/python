## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list

import random
num = []
for i in range(15):
    num.append(random.randint(1, 15))

num.sort()
print(num)

print("Missing numbers:")

for n in range(1, 16):
    if n not in num:
        print(n)
