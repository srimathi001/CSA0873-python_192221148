num = int(input("enter a number"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit
   temp //= 10
print("the sum of the digits:",sum)
