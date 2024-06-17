n=input("enter list elements")
l=list(map(int,n.split(",")))
l1=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]>l[j]:
            c+=1
    l1.append(c)
print(l1)
