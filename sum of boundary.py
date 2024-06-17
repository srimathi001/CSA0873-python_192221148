def sum_boundary_elements(matrix):
    if not matrix or not matrix[0]:
        return 0  
    rows = len(matrix)
    cols = len(matrix[0])
    boundary_sum = 0
    boundary_sum += sum(matrix[0])
    boundary_sum += sum(matrix[rows-1])
    for i in range(1, rows-1):
        boundary_sum += matrix[i][0]  
        boundary_sum += matrix[i][cols-1]  
    return boundary_sum
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print("Sum of boundary elements:", sum_boundary_elements(matrix))
