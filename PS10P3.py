#Nicholas Rodriguez - 3/12/2026 - PS10P3
#Function
def calcCommis(salesRev):
    if salesRev <= 100000:
        commisRate = 0.05
    else: commisRate = 0.10
    saleCommis = salesRev * commisRate
    nextYrTarget = salesRev * 1.05
    return saleCommis, nextYrTarget
#Main
    #input
lastName = input("Enter the salesperson's last name: ")
salesRev = float(input("Enter their revenue from sales: "))
    #process
saleCommis, nextYrTarget = calcCommis(salesRev)
    #output
print("Salesperson Last Name:", lastName)
print("Commission Earned: $", format(saleCommis, '.2f'))
print("Next Year's Sales Target: $", format(nextYrTarget, '.2f'))