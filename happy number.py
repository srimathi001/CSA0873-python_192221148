def happy(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=sum+digit**2
        temp=temp//10
    return sum
num=int(input("Enter the number:"))
result=num
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("happy number")
elif result==4:
    print("not happy number")
