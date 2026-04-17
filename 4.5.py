# Logical Block 1: Interest Calculation
def calculate_interest(principal, roi, frequency=12):
    if principal < 0 or roi < 0:
        return 0

    interest = principal * roi * frequency / 100
    return interest



# Logical Block 2: EMI Calculation

def calculate_emi(principal, annual_rate, time):
    if principal <= 0 or annual_rate <= 0 or time <= 0:
        return 0

    monthly_rate = annual_rate / (12 * 100)   # convert % to monthly decimal
    months = time * 12

    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi



# Logical Block 3: EMI Details

def generate_emi_details(principal, roi, time):
    emi = calculate_emi(principal, roi, time)
    balance = principal
    emi_details = []

    months = time * 12
    monthly_rate = roi / (12 * 100)

    for i in range(1, months + 1):
        interest = balance * monthly_rate
        principal_paid = emi - interest
        balance -= principal_paid

        emi_dict = {
            "Month": i,
            "EMI": emi,
            "Interest": interest,
            "Principal": principal_paid,
            "Balance": max(balance, 0)  # avoid negative due to rounding
        }

        emi_details.append(emi_dict)

    return emi_details


# Logical Block 4: Display Table

def display_emi_details(emi_details):

    if not emi_details:
        print("No EMI Details")
        return

    print("\n" + "-" * 70)
    print(f"| {'Month':^8} | {'EMI':^12} | {'Interest':^12} | {'Principal':^12} | {'Balance':^12} |")
    print("-" * 70)

    total_emi = total_interest = total_principal = 0

    for row in emi_details:
        print(f"| {row['Month']:^8} | {row['EMI']:^12.2f} | {row['Interest']:^12.2f} | "
              f"{row['Principal']:^12.2f} | {row['Balance']:^12.2f} |")

        total_emi += row["EMI"]
        total_interest += row["Interest"]
        total_principal += row["Principal"]

    print("-" * 70)
    print(f"| {'Total':^8} | {total_emi:^12.2f} | {total_interest:^12.2f} | "
          f"{total_principal:^12.2f} | {'-':^12} |")
    print("-" * 70)



# Logical Block 5: Main Program

def main():
    

    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Annual Interest Rate (%): "))
    time = int(input("Enter Time (in years): "))

    emi_details = generate_emi_details(principal, rate, time)

    display_emi_details(emi_details)


# Run program
if __name__ == "__main__":
    main()