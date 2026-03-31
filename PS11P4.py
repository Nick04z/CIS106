#Nicholas Rodriguez - 3/30/2026 - PS11P4
#Resources: https://www.w3schools.com/python/python_ref_string.asp; https://realpython.com/len-python-function/#:~:text=To%20get%20the%20length%20of,1%2C%202%2C%203%5D)%20.; 
# https://phoenixnap.com/kb/python-repeat-string#:~:text=To%20create%20a%20function%20for,repetition%20is%20the%20output%20value.; https://www.quora.com/How-do-you-attempt-shifting-letters-in-Python;
#https://www.geeksforgeeks.org/python/python-right-and-left-shift-characters-in-string/

#Functions
def userInputs():
    userTxt = input("Enter a line of text: ")
    charPerLine = int(input("Enter the number of characters per line: "))
    numOfLines = int(input("Enter the number of lines to be printed: "))
    scrollDirect = input("Enter scroll direction (Left or Right): ")
    return userTxt, charPerLine, numOfLines, scrollDirect


def duplicateTxt(userTxt, charPerLine):
    numOfReps = int((charPerLine/len(userTxt))+1)
    dupeTxt = userTxt * numOfReps
    repeatTxt = dupeTxt[:charPerLine]
    return repeatTxt

def printAndShiftLines(repeatTxt, numOfLines):
    lineCount = 1
    print(repeatTxt)
    while lineCount < numOfLines:
        if scrollDirect == "Left": 
            repeatTxt = repeatTxt[1:] + repeatTxt[0]
            print(repeatTxt)
        elif scrollDirect == "Right":
            repeatTxt = repeatTxt[-1:] + repeatTxt[:-1]
            print(repeatTxt)
        lineCount += 1
        
    return
    

#Main
userTxt, charPerLine, numOfLines, scrollDirect = userInputs()
repeatTxt = duplicateTxt(userTxt, charPerLine)
printAndShiftLines(repeatTxt, numOfLines)
#print(repeatTxt)