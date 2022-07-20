##Author- Aatman Rangrej
#this application is a hand cricket game.

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from widgets import *
from random import randint
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.uix.image import Image
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp


Window.size = (1080,720)



class EvenButton(MDLabel):
    pass
class OddButton(MDLabel):
    pass
class EvenLabel(MDLabel):
    pass
class OddLabel(MDLabel):
    pass
class orLabel(MDLabel):
    pass
class confirmButton(MDLabel):
    pass

class hand1(MDLabel):
    pass
class hand2(MDLabel):
    pass
class hand3(MDLabel):
    pass
class hand4(MDLabel):
    pass
class hand5(MDLabel):
    pass
class hand6(MDLabel):
    pass
class tossResult(MDLabel):
    pass
class Continue(MDLabel):
    pass



class Toss(Screen):
    actions = Builder.load_string(actionsInToss)

    def run(self):

        with open("savePlayerName.txt", "r") as file:
            for last_line in file:
                pass
        self.ids.abc.text = last_line + ", please make your selection."
        file.close()

        self.add_widget(EvenButton())
        self.add_widget(OddButton())
        self.add_widget(EvenLabel())
        self.add_widget(OddLabel())
        self.add_widget(orLabel())
        self.ids.oddButton.disabled = False
        self.ids.evenButton.disabled = False
        self.ids.haveToss.disabled = False


    def even(self):
        self.ids.toss1.text = "You have selected Even."
        self.add_widget(confirmButton())

    def odd(self):
        self.ids.toss1.text = "You have selected Odd."
        self.add_widget(confirmButton())

    def haveToss(self):
        if self.ids.toss1.text == "You have selected Odd.":
            self.ids.tossPrint.text = "Comp Player selects Even."
        elif self.ids.toss1.text == "You have selected Even.":
            self.ids.tossPrint.text = "Comp Player selects Odd."
        self.ids.oddButton.disabled = True
        self.ids.evenButton.disabled = True

        self.add_widget(hand1())
        self.ids.hand1.disabled = False
        self.add_widget(hand2())
        self.ids.hand2.disabled = False
        self.add_widget(hand3())
        self.ids.hand3.disabled = False
        self.add_widget(hand4())
        self.ids.hand4.disabled = False
        self.add_widget(hand5())
        self.ids.hand5.disabled = False
        self.add_widget(hand6())
        self.ids.hand6.disabled = False
        self.ids.LetsHaveToss.disabled = True

        self.add_widget(tossResult())

        pass

    def initiateToss1(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand1.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" Comp Won the Toss."

        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 1" + "     "+ "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def initiateToss2(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand2.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" Comp Won the Toss."
        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 2"+ "     "+ "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def initiateToss3(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand3.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text =  " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: "+ str(tossSum) +" Result: "+" Comp Won the Toss."
        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 3"+ "     "+ "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def initiateToss4(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand4.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text = " Total: "+str(tossSum) + " Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: "+str(tossSum) + " Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: "+str(tossSum) + " Result: "+" Comp Won the Toss."
        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 4" + "     " + "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def initiateToss5(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand5.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text = " Total: " + str(tossSum) + " Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: " + str(tossSum) + " Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: " + str(tossSum) + " Result: "+" Comp Won the Toss."
        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 5" + "     " + "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def initiateToss6(self):
        if self.ids.toss1.text == "You have selected Odd.":
            toss = "O"
        elif self.ids.toss1.text == "You have selected Even.":
            toss = "E"
        comptossNum = randint(1, 6)
        usertossNum = int(self.ids.hand6.text)
        tossSum = usertossNum + comptossNum
        if tossSum % 2 != 0 and toss == "O":
            self.ids.tossResult.text = " Total: "+ str(tossSum) + " Result: "+" You Won the Toss."
        elif tossSum % 2 == 0 and toss == "E":
            self.ids.tossResult.text = " Total: "+ str(tossSum) + " Result: "+" You Won the Toss."
        else:
            self.ids.tossResult.text = " Total: "+ str(tossSum) + " Result: "+" Comp Won the Toss."
        self.ids.hand1.disabled = True
        self.ids.hand2.disabled = True
        self.ids.hand3.disabled = True
        self.ids.hand4.disabled = True
        self.ids.hand5.disabled = True
        self.ids.hand6.disabled = True
        self.ids.userSelection.text = "You selected number: 6" + "     " + "Comp selected number: "+ str(comptossNum)
        self.add_widget(Continue())
        self.ids.Continue.disabled = False

    def ContinueTo(self):
        self.File = open("saveTossResult.txt", "w")
        self.File.write(self.ids.tossResult.text)
        self.File.close()
        self.File = open("saveTossResult.txt", "r")
        printText = self.File.readline()

        self.File = open("savePlayerName.txt", "a")
        self.File.write("\t" + printText[18::1])
        self.File.close()


        if printText[18::1] == " Comp Won the Toss." or printText[19::1] == " Comp Won the Toss.":
            self.manager.current = "PlayGame"
        elif printText[18::1] == " You Won the Toss." or printText[19::1] == " You Won the Toss.":
            self.manager.current = "TossSelection"





class Mainscreen(Screen):
    def run(self):
        self.manager.current = "Screen2"
        self.manager.transition.direction = "left"
        self.ids.PlayGame.disabled = True



class PlayGameScreen(Screen):
    playerName = ObjectProperty(None)


    def Name_MDDialog(self):
        confirmButton = MDRectangleFlatButton(text = "YES", on_press = self.Confirm)
        reEnterButton = MDRectangleFlatButton(text="CLOSE", on_press = self.Close)

        self.dialog1 = MDDialog(title = "Player's Name", text = self.playerName.text, buttons = [confirmButton, reEnterButton])
        self.dialog1.open()

    def Confirm(self, obj):
        self.manager.current = "TossScreen"
        self.manager.transition.direction = "down"
        self.File = open("savePlayerName.txt", "a")
        self.File.write(self.playerName.text)
        self.ids.playerName.text = " "
        self.File.close()
        self.dialog1.dismiss()


    def Close(self, obj):
        self.ids.playerName.text = " "
        self.dialog1.dismiss()



class BatFirst(MDLabel):
    pass

class BowlFirst(MDLabel):
    pass



class TossSelection(Screen):
    action = Builder.load_string(actionsInTossSelection)
    def run(self):
        self.File = open("saveTossResult.txt", "r")
        printText = self.File.readline()
        self.ids.printText.text = printText[18::1]



        if printText[18::1] == " You Won the Toss." or printText[19::1] == " You Won the Toss.":
            self.add_widget(BatFirst())
            self.add_widget(BowlFirst())

        self.ids.batFirst.disabled = False
        self.ids.bowlFirst.disabled = False


    def userBatsFirst(self):
        self.manager.current = "PlayGame"
        self.File = open("TossSelection.txt", "w")
        self.File.write("bat")
        self.File.close()
        pass

    def userBowlsFirst(self):
        self.manager.current = "PlayGame"
        self.File = open("TossSelection.txt", "w")
        self.File.write("bowl")
        self.File.close()
        pass



class HowToPlay(Screen):

    def run(self):
        self.ids.PlayScroll.text = "XYZ"



class Aboutscreen(Screen):
    pass

class Statistics(Screen):

    def run(self):
        pass
    pass







class scores:

    def __init__(self, run=0):
        self._run = run

    def addRun(self, run):
        self._run += run

    def getScores(self):
        return self._run

compScore = scores()
userScore = scores()



class PlayGame(Screen):

    def run(self):
        self.File = open("TossSelection.txt", "r")
        tossSelection = self.File.readline()
        compSelection = int(randint(0, 1))

        if tossSelection == "bat":
            self.ids.printSelection.text = "You selected to Bat first."

        elif tossSelection == "bowl":
            self.ids.printSelection.text = "You selected to Bowl first."

        else:
            if compSelection == 0:
                self.ids.printSelection.text = "Comp selected to Bat first."
            elif compSelection == 1:
                self.ids.printSelection.text = "Comp selected to Bowl first."

        self.File = open("savePlayerName.txt", "a")
        self.File.write("\t" + self.ids.printSelection.text)
        self.File.close()

        self.File = open("TossSelection.txt", "w")
        self.File.write(self.ids.printSelection.text)
        self.File.close()

        self.add_widget(hand1())
        self.ids.Hand1.disabled = False
        self.add_widget(hand2())
        self.ids.Hand2.disabled = False
        self.add_widget(hand3())
        self.ids.Hand3.disabled = False
        self.add_widget(hand4())
        self.ids.Hand4.disabled = False
        self.add_widget(hand5())
        self.ids.Hand5.disabled = False
        self.add_widget(hand6())
        self.ids.Hand6.disabled = False
        self.ids.tossSelectionRun.disabled = True


    def gamePlay(self):
        self.ids.handP.opacity = 1
        if self.ids.userSelects.text == "1":
            self.ids.handP.source = "finger1-removebg.png"
        elif self.ids.userSelects.text == "2":
            self.ids.handP.source = "finger2-removebg.png"
        elif self.ids.userSelects.text == "3":
            self.ids.handP.source = "finger3-removebg.png"
        elif self.ids.userSelects.text == "4":
            self.ids.handP.source = "finger4-removebg.png"
        elif self.ids.userSelects.text == "5":
            self.ids.handP.source = "finger5-removebg.png"
        elif self.ids.userSelects.text == "6":
            self.ids.handP.source = "finger6-removebg.png"

        compNum = randint(1, 6)
        self.ids.handC.opacity = 1
        if compNum == 1:
            self.ids.handC.source = "finger1-removebg.png"
        elif compNum == 2:
            self.ids.handC.source = "finger2-removebg.png"
        elif compNum == 3:
            self.ids.handC.source = "finger3-removebg.png"
        elif compNum == 4:
            self.ids.handC.source = "finger4-removebg.png"
        elif compNum == 5:
            self.ids.handC.source = "finger5-removebg.png"
        elif compNum == 6:
            self.ids.handC.source = "finger6-removebg.png"




        userNum = int(self.ids.userSelects.text)

        if self.ids.printSelection.text == "You selected to Bat first.":
            if compNum != userNum:
                self.userBats(compNum, userNum)
                print("User score: " + str(userScore.getScores()))
            elif compNum == userNum:
                target = userScore.getScores() + 1
                print("target set by User", target)
                printTarget = "Target set by User " + str(target)
                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + printTarget)
                self.File.close()
                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title = "You are Out", text = "Comp needs "+str(target)+" runs to WIN.", buttons = [OkButton], auto_dismiss = False)
                self.outDialogBox.open()

        elif self.ids.printSelection.text == "You selected to Bowl first.":
            if compNum != userNum:
                self.userBowls(compNum, userNum)
                print("Comp score: " + str(compScore.getScores()))
            elif compNum == userNum:
                target = compScore.getScores() + 1
                print("target set my Comp", target)
                printTarget = "Target set by Comp " + str(target)
                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + printTarget)
                self.File.close()
                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title="Comp got Out", text="You need " + str(target) + " runs to WIN.", buttons=[OkButton], auto_dismiss = False)
                self.outDialogBox.open()

        elif self.ids.printSelection.text == "Comp selected to Bat first.":
            if compNum != userNum:
                self.userBowls(compNum, userNum)
                print("Comp score: " + str(compScore.getScores()))
            elif compNum == userNum:
                target = compScore.getScores() + 1
                print("target set by Comp:", target)
                printTarget = "Target set by Comp " + str(target)
                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + printTarget)
                self.File.close()
                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title="Comp got Out", text="You need " + str(target) + " runs to WIN.", buttons=[OkButton], auto_dismiss = False)
                self.outDialogBox.open()


        elif self.ids.printSelection.text == "Comp selected to Bowl first.":
            if compNum != userNum:
                self.userBats(compNum, userNum)
                print("User score: " + str(userScore.getScores()))
            elif compNum == userNum:
                target = userScore.getScores() + 1
                print("target set my User", target)
                printTarget = "Target set by User " + str(target)
                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + printTarget)
                self.File.close()
                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title="You got Out", text="Comp needs " + str(target) + " runs to WIN.", buttons=[OkButton], auto_dismiss = False)
                self.outDialogBox.open()


        if userScore.getScores() > 0:
            self.ids.printPlayerScore.text = "Your Score: "+str(userScore.getScores())
        if compScore.getScores() > 0:
            self.ids.printCompScore.text = "Comp Score: "+str(compScore.getScores())



    def userBowls(self, compNum, userNum):
         compScore.addRun(compNum)

    def userBats(self, compNum, userNum):
        userScore.addRun(userNum)

    def Hand1(self):
        self.ids.userSelects.text = "1"
        self.gamePlay()

    def Hand2(self):
        self.ids.userSelects.text = "2"
        self.gamePlay()

    def Hand3(self):
        self.ids.userSelects.text = "3"
        self.gamePlay()


    def Hand4(self):
        self.ids.userSelects.text = "4"
        self.gamePlay()

    def Hand5(self):
        self.ids.userSelects.text = "5"
        self.gamePlay()

    def Hand6(self):
        self.ids.userSelects.text = "6"
        self.gamePlay()

    def Ok(self, obj):
        self.outDialogBox.dismiss()
        self.manager.current = "PlayGame2"




