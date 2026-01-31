## write a python code , for the following test cases

# testcase 1
'''
INPUT: 'a'
OUTPUT: 1
'''

# testcase 2
'''
INPUT:'b'
OUTPUT: 2
'''

# testcase 3
'''
INPUT:'y'
OUTPUT: 25
'''
# take input from user
ch = input("Enter a lowercase letter: ")

# find its position in the alphabet
position = ord(ch) - ord('a') + 1

print(position)
