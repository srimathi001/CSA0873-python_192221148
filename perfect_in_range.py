def perfectSquares(l, r):
    for i in range(l, r + 1):
        if (i**(.5) == int(i**(.5))):
            print(i, end=" ")
l = 1
r = 10
perfectSquares(l, r)
