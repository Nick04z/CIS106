#Nicholas Rodriguez - 1/29/2026 - PS4P4

#inputs
appName = input("Enter Name of Appliance: ")
appCost = float(input("Enter Cost of the Appliance: "))

#process
if appCost > 1000.00:
    warrentCost = appCost * 0.10
else: warrentCost = appCost * 0.05

totalPrice = appCost + warrentCost

#outputs
print("Appliance Name: ", appName)
print("Cost of Appliance: $", appCost)
print("Warrantee Cost: $", warrentCost)
print("Total Cost: $", totalPrice)