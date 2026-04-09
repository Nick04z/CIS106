#Nicholas Rodriguez - 4/8/2026 - PS12P4P5

#Functions
def displayArrays(playerNames, batAvg):
    for i in range(len(playerNames)):
        print("Player Name:", playerNames[i], "-- Batting Average:", batAvg[i])
    return

def searchFunction(playerNames, batAvg, searchName):
    searchIndex = -1
    for y in range(len(playerNames)):
        if playerNames[y] == searchName:
            searchIndex = y 

    if searchIndex == -1:
        print("Name not found")
    else: print("Results:", playerNames[searchIndex], "-- Batting Average:", batAvg[searchIndex])

#Main
file = open("PS12P4_P5_data.txt", "r")
playerNames = []
batAvg = []

fileName = str(file.readline().rstrip('\n'))
while fileName != "":
    playerNames.append(fileName)
    fileAvg = float(file.readline())
    batAvg.append(fileAvg)
    fileName = str(file.readline().rstrip('\n'))
    file.close

displayArrays(playerNames, batAvg)

searchQuestion = input("Would you like to search for a specfic player? (Y or N) ")
while searchQuestion == "Y":
    searchName = input("Enter a name: ")
    searchFunction(playerNames, batAvg, searchName)
    searchQuestion = input("Search again? (Y or N) ")