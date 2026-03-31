#Nicholas Rodriguez - 3/19/2026 - PS11P2
#Resources: https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string; https://www.w3schools.com/python/; https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3

#Functions
def userInput():
    txtLine = input("Enter a line of text: ")
    return txtLine

def deleteExtra(txtLine):
    leadTrailLine = txtLine.strip()
    finalLine = " ".join(leadTrailLine.split())
    return finalLine

def reverseFunction(finalLine):
    reverseLine = "".join(reversed(finalLine))
    return reverseLine

def outputLine(reverseLine):
    print(reverseLine)
    return

#Main
txtLine = userInput()
finalLine = deleteExtra(txtLine)
reverseLine = reverseFunction(finalLine)
outputLine(reverseLine)
