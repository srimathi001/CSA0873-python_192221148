def add_binary(a, b):
    int_a = int(a, 2)
    int_b = int(b, 2)
    sum_int = int_a + int_b
    return bin(sum_int)[2:]
def main():
    a = input("Enter the first binary number: ")
    b = input("Enter the second binary number: ")
    if not all(c in '01' for c in a) or not all(c in '01' for c in b):
        print("Invalid input. Please make sure to enter only binary numbers (0 or 1).")
        return
    result = add_binary(a, b)
    print(f"The sum of {a} and {b} is {result}")
if __name__ == "__main__":
    main()
