d=open("sample.txt","w")
d.write("hello everyone\n")
d.write("new line here hello")
d.close()
f=open("sample.txt","r")
word=input (" Enter a word: ")
c=0
for x in f:
    a=x.split()
    print(a)
    for i in range (0, len(a)):
        if (word == a[i]):
            c=c+1
print ("The word :",word,"appears:", c," times ")
          
