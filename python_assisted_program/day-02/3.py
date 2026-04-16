#Bill generation app

#setting constants 
APPLE_GST= 0.12
ORANGE_GST = 0.05

#Enter price and quantity of apples and oranges
buyer_name=input("Enter Buyer Name : ")
apple_price_kg=int(input("Enter apple price per kg: "))
apple_qty_kg=float(input("Enter apple Quantity in kg: "))
orange_price_kg=int(input("Enter apple price per kg: "))
orange_qty_kg=float(input("Enter apple Quantity in kg: "))

print(f"Buyer Name :{buyer_name}")

#calculate total price of apple and orange

total_price_apple=apple_price_kg*apple_qty_kg
total_price_orange=orange_price_kg*orange_qty_kg

#calculate gst of apples and oranges

total_apple_gst = total_price_apple * APPLE_GST
total_orange_gst = total_price_orange* ORANGE_GST

# calculate total amount with gst

total_billing_apple = total_price_apple + total_apple_gst
total_billing_orange = total_price_orange + total_orange_gst

#calculating both apple and orange

total_amount = total_billing_apple + total_billing_orange
total_round_amount = round(total_amount)

print(f"-"*77)
print(f"| {"Item code": ^10} | {"Price/Unit" : ^10} | {" #unit" : ^5} | {"price": ^10} | {"GST":^10} | {"Total w/ GST" : ^10} |")
print(f"-"*77)
print(f"| {"Apple": ^10} | {"Rs " + str(apple_price_kg) : ^10} | {apple_qty_kg : ^5} | {"Rs " + str(total_price_apple): ^10} | {"Rs " + str(total_apple_gst):^10} | {"Rs " + str(total_billing_apple ): ^10} |")
print(f"| {"Orange": ^10} | {"Rs " + str(orange_price_kg) : ^10} | {orange_qty_kg : ^5} | {"Rs " + str(total_price_orange): ^10} | {"Rs " + str(total_orange_gst):^10} | {"Rs " + str(total_billing_orange ): ^10} |")
print(f"-"*77)
print(f"  Total {" " *55}  \u20B9 {total_amount:.2f}")
print(f"  Total Round {" " *50}  \u20B9 {total_round_amount:.2f}")
print(f"-"*77)