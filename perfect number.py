num=int(input("enter a number:"))
sum=0
for i in range (1,num):
    if num%i ==0:
        sum+=i
if sum==num:
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")
