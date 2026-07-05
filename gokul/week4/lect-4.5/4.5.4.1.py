## write a python code to print the maximum element of the list, using for loop


l = [1,44,22,11,23,36,49,28,31,8,54,54]

max_value = l[0]      # start with first element

for n in l:
    if n > max_value:
        max_value = n

print("Maximum element:", max_value)
