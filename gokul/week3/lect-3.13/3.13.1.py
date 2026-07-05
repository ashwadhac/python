## write a code for the below test cases

# print until you find @ in the string, using break statement
# TestCase 1
INPUT="abcd@gmail.com"
# OUTPUT:
'''
a
b
c
d
'''


input = "abcd@gmail.com"

for ch in input:
    if ch == '@':  # stop when @ is found
        break
    print(ch)
