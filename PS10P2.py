#Nicholas Rodriguez - 3/12/2026 - PS10P2
#Function
def calcExamPoints(examScore1, examScore2, examScore3):
    totalPoints = examScore1 + examScore2 + examScore3
    avgScore = totalPoints / 3
    return totalPoints, avgScore

#Main
    #input
lastName = input("Enter your last name: ")
examScore1 = float(input("Enter your first exam score: "))
examScore2 = float(input("Enter your second exam score: "))
examScore3 = float(input("Enter your third exam score: "))
    #process
totalPoints, avgScore = calcExamPoints(examScore1, examScore2, examScore3)
    #output
print("Student Last Name:", lastName)
print("Total Points:", totalPoints)
print("Average Score:", avgScore)