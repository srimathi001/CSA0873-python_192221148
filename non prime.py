a=int(input("enter a number"))
b=int(input("enter a number"))
p=[]
for n in range(a,b+1):
    if n>1:
        for i in range(2,n):
            if (n%i)==0:
                break
            else:
                p[i]=n
print(p)
