# print all odd number between 3 to 30 , using while loop

# start number
num = 3

# loop until num reaches 30
while num <= 30:
    if num % 2 != 0:   # check if number is odd
        print(num)
    num += 1           # go to next number
