def main():
    rows = int(input("Enter the number of rows for the matrices: "))
    cols = int(input("Enter the number of columns for the matrices: "))
    print("Matrix A:")
    A = input_matrix(rows, cols)
    print("Matrix B:")
    B = input_matrix(rows, cols)
    result = matrix_addition(A, B)
    print("Result of matrix addition:")
    for row in result:
        print(row)
if __name__ == "__main__":
    main()
