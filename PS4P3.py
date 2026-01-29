#Nicholas Rodriguez - 1/29/2026 - PS4P3

#inputs
numberOfBooks = float(input("Enter Number of Books: "))
bookPrice = float(input("Enter Cost per Book: "))

#process
orderTotal = numberOfBooks * bookPrice
if orderTotal > 50.00:
    shipCharge = 0.00
else: shipCharge = 25.00

#outputs
print("Total Cost of Order: $", orderTotal)
print("Shipping Charge: $", shipCharge)