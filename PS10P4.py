#Nicholas Rodriguez - 3/12/2026 - PS10P4
#Function
def calcAvgScores(gameScore1, gameScore2, gameScore3, handicap):
    avgScore = (gameScore1 + gameScore2 + gameScore3) / 3
    hAvgScore = avgScore + handicap
    return avgScore, hAvgScore
#Main
    #input
lastName = input("Enter the bowler's last name: ")
gameScore1 = float(input("Enter their first game score: "))
gameScore2 = float(input("Enter their second game score: "))
gameScore3 = float(input("Enter their thrid game score: "))
handicap = float(input("Enter the player's handicap value: "))
    #process
avgScore, hAvgScore = calcAvgScores(gameScore1, gameScore2, gameScore3, handicap)
    #output
print("Bowler Last Name:", lastName)
print("Average Score:", avgScore)
print("Average Score w/ Handicap:", hAvgScore)