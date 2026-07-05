# create a python code to sort the list using for loop
l = [9, 3, 7, 1, 6, 3, 4]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print("Sorted list:", l)


