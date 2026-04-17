# PROG 4.4: Display EMI Details

# Function to display the Monthly EMI, Interest, Principal and Balance
# for the given number of years in a tabular format
def display_emi_details(emi_details):

    # Step 1: Display the header for the table
    print(f"{'-' * 65}")
    print(f"| {'Month':^8} | {'EMI':^10} | {'Interest':^10} "
          f"| {'Principal':^10} | {'Balance':^10} |")
    print(f"{'-' * 65}")

    # Step 2: Initialize totals
    total_month = total_emi = total_interest = total_principal = 0.0

    # Step 3: Loop through EMI details
    for emi_dict in emi_details:

        # Step 4: Extract values from dictionary
        month = emi_dict["Month"]
        emi = emi_dict["EMI"]
        interest = emi_dict["Interest"]
        principal = emi_dict["Principal"]
        balance = emi_dict["Balance"]

        # Step 5: Update totals
        total_month += 1
        total_emi += emi
        total_interest += interest
        total_principal += principal

        # Step 6: Print each row
        print(f"| {month:^8} | {emi:^10} | {interest:^10} "
              f"| {principal:^10} | {balance:^10} |")

    # Step 7: Display footer (totals)
    print(f"{'-' * 65}")
    print(f"| {'Total':^8} | {total_emi:^10.2f} | {total_interest:^10.2f} "
          f"| {total_principal:^10.2f} | {balance:^10.2f} |")
    print(f"{'-' * 65}")



display_emi_details(compute_emi_details(10000, 10, 1))