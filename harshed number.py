num = int(input("enter a number"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit
   temp //= 10
if num%sum==0:
   print(num,"is an harshed number")
else:
   print(num,"is not harshed number")
