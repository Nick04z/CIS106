#Nicholas Rodriguez - 3/5/2026 - PS9P1
#Function
def calcNextMonSales(dateMonth, salesAmt):
    if dateMonth == "January" or dateMonth == "Feburary" or dateMonth == "March":
        forecastPercent = 0.10
    elif dateMonth == "April" or dateMonth == "May" or dateMonth == "June":
        forecastPercent = 0.15
    elif dateMonth == "July" or dateMonth == "August" or dateMonth == "September":
        forecastPercent = 0.20
    else: forecastPercent = 0.25

    nextMonSales = salesAmt * (1 + forecastPercent)
    return nextMonSales


    
#Main
    #input
response = input("Run this Program? (Yes or No)")
    #process
while response == "Yes":
    lastName = input("Enter your Last Name: ")
    dateMonth = input("Enter the current month: ")
    salesAmt = float(input("Enter the number of sales for this month: "))

    nextMonSales = calcNextMonSales(dateMonth, salesAmt)
    print("The Sales for Next Month should be: $", format(nextMonSales, '.2f'))
    response = input("Run the Program Again? (Yes or No)")

print("Thank You for using this program!")