## What will be the outcome of the following expression if x and y are two strings?

# len(x) + len(y) == len(x+y)

op:
True
eg:
x = "Hello"
y = "World"

print(len(x))        # 5
print(len(y))        # 5
print(len(x + y))    # 10

print(len(x) + len(y) == len(x + y))

op:
5
5
10
True