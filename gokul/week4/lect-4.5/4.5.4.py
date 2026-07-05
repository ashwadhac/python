
## write a python code to print the minimum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]


l = [1,44,22,11,23,36,49,28,31,8,54,54]

min_value = l[0]      # start with first element

for n in l:
    if n <min_value:
        min_value = n

print("Minimum element:", min_value)
