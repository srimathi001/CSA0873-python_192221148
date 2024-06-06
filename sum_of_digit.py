def sum(numbers):
    total_sum = 0
    for num in numbers:
        if 10 <= num < 100 and num % 10 < 10:
            total_sum += num
    return total_sum
numbers_list = [12, 45, 7, 89, 23, 6, 54, 9]
result = sum(numbers_list)
print("Sum of two-digit numbers less than 10:", result)
