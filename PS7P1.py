#Nicholas Rodriguez - 2/19/2026 - PS7P1
#input
principle = float(input("Enter Principle Amount: "))
intRate = float(input("Enter Interest Rate in Decimal Form: "))

#process - before loop
totalInt = 0
print("Year--Start Balance--End Balance")
#process - loop
for count in range (1, 6, 1):
    interest = principle * intRate 
    endBal = principle + interest 
    totalInt += interest
    print(count, "   ", principle, "   ", round(endBal, 2))
    principle = round(endBal, 2)

print("Total Interest Earned: ", round(totalInt, 2))