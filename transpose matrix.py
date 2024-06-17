a=[[4,6,7,8],
 [3,7,2,7],
   [7,3,7,5]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        c[i][j]=a[j][i]
for i in c:
    print(i)
