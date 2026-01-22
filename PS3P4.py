# Nicholas Rodriguez - 1/22/2026

#inputs
carmake = input("Make of the Auto: ")
carmodel = input("Model of the Auto: ")
msrpamount = float(input("Enter MSRP: "))
discountpercent = float(input("Enter Discount Percent as a Decimal: "))

#process
amountoff = msrpamount * discountpercent
disprice = msrpamount - amountoff

#outputs
print("Make: ", carmake)
print("Model: ", carmodel)
print("MSRP: ", msrpamount)
print("Discount Percent", discountpercent)
print("Amount Taken Off", amountoff)
print("Discounted Price: $", disprice)