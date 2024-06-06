def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube
given_number = 0.6
square_number, cube_number = calculate_square_and_cube(given_number)

print("Square Number:", square_number)
print("Cube Number:", cube_number)
