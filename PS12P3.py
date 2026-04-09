#Nicholas Rodriguez - 4/7/2026 - PS12P3

#Functions
def displayNameScore(lastName, personScore):
    for i in range(len(lastName)):
        print(lastName[i], "-- Score:", personScore[i])
    return

def highLowScores(lastName, personScore):
    highVar = -1.0
    lowVar = 99999.99
    for y in range(len(lastName)):
        if float(personScore[y]) > float(highVar):
            highIndex = y
            highVar = personScore[y]
        if float(personScore[y]) < float(lowVar):
            lowIndex = y
            lowVar = personScore[y]
    print("Highest Score:", lastName[highIndex], "at", personScore[highIndex])
    print("Lowest Score: ", lastName[lowIndex], "at", personScore[lowIndex])
    
#Main
file = open("PS12P3_data.txt", "r")
lastName = []
personScore = []


fileLastName = str(file.readline().rstrip('\n'))

while fileLastName != "":
    lastName.append(fileLastName)
    fileScore = float(file.readline())
    personScore.append(fileScore)
    fileLastName = str(file.readline().rstrip('\n'))
    file.close

displayNameScore(lastName, personScore)
highLowScores(lastName, personScore)