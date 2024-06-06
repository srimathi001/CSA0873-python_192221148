a=input("enter a value")
b=input("enter a value")
print("addition:",add(a+b))
print("subraction:",a-b)
if isinstance(a, int) and isinstance(b, int):
    if b != 0:
        print("Integer Division:", a//b)
    else:
        print("Integer Division: Division by zero error")
else:
    print("Integer Division: Not applicable for floats")
if b != 0:
    print("Floor Division:", a//b)
    print("Modulo Division:", a%b)
else:
    print("Floor Division: Division by zero error")
    print("Modulo Division: Division by zero error")
