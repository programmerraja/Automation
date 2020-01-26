import tkinter as t
import random
import os 
from tkinter import messagebox as b
from pygame import mixer
import pygame
mixer.init()
pygame.init()

class game:
        def __init__(s):
             s.root=t.Tk()
             color="orange"
             s.root.wm_resizable(0,0)
             s.root.configure(bg=color)
             s.root.geometry("470x320+320+30")
             s. root.title("ROCK PAPPER SCISSORS")
             s.man=0
             s.robo1=0
             s.score=t.Label( s.root,text="Score",font=("arieal",20,"italic"),bg=color)
             s.score.grid(row=0,column=0)
             s.man1=t.Label(text="You",font=("arieal",15,"italic"),bg=color)
             s. man1.grid(row=1,column=0)
             s.score1=t.Label(text=":"+str(s.man),font=("arieal",15,"italic"),bg=color)
             s.score1.grid(row=1,column=1)
             s.robo=t.Label(text="Chotu 7.0",font=("arieal",15,"italic"),bg=color)
             s.robo.grid(row=2,column=0)
             s.score2=t.Label(text=":"+str(s.robo1),font=("arieal",15,"italic"),bg=color)
             s.score2.grid(row=2,column=1)
             s.status=t.Label(s.root,text="",font=("arieal",15,"italic"),bg=color)
             s.status.grid(row=3,column=1)
          
             s.scssisor_image=t.PhotoImage(file=os.getcwd()+"\\image\\scissors.png")
             s.scissor=t.Button( s.root,height=140,width=140,image=s.scssisor_image,command=lambda:s.check("scissor"),relief="groove")
             s.scissor.grid(row=4,column=0)

             s.rock_image=t.PhotoImage(file=os.getcwd()+"\\image\\rock.png")
             s.rock=t.Button( s.root,width=140,height=140,image=s.rock_image,command=lambda:s.check("rock"),relief="groove")
             s.rock.grid(row=4,column=1)

             s.paper_image=t.PhotoImage(file=os.getcwd()+"\\image\\paper.png")
             s.paper=t.Button( s.root,width=140,height=140,image=s.paper_image,command=lambda:s.check("paper"),relief="groove")
             s.paper.grid(row=4,column=2)

             s.f=t.Frame(height=10,width=20,bg=color).grid()
             s.status["text"]="CLICK ANY ONE ! "
             s.about=t.Label(text="Made by @CSE-II ",fg="black",bg="green").grid(row=6,column=1)
             mixer.music.load(os.getcwd()+"\\sound\\rps music.mp3")
             mixer.music.play()
             s.root.mainloop()
        def score_check(s):
            if  s.man ==20:
              b.showinfo("RESULT ","MMM! YOU WON THE BATTLE!!!")
              msg=b.askquestion("BOT","Would like To Play Again With Me")
              if(msg=="no"):
                      b.showinfo("BYE","Thank you For Play")
                      os._exit(0)
              s. man=0
              s.score1["text"]=":"+str( s.man)
              s.robo1=0
              s.score2["text"]=":"+str( s.robo1)
              s.status["text"]=" " 
            elif s.robo1==20:
              b.showinfo("RESULT","YEAH!!!  I WON THE BATTLE!!!")
              msg=b.askquestion("BOT","Would like To Play Again With Me")
              if(msg=="no"):
                      b.showinfo("BYE","Thank you For Play")
                      os._exit(0)
              s.man=0
              s.score1["text"]=":"+str( s.man)
              s.robo1=0
              s.score2["text"]=":"+str( s.robo1)
              s.status["text"]=" "
        def check(s,choice):
         s.score_check()
         s.computer=random.choice(["rock","paper","scissor"])
         if( choice=="rock"):
            if( s.computer=="rock"):
                 s.status["text"]="  It's a draw       ".upper()
            elif( s.computer=="paper"):
                 s.robo1=s.robo1+1
                 s.score2["text"]=":"+str( s.robo1)
                 s.status["text"]="  YOU LOOSE !     "
            elif(s.computer=="scissor"):
                 s.man+=1
                 s.score1["text"]=":"+str(s.man)
                 s.status["text"]="  YOU WON !        "
         elif( choice=="paper"):
            if( s.computer=="rock"):
                 s. man+=1
                 s.score1["text"]=":"+str(s.man)
                 s.status["text"]="  YOU WON !        "
            elif(s.computer=="paper"):
                 s.status["text"]="  It's a draw      ".upper()
            elif( s.computer=="scissor"):
                 s.robo1=s.robo1+1
                 s.score2["text"]=":"+str( s.robo1)
                 s.status["text"]="  YOU LOOSE !    "
         elif(choice=="scissor"):
            if( s.computer=="rock"):
                  s.robo1=s.robo1+1
                  s.score2["text"]=":"+str(s.robo1)
                  s.status["text"]="  YOU LOOSE !    "
            elif( s.computer=="paper"):
                 s.man+=1
                 s.score1["text"]=":"+str(s.man)
                 s.status["text"]="  YOU WON !       "
            elif( s.computer=="scissor"):
                 s.status["text"]="  It's a draw      ".upper()
         
         s.score_check()
    
if "__name__"=="__main__":         
  g=game()
