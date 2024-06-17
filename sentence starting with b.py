string=input("Enter the Para: ")
str1=string.split(".")
print("Total number of lines:",len(str1))
count=0
for i in str1:
    str2=i.split()
    for j in str2:
        if j[0]=="B" or j[0]=="b":
            count=count+1
print("Number of Sentences that start with letter B :",count)
