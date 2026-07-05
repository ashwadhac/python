# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# Add these two matrices and store it in C 

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

# Empty matrix C
C = []

# Matrix addition
for i in range(len(A)):          # rows
    row = []
    for j in range(len(A[0])):   # columns
        row.append(A[i][j] + B[i][j])
    C.append(row)

# Print result
print("Matrix C (A + B):")
for row in C:
    print(row)

