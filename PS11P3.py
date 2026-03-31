#Nicholas Rodriguez - 3/25/2026 - PS11P3
#Resources: https://www.freecodecamp.org/news/print-newline-in-python/, https://www.w3schools.com/python/python_ref_string.asp, https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3
            #https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string

#Functions
def userInput():
    textList = input("Enter a list of values separated via commas: ")
    return textList

def deleteLeadTrailExSpace(textList):
    finalLine = textList.replace(" ", "")
    return finalLine

def splitList(finalLine):   
    finalList = finalLine.split(",")
    return finalList


def outputList(finalList):
    print('\n'.join(finalList))
    return


#Main
textList = userInput() 
finalLine = deleteLeadTrailExSpace(textList)
finalList = splitList(finalLine)
outputList(finalList)