# Accept a two digit number as input and print the sum of its digits. What about a three digit number?


for two digit number
n = int(input())

print((n // 10) + (n % 10))

Idea:
tens digit = 45 // 10 = 4
ones digit = 45 % 10 = 5

Example:

Input: 45

45 // 10 = 4
45 % 10 = 5

Sum = 4 + 5 = 9

for three digit number
Idea:
hundreds = 123 // 100 = 1
tens = (123 // 10) % 10 = 2
ones = 123 % 10 = 3

n = int(input())

print((n // 100) + ((n // 10) % 10) + (n % 10))

Input: 123

1 + 2 + 3 = 6