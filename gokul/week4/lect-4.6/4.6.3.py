# write a piece of code to  find the dot product.

x = [1, 7, 3, 4]
y = [8, 6, 3, 2]

dot_product = 0

for i in range(len(x)):
    dot_product = dot_product + (x[i] * y[i])

print("Dot product:", dot_product)

