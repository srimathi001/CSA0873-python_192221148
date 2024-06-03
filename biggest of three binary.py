def main():
    a = input("Enter the first binary number: ")
    b = input("Enter the second binary number: ")
    c = input("Enter the third binary number: ")
    max_binary = max(a, b, c, key=lambda x: int(x, 2))
    print(f"The greatest of {a}, {b}, and {c} is {max_binary}")
if __name__ == "__main__":
    main()
