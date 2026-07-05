# create a python code to sort the list using while loop

l = [9, 3, 7, 1, 6, 3, 4]

i = 0
while i < len(l):
    j = i + 1
    while j < len(l):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
        j += 1
    i += 1

print("Sorted list:", l)

