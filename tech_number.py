n = int(input("enter a number:"))
s = str(n)
l = len(s)
if(l % 2 == 0):
    fst_half = s[:l//2]
    scnd_half = s[l//2:]
    tot_sum = (int(fst_half)+int(scnd_half))
    square_sum = tot_sum*tot_sum
    if(n == square_sum):
        print("The Given Number {", n, "} is Tech number")
    else:
        print("The Given Number {", n, "} is Not a Tech number")
else:
    print("The Given Number {", n, "} is Not a Tech number")
