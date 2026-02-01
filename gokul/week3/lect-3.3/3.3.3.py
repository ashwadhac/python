# find the factorial of a number using while loop, take number n as input

# take input
n = int(input("Enter a number: "))

# initialize variables
factorial = 1
num = 1  # start multiplying from 1

# loop to calculate factorial
while num <= n:
    factorial *= num   # multiply factorial by current num
    num += 1           # go to next number

# print result
print("Factorial of", n, "is", factorial)
