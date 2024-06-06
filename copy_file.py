d=open("sample.txt","w")
d.write("hello everyone\n")
d.write("new line here hello")
d.close()
with open("sample.txt") as f:
    with open("copy.txt","w")as u:
        for line in f:
            u.write(line)
