
from random import randint
from main import *

class scores:

    def __init__(self, run=0):
        self._run = run

    def addRun(self, run):
        self._run += run

    def getScores(self):
        return self._run

def userBatsFirst():
    compBowlingNum = randint(1, 6)
    userBatingNum = int(input("Please Enter your Bating number:"))
    userScore = scores()
    while userBatingNum != compBowlingNum:
        if userBatingNum in range(1, 7):
            userScore.addRun(userBatingNum)
            print("Computer's Bowling number is %d" % compBowlingNum, "\t \t",
                  "Current User Score: %s" % userScore.getScores())
            userBatingNum = int(input("Please Enter your Bating number:"))
            compBowlingNum = randint(1, 6)
        else:
            print("Please enter your batting num in range 1-6")
            userBatingNum = int(input("Please Enter your Bating number:"))
    target = userScore.getScores() + 1
    print("Computer's Bowling number is %d" % compBowlingNum)
    print("You got out. Computer need to score %d to WIN." % target)

    compBatingNum = randint(1, 6)
    userBowlingNum = int(input("Please Enter your Bowling number:"))
    compScore = scores()
    while compBatingNum != userBowlingNum and compScore.getScores() < target:
        if userBowlingNum in range(1, 7):
            compScore.addRun(compBatingNum)
            print("Computer's batting number is %d" % compBatingNum, "\t \t",
                  "Current Comp Score: %s" % compScore.getScores())
            userBowlingNum = int(input("Please Enter your Bowling number:"))
            compBatingNum = randint(1, 6)
        else:
            print("Please enter your bowling num in range 1-6")
            userBowlingNum = int(input("Please Enter your Bowling number:"))

    print("Computer's batting number is %d" % compBatingNum)
    print("Computer's total score is %d" % compScore.getScores())

    if compScore.getScores() > target:
        return "Comp WON"
    elif compScore.getScores() == target:
        return "It is a TIE"
    elif compScore.getScores() < target:
        return "User WON"


def userBowlsFirst():
    compBatingNum = randint(1, 6)
    userBowlingNum = int(input("Please Enter your Bowling number:"))
    compScore = scores()
    while compBatingNum != userBowlingNum:
        if userBowlingNum in range(1, 7):
            compScore.addRun(compBatingNum)
            print("Computer's batting number is %d" % compBatingNum, "\t \t",
                  "Current Comp Score: %s" % compScore.getScores())
            userBowlingNum = int(input("Please Enter your Bowling number:"))
            compBatingNum = randint(1, 6)
        else:
            print("Please enter your bowling num in range 1-6")
            userBowlingNum = int(input("Please Enter your Bowling number:"))

    target = compScore.getScores() + 1
    print("Computer's batting number is %d" % compBatingNum)
    print("Computer got Out. You need %d runs to WIN." % target)

    compBowlingNum = randint(1, 6)
    userBatingNum = int(input("Please Enter your Bating number:"))
    userScore = scores()
    while userBatingNum != compBowlingNum and userScore.getScores() < target:
        if userBatingNum in range(1, 7):
            userScore.addRun(userBatingNum)
            print("Computer's Bowling number is %d" % compBowlingNum, "\t \t",
                  "Current User Score: %s" % userScore.getScores())
            userBatingNum = int(input("Please Enter your Bating number:"))
            compBowlingNum = randint(1, 6)
        else:
            print("Please enter your batting num in range 1-6")
            userBatingNum = int(input("Please Enter your Bating number:"))

    print("Computer's Bowling number is %d" % compBowlingNum)
    print("User's total score is %d" % userScore.getScores())

    if userScore.getScores() > target:
        return "User WON"
    elif userScore.getScores() == target:
        return "It is a TIE"
    elif userScore.getScores() < target:
        return "Comp WON"


def toss():
    print("Let's have a toss.")
    print("Press O to select \"Odd\".")
    print("Press E to select \"Even\".")
    userToss = input("Press O or E: ")
    if userToss == "O":
        toss = "Odd"
        print("You have selected Odd.")
    elif userToss == "E":
        toss = "Even"
        print("You have selected EVEN.")
    print("If sum of your number and computer's number is %s, you will win the toss." % toss)
    usertossNum = int(input("Please enter your move number between 1 to 6, inclusive: "))
    comptossNum = randint(1, 6)
    print("Computer choose the number", comptossNum)
    tossSum = usertossNum + comptossNum
    if tossSum % 2 != 0 and userToss == "O":
        return "userWin"
    elif tossSum % 2 == 0 and userToss == "E":
        return "UserWin"
    else:
        return "CompWin"


def playersDecides(selectedOption):
    if selectedOption == "1":  # player decide to bat frist
        return "bat"

    elif selectedOption == "2":  # player decide to bowl frist
        return "bowl"

