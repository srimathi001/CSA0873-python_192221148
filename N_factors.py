def find_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def print_first_N_factors(num, N):
    factors = find_factors(num)
    print("Number of factors =", len(factors))
    print("1st", N, "factors are:", ", ".join(map(str, factors[:N])))
given_number = int(input("enter a number:"))
N = int(input("enter N value:"))
print_first_N_factors(given_number,N)
