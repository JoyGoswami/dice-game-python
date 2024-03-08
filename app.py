import random
from tkinter import *

root = Tk()
root.title('Dice Game')
root.geometry("600x600")

# -------------------functionality--------------------
currentScore = 0
activePlayer = 0
score = [0,0]
isGameOn = True

def switchPlayer():
    global currentScore
    global activePlayer

    currentScore = 0
    if activePlayer == 0:
        player0CurrentScore.config(text= 0)
        activePlayer = 1
    else:
        player1CurrentScore.config(text= 0)
        activePlayer = 0

def displayMsg():
    if activePlayer == 0:
        winMsg.config(text="Player 1 Won")
        winMsg.pack()
    else:
        winMsg.config(text="Player 2 Won")
        winMsg.pack()

def handleRoll():
    if isGameOn:
        randDiceNum = random.randint(1,6)

        # display the randon dice number to the dice label 
        dice.config(text=randDiceNum)

        # check if the rand num is not 1, then add it and display it to current score
        # if rand num is not 1, change the player
        if randDiceNum != 1:
            global currentScore
            global activePlayer
            currentScore = currentScore + randDiceNum
            
            if activePlayer == 0:
                player0CurrentScore.config(text= currentScore)
            else:
                player1CurrentScore.config(text= currentScore)
        else:
            switchPlayer()
        print(activePlayer)

def handleHold():
    global isGameOn
    if isGameOn:
        score[activePlayer] = score[activePlayer] + currentScore
        if score[activePlayer] >= 20:
            print("player won")
            displayMsg()
            isGameOn = False
        else:
            if activePlayer == 0:
                player0Score.config(text= score[activePlayer])
            else:
                player1Score.config(text= score[activePlayer])
        print(score)
        dice.config(text="Roll the Dice")
        switchPlayer()

def handleReset():
    global currentScore, score, isGameOn, activePlayer
    activePlayer = 0
    isGameOn = True
    currentScore = 0
    score = [0,0]
    player0Score.config(text= 0)
    player1Score.config(text= 0)
    player0CurrentScore.config(text= 0)
    player1CurrentScore.config(text= 0)
    dice.config(text="Roll the Dice")


#----------------win frame------------------
winMsg = Label(root, text="Won")
winMsg.config(font=("Roboto", 25))
winMsg.pack_forget()

    
#--------------player 1 frame--------------
player0Frame = Frame(root, width=200, height=250, highlightbackground="red", highlightthickness="3")
player0Frame.pack_propagate(False)
player0Frame.place(x=100, y=100)

player0Name = Label(player0Frame, text="Player 1", pady="20")
player0Name.config(font=("Roboto", 25))
player0Name.pack()

player0Score = Label(player0Frame, text="0")
player0Score.pack()
player0Score.config(font=("Roboto", 25))

player0CurrentScoreLabel = Label(player0Frame, text="Current Score", pady="10")
player0CurrentScoreLabel.pack()
player0CurrentScoreLabel.config(font=("Roboto", 15))

player0CurrentScore = Label(player0Frame, text="0")
player0CurrentScore.pack()
player0CurrentScore.config(font=("Roboto", 15))

#--------------player 2 frame--------------
player1Frame = Frame(root, width=200, height=250, highlightbackground="red", highlightthickness="3")
player1Frame.pack_propagate(False)
player1Frame.place(x=320, y=100)

player1Name = Label(player1Frame, text="Player 2", pady="20")
player1Name.config(font=("Roboto", 25))
player1Name.pack()

player1Score = Label(player1Frame, text="0")
player1Score.pack()
player1Score.config(font=("Roboto", 25))

player1CurrentScoreLabel = Label(player1Frame, text="Current Score", pady="10")
player1CurrentScoreLabel.pack()
player1CurrentScoreLabel.config(font=("Roboto", 15))

player1CurrentScore = Label(player1Frame, text="0")
player1CurrentScore.pack()
player1CurrentScore.config(font=("Roboto", 15))
#--------------Buttons frame--------------



btnFrame = Frame(root, width=420, height=150, highlightbackground="red", highlightthickness="3")
btnFrame.pack_propagate(False)
btnFrame.place(x=100, y=350)

dice = Label(btnFrame, text="0", pady="20")
dice.config(font=("Roboto", 25))
dice.pack()

rollBtn = Button(btnFrame, text="Roll", width=10, height=10, command = handleRoll)
rollBtn.config(font=("Roboto", 15))
rollBtn.pack(side="left")

holdBtn = Button(btnFrame, text="Hold", width=10, height=10, command=handleHold)
holdBtn.config(font=("Roboto", 15))
holdBtn.pack(side="left")

resetBtn = Button(btnFrame, text="Reset", width=10, height=10, command=handleReset)
resetBtn.config(font=("Roboto", 15))
resetBtn.pack(side="left")





root.mainloop()