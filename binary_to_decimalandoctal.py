def binary_to_decimal_and_octal(binary_str):
    decimal_value = int(binary_str, 2)
    octal_value = oct(decimal_value)

    return decimal_value, octal_value[2:]
def main():
    binary_str = input("Enter a binary number: ")
    if not all(char in '01' for char in binary_str):
        print("Invalid binary number.")
        return
    decimal_value, octal_value = binary_to_decimal_and_octal(binary_str)
    print(f"Binary: {binary_str}")
    print(f"Decimal: {decimal_value}")
    print(f"Octal: {octal_value}")
if __name__ == "__main__":
    main()
