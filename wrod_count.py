f=open("sample.txt","r")
c=0
for x in f:
    a=x.split()
    print(a)
    c=c + len(a)
print ("Total number of words = ", c)
