# take a number as input and find the sum of numbers from 1 to that number

# take input
n = int(input("Enter a number: "))

sum_numbers = 0

for i in range(1, n + 1):
    sum_numbers += i

print("Sum of numbers from 1 to", n, "is", sum_numbers)
