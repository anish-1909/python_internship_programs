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

# 🔹 EMI details
def compute_emi_details(principal, roi, time):
    emi_details = []
    emi = calculate_emi(principal, roi, time)
    balance = principal

    for month in range(1, time * 12 + 1):

        interest = calculate_interest(balance, roi, 12)
        principal_paid = emi - interest
        balance = balance - principal_paid

        if balance < 0:
            principal_paid += balance
            emi = principal_paid + interest
            balance = 0

        emi_dict = {
            "Month": month,
            "EMI": round(emi, 2),
            "Interest": round(interest, 2),
            "Principal": round(principal_paid, 2),
            "Balance": round(balance, 2)
        }

        emi_details.append(emi_dict)

    return emi_details  #  outside loop

emi_details = compute_emi_details(1000, 10, 1)

print("\nEMI Details:")
for row in emi_details:
    print(row)

import json
emi_details_json = json.dumps(emi_details)

print("\nJSON Payload:")
print(json.dumps(json.loads(emi_details_json), indent=2))