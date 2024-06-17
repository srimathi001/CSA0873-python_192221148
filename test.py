str=input("enter a string:")
c=input("enter the character:")
j=0
while j<len(str):
    for i in range(0,len(str),1):
        if str[i]==c:
            res=true
    print("index:",i)
    j+=1
if c not in str:
    print("the character is not found")
