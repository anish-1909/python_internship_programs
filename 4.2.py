def calculate_interest(principal, roi, frequency=12):
    return round(principal * roi / (frequency * 100), 2)

def calculate_emi(principal, roi, time):
    interest_per_month = calculate_interest(1, roi)
    months = time * 12

    emi = round(
        principal * interest_per_month * (1 + interest_per_month) ** months /
        ((1 + interest_per_month) ** months - 1),
        2
    )
    return emi

print(f"EMI for Principal: 1000, ROI: 10, Years: 1 is {calculate_emi(1000,10,1)}")

