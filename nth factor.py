num=int(input("enter the number:"))
n=int(input("enter the nth value:"))
factor=[]
count=0
for i in range (1,num+1):
    if num%i==0:
        count+=1
        factor.append(i)
print("number of factors:",count)
print(n,"th factor:",factor[n-1])