class PlayGame2(Screen):

    def run(self):
        self.add_widget(hand1())
        self.ids.Hand1.disabled = False
        self.add_widget(hand2())
        self.ids.Hand2.disabled = False
        self.add_widget(hand3())
        self.ids.Hand3.disabled = False
        self.add_widget(hand4())
        self.ids.Hand4.disabled = False
        self.add_widget(hand5())
        self.ids.Hand5.disabled = False
        self.add_widget(hand6())
        self.ids.Hand6.disabled = False
        self.ids.tossSelectionRun.disabled = True

        self.File = open("TossSelection.txt", "r")
        secondinnings = self.File.readline()

        if secondinnings == "You selected to Bat first.":
            self.ids.printInnings.text = "It is your Bowling now."
        elif secondinnings == "You selected to Bowl first.":
            self.ids.printInnings.text = "It is your Batting now."
        elif secondinnings == "Comp selected to Bat first.":
            self.ids.printInnings.text = "It is your Batting now."
        elif secondinnings == "Comp selected to Bowl first.":
            self.ids.printInnings.text = "It is your Bowling now."


    def gamePlay(self):

        self.ids.handP.opacity = 1
        if self.ids.userSelects.text == "1":
            self.ids.handP.source = "finger1-removebg.png"
        elif self.ids.userSelects.text == "2":
            self.ids.handP.source = "finger2-removebg.png"
        elif self.ids.userSelects.text == "3":
            self.ids.handP.source = "finger3-removebg.png"
        elif self.ids.userSelects.text == "4":
            self.ids.handP.source = "finger4-removebg.png"
        elif self.ids.userSelects.text == "5":
            self.ids.handP.source = "finger5-removebg.png"
        elif self.ids.userSelects.text == "6":
            self.ids.handP.source = "finger6-removebg.png"

        compNum = randint(1, 6)
        self.ids.handC.opacity = 1
        if compNum == 1:
            self.ids.handC.source = "finger1-removebg.png"
        elif compNum == 2:
            self.ids.handC.source = "finger2-removebg.png"
        elif compNum == 3:
            self.ids.handC.source = "finger3-removebg.png"
        elif compNum == 4:
            self.ids.handC.source = "finger4-removebg.png"
        elif compNum == 5:
            self.ids.handC.source = "finger5-removebg.png"
        elif compNum == 6:
            self.ids.handC.source = "finger6-removebg.png"

        userNum = int(self.ids.userSelects.text)

        self.File = open("TossSelection.txt", "r")
        secondinnings = self.File.readline()



        if secondinnings == "You selected to Bat first.":
            target = userScore.getScores() + 1
            if compNum != userNum:
                compScore.addRun(compNum)
                print("Comp score: " + str(compScore.getScores()))
            if compNum == userNum or compScore.getScores() >= target :
                if compScore.getScores() >= target:
                    difference = compScore.getScores() - userScore.getScores()
                    result = "Comp WON the Game. Better Luck next time."
                    result1 = "User Lost by %d runs." % difference
                elif compScore.getScores() == target - 1:
                    result = "It is a TIE!"
                elif compScore.getScores() < target - 1:
                    difference = userScore.getScores() - compScore.getScores()
                    result = "You WON the Game. Congratulations"
                    result1 = "Comp Lost by %d runs." % difference

                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title=result,text = result1, buttons=[OkButton], auto_dismiss=False)
                self.outDialogBox.open()

                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + result[0:18] + "\t" + result1 + "\n")
                self.File.close()



        elif secondinnings == "You selected to Bowl first.":
            target = compScore.getScores() + 1
            if compNum != userNum:
                userScore.addRun(userNum)
                print("Comp score: " + str(compScore.getScores()))
            if compNum == userNum or userScore.getScores() >= target:
                if userScore.getScores() >= target:
                    difference = userScore.getScores() - compScore.getScores()
                    result = "You WON the Game. Congratulations"
                    result1 = "Comp Lost by %d runs." % difference
                elif userScore.getScores() == target - 1:
                    result = "It is a TIE!"
                elif userScore.getScores() < target - 1:
                    difference = compScore.getScores() - userScore.getScores()
                    result = "Comp WON the Game. Better Luck next time."
                    result1 = "User Lost by %d runs." % difference

                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title=result, text =result1, buttons=[OkButton], auto_dismiss=False)
                self.outDialogBox.open()

                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + result[0:18] + "\t" + result1 + "\n")
                self.File.close()

        elif secondinnings == "Comp selected to Bat first.":
            target = compScore.getScores() + 1
            if compNum != userNum:
                userScore.addRun(userNum)
                print("Comp score: " + str(compScore.getScores()))
            if compNum == userNum or userScore.getScores() >= target:
                if userScore.getScores() >= target:
                    difference = userScore.getScores() - compScore.getScores()
                    result = "You WON the Game. Congratulations"
                    result1 = "Comp Lost by %d runs." % difference
                elif userScore.getScores() == target - 1:
                    result = "It is a TIE!"
                elif userScore.getScores() < target - 1:
                    difference = compScore.getScores() - userScore.getScores()
                    result = "Comp WON the Game. Better Luck next time."
                    result1 = "User Lost by %d runs." % difference

                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title=result,text = result1, buttons=[OkButton], auto_dismiss=False)
                self.outDialogBox.open()

                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + result[0:18] + "\t" + result1 + "\n")
                self.File.close()

        elif secondinnings == "Comp selected to Bowl first.":
            target = userScore.getScores() + 1
            if compNum != userNum:
                compScore.addRun(compNum)
                print("User score: " + str(userScore.getScores()))
            if compNum == userNum or compScore.getScores() >= target:
                if compScore.getScores() >= target:
                    difference = compScore.getScores() - userScore.getScores()
                    result = "Comp WON the Game. Better Luck next time."
                    result1 = "User Lost by %d runs." % difference
                elif compScore.getScores() == target - 1:
                    result = "It is a TIE!"
                elif compScore.getScores() < target - 1:
                    difference = userScore.getScores() - compScore.getScores()
                    result = "You WON the Game. Congratulations"
                    result1 = "Comp Lost by %d runs." % difference

                OkButton = MDRectangleFlatButton(text="OK", on_press=self.Ok)
                self.outDialogBox = MDDialog(title=result, text = result1, buttons=[OkButton], auto_dismiss=False)
                self.outDialogBox.open()

                self.File = open("savePlayerName.txt", "a")
                self.File.write("\t" + result[0:18] + "\t" + result1 + "\n")
                self.File.close()




        self.ids.printPlayerScore.text = 'Your Score: '+str(userScore.getScores())

        self.ids.printCompScore.text = "Comp score: "+str(compScore.getScores())



    def Hand1(self):
        self.ids.userSelects.text = "1"
        self.gamePlay()

    def Hand2(self):
        self.ids.userSelects.text = "2"
        self.gamePlay()

    def Hand3(self):
        self.ids.userSelects.text = "3"
        self.gamePlay()


    def Hand4(self):
        self.ids.userSelects.text = "4"
        self.gamePlay()

    def Hand5(self):
        self.ids.userSelects.text = "5"
        self.gamePlay()

    def Hand6(self):
        self.ids.userSelects.text = "6"
        self.gamePlay()

    def Ok(self, obj):
        self.outDialogBox.dismiss()
        self.ids.Hand1.disabled = True
        self.ids.Hand2.disabled = True
        self.ids.Hand3.disabled = True
        self.ids.Hand4.disabled = True
        self.ids.Hand5.disabled = True
        self.ids.Hand6.disabled = True






sm = ScreenManager()

sm.add_widget(Mainscreen(name='Screen0'))
sm.add_widget(PlayGameScreen(name='Screen2'))
sm.add_widget(HowToPlay(name='Screen3'))
sm.add_widget(Aboutscreen(name='about'))
sm.add_widget(Statistics(name="stats"))
sm.add_widget(Toss(name="TossScreen"))
sm.add_widget(TossSelection(name = "TossSelection"))
sm.add_widget(PlayGame(name = "PlayGame"))
sm.add_widget(PlayGame2(name = "PlayGame2"))


class HandCricketApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.screen = Builder.load_string(screens)

        return self.screen


HandCricketApp().run()
File1 = open("saveTossResult.txt", "w")
File1.write("")
File1.close()
File = open("TossSelection.txt", "w")
File.write("")
File.close()

