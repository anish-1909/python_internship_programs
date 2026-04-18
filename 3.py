# Original matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose logic
transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

# Output
print("Transpose matrix")
for row in transpose:
    print(row)