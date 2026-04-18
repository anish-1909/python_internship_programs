def loan_payment(P,Y,R):
    r=R/100/12
    n=Y*12
    monthly_payment = (P*r*(1+r)**n/((1+r)**n-1))
    return monthly_payment



principal_amount = float(input("Enter the principal amount in rupees: "))
years_to_pay_off=int(input("Enter the duration to pay of the loan in years:"))
annual_interest_rate=float(input("Enter the annual interest(in percentage) : "))



monthly_payment = loan_payment(principal_amount, years_to_pay_off, annual_interest_rate)
print(f"Monthly car loan payment : {monthly_payment:.2f}")

     