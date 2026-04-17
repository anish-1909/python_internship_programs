# EMI Calculator (Screenshot Logic Version)

# 🔹 Input
principal_entered = input("Enter the Principal Amount: ")
roi_entered = input("Enter the Rate of Interest: ")
years_entered = input("Enter the Time in years: ")

# 🔹 Validate + Convert
principal = int(principal_entered) if principal_entered.isdigit() else None
roi = float(roi_entered) if roi_entered.isdigit() else None
years = int(years_entered) if years_entered.isdigit() else None

# 🔹 Check validity
if (principal is not None and roi is not None and years is not None and
    principal > 0 and roi > 0 and years > 0):

    # 🔹 Monthly interest rate
    interest_per_month = round(roi / (12 * 100), 2)

    # 🔹 Total months
    months = years * 12

    # 🔹 EMI calculation
    emi = round(
        principal * interest_per_month * (1 + interest_per_month) ** months /
        ((1 + interest_per_month) ** months - 1),
        2
    )

    # 🔹 Initial balance
    balance = principal

    # 🔹 Header
    print("-" * 65)
    print(f"| {'Month':^8} | {'EMI':^10} | {'Interest':^10} | {'Principal':^10} | {'Balance':^10} |")
    print("-" * 65)

    total_month = 0
    total_emi = 0
    total_interest = 0
    total_principal = 0

    # 🔹 Loop through months
    for month in range(1, months + 1):

        interest = round(balance * roi / (12 * 100), 2)
        principal_paid = round(emi - interest, 2)

        balance = round(balance - principal_paid, 2)

        # 🔹 Fix last month rounding issue
        if balance < 0:
            principal_paid = round(principal_paid + balance, 2)
            emi = round(principal_paid + interest, 2)
            balance = 0

        # 🔹 Totals
        total_month += 1
        total_emi += emi
        total_interest += interest
        total_principal += principal_paid

        # 🔹 Print row
        print(f"| {month:^8} | {emi:^10} | {interest:^10} | {principal_paid:^10} | {balance:^10} |")

    # 🔹 Final totals
    print("-" * 65)
    print(f"| {'Total':^8} | {total_emi:^10.2f} | {total_interest:^10.2f} | {total_principal:^10.2f} | {balance:^10.2f} |")

else:
    print("Invalid Input")