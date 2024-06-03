def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[1, 4],
     [2, 5],
     [3, 6]]
result = matrix_multiply(A, B)
print("Result of multiplication:")
for row in result:
    print(row)
