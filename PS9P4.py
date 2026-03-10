#Nicholas Rodriguez - 3/5/2026 - PS9P4
#Function
def calcTicketPrice(milesFromChi):
    if milesFromChi >= 30:
        ticketPrice = 12.00
    elif milesFromChi >= 20 and milesFromChi <= 29:
        ticketPrice = 10.00
    elif milesFromChi >= 10 and milesFromChi <= 19:
        ticketPrice = 8.00
    else: ticketPrice = 5.00

    return ticketPrice
#Main
ticketPriceSum = 0
    #input
response = input("Run this program to get train ticket prices? (Yes or No): ")
    #process
while response == "Yes":
    lastName = input("Enter your last name: ")
    milesFromChi = float(input("How many miles are you from downtown Chicago? "))
    ticketPrice = calcTicketPrice(milesFromChi)
    ticketPriceSum += ticketPrice

    print("Last Name:", lastName)
    print("Price of Ticket: $", format(ticketPrice, '.2f'))
    response = input("Run again for another ticket price? (Yes or No): ")

    #output
print("The total price of all the tickets you entered is $", format(ticketPriceSum, '.2f'))
