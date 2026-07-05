# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# multiply these two matrices using for loops

# Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B
B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

# Result matrix C (3x3 with zeros)
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Matrix multiplication
for i in range(len(A)):          # rows of A
    for j in range(len(B[0])):   # columns of B
        for k in range(len(B)):  # columns of A / rows of B
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

# Print result
print("Result Matrix (A x B):")
for row in C:
    print(row)
