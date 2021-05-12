import random
import tkinter as tk
from tkinter import ttk
from tkinter import tix
import timeit
import time

##==================       WINDOW  ==============
main= tk.Tk()
main.title('Stone Paper Scissors')
main.geometry('1200x450')

###===============         Storage  ====================

humanScore=0
compScore=0
humanChoice=""
compChoice=""

##==================   HUMAN  INTERACTION  =============

def paperChose():
    global humanChoice
    humanChoice=""
    humanChoice='paper'
    cpuTurn()

def scissorsChose():
    global humanChoice
    humanChoice=""
    humanChoice='scissors'
    cpuTurn()

def stoneChose():
    global humanChoice
    humanChoice=""
    humanChoice='stone'
    cpuTurn()



## =================   CPU AUTO TURN   ================
def cpuTurn():
    global compChoice
    compChoice=''
    time.sleep(1)
    a= random.randint(0,2)
    if a==0:
        compChoice='stone'
    elif a==1:
        compChoice='paper'
    else:
        compChoice='scissors'

    checkResult()

##==============      functionality  +++++++++++++++++++++
def checkResult():
    global humanChoice
    global compChoice
    global humanScore
    global compScore
    if humanChoice=="stone" and compChoice=='scissors':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Scissors",You Won!!')
        screen.configure(fg='green')
        humanScore+=1
    elif humanChoice=="paper" and compChoice=='stone':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Stone",You Won!!')
        screen.configure(fg='green')
        humanScore+=1
    elif humanChoice=="scissors" and compChoice=='paper':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Stone",You Won!!')
        screen.configure(fg='green')
        humanScore+=1

    elif compChoice=="stone" and humanChoice=='scissors':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Stone",You Lost!!')
        screen.configure(fg='red')
        compScore+=1
    elif compChoice=="paper" and humanChoice=='stone':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Paper",You Lost!!')
        screen.configure(fg='red')
        compScore+=1
    elif compChoice=="scissors" and humanChoice=='paper':
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,'Computer chose "Scissors",You Lost!!')
        screen.configure(fg='red')
        compScore+=1

    elif humanChoice==compChoice:
        if screen.get() != '':
            screen.delete(0,tk.END)
        screen.insert(tk.END,f'Computer chose {compChoice} , it\'s a TIE.')
        screen.configure(fg='black')
    score()
    

##=====================            Control win             =======================
screen = tk.Entry(main,borderwidth=10,font='condensed 32',fg='Green',bg='Yellow')
screen.pack(side=tk.TOP,fill='both')

Label = tix.Label(main,text="Please Choose, it's your turn now.",font='Rockwell 15 bold',fg='Maroon')
Label.pack()

Stonebtn = tix.Button(main,text='Stone',width=11,padx=5,pady=5,font='TimesNewRoman 15 bold',fg='Red',command=stoneChose)
Stonebtn.pack(anchor='n')

Paperbtn = tix.Button(main,text='Paper',width=11,padx=5,pady=5,font='TimesNewRoman 15 bold',fg='Red',command=paperChose)
Paperbtn.pack(anchor='n')

Scissorsbtn = tix.Button(main,text='Scissors',width=11,padx=5,pady=5,font='TimesNewRoman 15 bold',fg='Red',command=scissorsChose)
Scissorsbtn.pack(anchor='n')


def score():
    ScoreCard= tix.Label(main,text=f"Your WINS:{humanScore}\nComputer WINS:{compScore}",font='Georgia 32')
    ScoreCard.pack()
    screen.update()
    time.sleep(1)
    ScoreCard.destroy()
    
 





main.mainloop()