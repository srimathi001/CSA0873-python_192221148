a=eval(input("enter 1st binary number:"))
b=int(input("enter 2nd binary number:"))
c=int(input("enter 3rd binary number:"))
bina=int(a)
binb=int(b)
binc=int(c)
print(bina,binb,binc)
if bina>binb and bina>binc:
    print("Greatest is", a)
elif binb>bina and binb>binc:
    print("Greatest is", b)
else:
    print("Greatest is", c)
