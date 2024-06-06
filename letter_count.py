f=open("sample.txt","r")
l=0
for line in f:
    a=line.split()
    for i in a:
        for letter in i:
            l=l+1
print (" The total number of letters is = ", l)
