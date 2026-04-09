#Nicholas Rodriguez - 4/2/2026 - PS12P1P2

#Function
def displayLastNames(lastNames, examScores):
    for i in range(len(lastNames)):
        print(lastNames[i], "got a score of", examScores[i])
    return

def displayReverse(lastNames, examScores):
        print("Reverse Order: ") 
        reverseLName = lastNames[::-1]
        reverseScore = examScores[::-1]
        for i in range(len(reverseLName)):
            print(reverseLName[i], "got a score of", reverseScore[i])
     

        return

#Main
lastNames = ["Rodriguez", "Roden", "Desai", "George", "Toosley", "Parker", "Brock", "Ketchum", "Robinson", "Watterson"]
examScores = ["98", "80", "100", "95", "78", "97", "74", "65", "77", "52"]
displayLastNames(lastNames, examScores)
print("\n")
displayReverse(lastNames, examScores)

