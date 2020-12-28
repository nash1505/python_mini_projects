from tkinter import *

import random #import thw random package
root = Tk()



option = ["Rock","Paper","Scissor"] # created list for storing the value of computer choices 

cs = 0 # computer score to store the computer score
us = 0 # user score to store the user score
def Rock(): # defined the rock function when rock button click
    global cs # cs varible declare as the global variable 
    global us # us varible declare as the global variable 
    computer = random.randrange(3)  # created computer choice with random function upto 3
    if computer == 0:  # checking the condition with computer option it is same as user the return tie
        res.set("tie")
       
    elif computer == 1: # checking the condition with computer option it is differnt 
        res.set("Computer Win")
        cs +=1 #increament the value of computer score
        compscore.set(cs)
    else:
        
        res.set("You Win")
        us +=1 #increament the value of user score
        userscore.set(us)
    
def Paper():   # defined the paper function when paper button click
    global cs # cs varible declare as the global variable
    global us # us varible declare as the global variable
    computer = random.randrange(3)
    if computer == 1:
        res.set("tie")
    elif computer == 2:
        res.set("Computer Win")
        cs +=1
        compscore.set(cs)
    else:
        res.set("You Win")
        
        us +=1
        userscore.set(us)
        
        
        
def Scissor(): # defined the scissor function when scissor button click
    global cs 
    global us
    computer = random.randrange(3)
    if computer == 2:
        res.set("tie")
    elif computer == 0:
        cs +=1
        compscore.set(cs)
        res.set("Computer Win")
    else:
        res.set("You Win")
        us +=1
        userscore.set(us)
        
        
        
        
        
        

root.title("Rock,Paper,Scissor")





res = StringVar() 
Result = Label(root,text="XXXXXXX",textvariable=res) # label for result of the game
Result.grid(row=1,column=2) 

Button(root,text="Rock",width="10",command=Rock).grid(row=3,column=1) # button for rock
Button(root,text="paper",width="10",command=Paper).grid(row=3,column=2) # button for paper
Button(root,text="Scissor",width="10",command=Scissor).grid(row=3,column=3) # button for Scissor
compscore = StringVar()



Label(root,text="Computer Score").grid(row=3,column=4)

ComputerScore = Label(root,text="",textvariable=compscore) # here it shows the score of the computer


ComputerScore.grid(row=4,column=4)


userscore = StringVar()
UserScore = Label(root,text="",textvariable=userscore) # here it shows the score of the user
Label(root,text="User Score").grid(row=3,column=5)
UserScore.grid(row=4,column=5)


root.mainloop()