array = [16, 18, 27,17, 16, 23, 21, 19]
s=[]
count = 0
for num in array:
    if num < 4:
        continue
    for i in range(2, num):
        if num % i == 0:
            count += 1
            s.append(num)
            break
print("Number of Composite Numbers =", count)
print(s)
