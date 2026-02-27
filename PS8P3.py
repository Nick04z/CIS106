#Nicholas Rodriguez - 2/26/2026 - PS8P3
#Function
def calcMilesPerGal(milesTrav, gasGallons):
    milesPerGal = milesTrav /gasGallons
    return milesPerGal
#Main
tripCount = 0
    #input
response = input("Run this Program to calculate miles per gallon? (Yes or No)")
    #process
while response == "Yes":
    cityDest = input("Enter your destination city: ")
    milesTrav = float(input("Enter the amount of miles you travelled: "))
    gasGallons = float(input("Enter the gallons of gas you used on your trip: "))

    milesPerGal = calcMilesPerGal(milesTrav, gasGallons)
    tripCount += 1

    print("Destination City:", cityDest)
    print("Miles Travelled:", milesTrav)
    print("Miles per Gallon:", milesPerGal, "mpg")
    response = input("Run the program again? (Yes or No)")

    #output
print("Number of Trips:", tripCount)