def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("Original List:\n")
print(lst)
print("Reversed List:\n")
print(Reverse(lst))
