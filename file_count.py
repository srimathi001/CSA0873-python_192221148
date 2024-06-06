d=open("sample.txt","w")
d.write("hello everyone\n")
d.write("new line here")
d.close()
f=open('class.txt','r')
text=f.read()
space=0
line=0
char=0
for i in text:
    if (i==" "):
        space=space+1
    elif (i=="\n"):
        line=line+1
    else:
        char=char+1
print(" The total number of characters is = ",char)
print(" The number of lines is = ",line+1)
print(" The number of spaces is = ",space)
