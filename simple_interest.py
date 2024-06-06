def calculate_simple_interest(principal, time, gender, is_senior):
    senior_citizen_rate = 0.15  # 15%
    female_rate = 0.12  # 12%
    default_rate = 0.10  # 10%
    if is_senior.lower() == 'y':
        rate = senior_citizen_rate
    elif gender.lower() == 'f':
        rate = female_rate
    else:
        rate = default_rate
    interest = principal * rate * time
    
    return interest
principal = float(input("Enter the principal amount: "))
time = int(input("Enter the number of years: "))
gender = input("Gender (m/f): ")
is_senior = input("Is the customer a senior citizen (y/n)? ")
interest = calculate_simple_interest(principal, time, gender, is_senior)
print(f"Interest: {interest:.2f}")
