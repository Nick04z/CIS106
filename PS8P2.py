#Nicholas Rodriguez - 2/26/2026 - PS8P2
#Function
def calcBatAvg(hitAmt, atBats):
    batAvg = hitAmt / atBats
    return batAvg
#Main
playerCount = 0
    #input
response = input("Would you like to run this Program? (Yes or No)")
    #Process
while response == "Yes":
    lastName = input("Enter Player Last Name:")
    hitAmt = float(input("Enter number of hits:"))
    atBats = float(input("Enter the player's At Bats:"))
    batAvg = calcBatAvg(hitAmt, atBats)

    playerCount += 1 
    print("Player's Last Name:", lastName)
    print("Batting Average:", batAvg)
    response = input("Repeat this Program? (Yes or No)")
    #output
print("Number of Players entered:", playerCount)