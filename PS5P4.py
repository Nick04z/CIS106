#Nicholas Rodriguez - 2/5/2026 - PS5P4

#input
ticketQty = float(input("Enter your Quantity of Concert Tickets: "))

#process
if ticketQty >= 25:
    ticketPrice = 50
elif ticketQty >= 10 and ticketQty <= 24:
    ticketPrice = 60
elif ticketQty >= 5 and ticketQty <= 9:
    ticketPrice = 70
else: ticketPrice = 75

totalCost = ticketQty * ticketPrice

#output
print("Number of Tickets: ", ticketQty)
print("Price per Ticket: $", ticketPrice)
print("Total Cost of Tickets: $", totalCost)