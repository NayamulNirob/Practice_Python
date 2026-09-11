matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])

for row in matrix:
    for col in row:
        print(col, end=" ")