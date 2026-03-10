#Nicholas Rodriguez - 3/5/2026 - PS9P3
#Function
def calcOutOfDoor(carMake, carModel, electricCode, carMSRP):
    if electricCode == "Y":
        msrpPercentOff = 0.30
    elif carMake == "Honda" and carModel == "Accord":
        msrpPercentOff = 0.10
    elif carMake == "Toyota" and carModel == "Rav4":
        msrpPercentOff = 0.15
    else: msrpPercentOff = 0.05

    msrpDiscount = carMSRP * msrpPercentOff
    newMSRP = carMSRP - msrpDiscount
    outOfDoorPrice = newMSRP + (newMSRP * 0.07)
    return outOfDoorPrice
#Main
msrpSum = 0
salePriceSum = 0
    #input
response = input("Use this program to determine the price of your car? (Yes or No): ")
    #process
while response == "Yes":
    carMake = input("Enter your car's Make: ")
    carModel = input("Enter the model of your car: ")
    electricCode = input("Enter the Electric Vehicle Code (Y or N): ")
    carMSRP = float(input("Enter the car's MSRP: "))
    outOfDoorPrice = calcOutOfDoor(carMake, carModel, electricCode, carMSRP)

    msrpSum += carMSRP
    salePriceSum += outOfDoorPrice
    print("The sales price for the car is $", format(outOfDoorPrice, '.2f'))
    response = input("Run the Program again? (Yes or No): ")
    #output
print("The sum of all your MSRP's is $", format(msrpSum, '.2f'))
print("Meanwhile, the sum of every sales price is $", format(salePriceSum, '.2f'))