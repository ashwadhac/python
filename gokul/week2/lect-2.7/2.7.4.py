
# write a python script for the below test case,
# Note the input will be of 5 characters long,


# testcase 1
'''
INPUT : 'gokul'
OUTPUT : 'hplvm'
'''

# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:
# Take input from user
s = input("Enter a 5 character string: ")

# Initialize output string
result = ""

# Loop through each character
for ch in s:
    # Shift character by 1
    # ord() gives ASCII value, chr() converts back to character
    result += chr(ord(ch) + 1)

print(result)

