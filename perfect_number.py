def is_perfect_number(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n
number = int(input("enter a number:"))
if is_perfect_number(number):
    print("It's a Perfect Number")
else:
    print("It's not a Perfect Number")
