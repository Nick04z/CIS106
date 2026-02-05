#Nicholas Rodriguez - 2/5/2026 - PS5P3

#input
principleCD = float(input("Enter the Prinicple Amount of a CD: "))
maturityYrs = float(input("Enter the Number of Years to Maturity: "))

#process
if principleCD > 100000 and maturityYrs == 5:
    intRate = .06
elif principleCD >= 50000 and principleCD <= 100000:
    if maturityYrs == 10:
        intRate = .05
    elif maturityYrs == 5:
        intRate = .04
    else: intRate = .02 
else: intRate = .02

firstYrInt = principleCD * intRate

#output
print("Your Principle: $", principleCD)
print("Interest Rate: ", intRate*100, "%")
print("Interest Amount for the First Year: $", firstYrInt)