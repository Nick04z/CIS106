#Nicholas Rodriguez - 3/5/2026 - PS9P5
#Function
def calcAssessVal(userCounty, marketVal):
    if userCounty == "Cook":
        assessPercent = 0.90
    elif userCounty == "DuPage":
        assessPercent = 0.80
    elif userCounty == "McHenry":
        assessPercent = 0.75
    elif userCounty == "Kane":
        assessPercent = 0.60
    else: assessPercent = 0.70

    assessVal = marketVal * assessPercent
    return assessVal

#Main
marketSum = 0
assessSum = 0
    #input
response = input("Use this program to get house prices? (Yes or No): ")
    #process
while response == "Yes":
    userCounty = input("What County is the house located in? ")
    marketVal = float(input("Enter the market value of the house: "))
    assessVal = calcAssessVal(userCounty, marketVal)
    marketSum += marketVal
    assessSum += assessVal
    print("Market Value: $", marketVal)
    print("Assessed Value: $", format(assessVal, '.2f'))
    response = input("Run this program again? (Yes or No): ")

    #output
print("Total Market Values: $", format(marketSum, '.2f'))
print("Total Assessed Values: $", format(assessSum, '.2f'))
