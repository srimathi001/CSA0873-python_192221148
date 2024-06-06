def fact(no):
    f=1
    for i in range(1,no+1):
        f=f*i
        return (f)
def maximum(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if (max <arr[i]):
            max=arr[i]
            return max
import myfunctions
no=int(input("Enter number to find factorial :"))
print ("Factorial of a given number is %d"%myfunctions.fact(no))
a=[8,10,30,15,20]
print("The maximum number is %d"%myfunctions.maximum(a))
