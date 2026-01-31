# write a python code where you will take an input number k and a string s.
# you have to move the string by k characters to the right

# TestCase 1
'''
INPUT:
    s='abcdefg'
    k=2

OUTPUT: 'cdefghi`
'''

# TestCase 2
'''
INPUT:
    s='chennai'
    k=20
OUTPUT:
    'wbyhhuc'
'''
s = input("Enter string: ")    # e.g., 'abcdefg'
k = int(input("Enter k: "))    # e.g., 2

result = ""

for ch in s:
    shifted = (ord(ch) - ord('a') + k) % 26 + ord('a')
    result += chr(shifted)

print(result)
