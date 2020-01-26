import os
import tkinter as t
from tkinter import scrolledtext
from tkinter import messagebox
from pygame import mixer
from email.message import EmailMessage as email
import smtplib as sm
import time 
import pygame
mixer.init()
pygame.init()
class sorry_fb:
  def __init__(s,yes=0):
    if(yes==1):
      s.root=t.Tk()
      s.color="#34ebc9"
      s.root.wm_resizable(0,0)
      s.root.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
      s.root.configure(bg=s.color)
      s.root.title("SORRY FOR PROBLEM ")
      s.root.geometry("420x400+320+30")
      s.image=t.PhotoImage(file=os.getcwd()+"\\image\\spam.png")
      s.label_img=t.Label(s.root,image=s.image,bg=s.color).pack()
      s.text = t.Text(s.root,height=9,width=49,wrap=t.WORD,bg="#ff7188",fg="#000000",font=("garamond",11,"bold"),border=5)
      s.text.place(x=10,y=180)
      lists=["we are sorry to say that we are blocked by Facebook spam because Facebook consider our shorten link as spam so we are unable to share the link on Facebook. Our team working on the problem  soon we get a solution for that. until we suggest you to sharing manually  on any other social media  please.\n\t\t Thank you \n \t\t\t\t\t by \n \t\t\t\t Our Team CSE-II"]
      for i in lists:
       s.text.insert(t.INSERT,i)
      s.text.configure(state="disabled")
      s.button =t.Button(s.root,text="report or feedback",command=lambda:s.mail(1))
    
      s.button.place(x=160,y=370)
      mixer.music.load(os.getcwd()+"\\sound\\spam.mp3")
      mixer.music.play()
      s.root.mainloop()
    else:
      pass
  def mail(s,a=0,r=None):
      if (a==1):
         s.root.destroy()
         s.root=t.Tk()
      elif(a==0):
        r.destroy()
        s.root=t.Tk()
        s.toplevel=t.Toplevel(s.root)
        s.toplevel.title("BOT")
        s.toplevel.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
        s.toplevel.geometry("230x250+0+0")
        s.images=t.PhotoImage(file=os.getcwd()+"\\image\\bot.png")
        s.label=t.Label(s.toplevel,image=s.images).pack()
        s.label2=t.Label(s.toplevel,text="NAME: Chotu 7.0 ",font=("garamond",12,"bold"),fg="red").pack()
        
      s.root.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
      s.root.configure(bg="#34ebc9")
      s.root.title("FEEDBACK ")
      s.root.geometry("420x420+320+30")
      s.image=t.PhotoImage(file=os.getcwd()+"\\image\\feed.png")
      s.label_img=t.Label(s.root,image=s.image,).pack()
      s.label2=t.Label(s.root,text="Enter your Name:",font=("arieal",10,"bold"),bg="#34ebc9")
      s.label2.place(x=10,y=180)
      names=t.StringVar()
      s.entry=t.Entry(s.root,font=("arieal",10,"bold"),relief="raised",textvariable=names)
      s.entry.place(x=124,y=180)
      s.text = t.Text(s.root,height=9,width=49,wrap=t.WORD,bg="#ff7188",fg="#000000",font=("garamond",13,"bold"),border=5)
      s.text.place(x=10,y=200)
      s.button =t.Button(s.root,text="Send",command=lambda:s.send(names))
      s.button.place(x=170,y=390)
  def send(s,names): 
    f=open(os.getcwd()+"\\text file\\feedback.txt","w")
    f.write(str(s.text.get(1.0,t.END)))
    f.close()
    try:
      msg=email()
      msg["subject"]="feedback "+names.get()+" user"
      msg["from"]="kesavaperumal73@gmail.com"
      msg["to"]="boooathis123@gmail.com"
      with open(os.getcwd()+"\\text file\\feedback.txt","r")as f:
              file=f.read()
              bs = file.encode('utf-8')
      msg.add_attachment(bs,maintype="text",subtype=".txt")
      with sm.SMTP_SSL("smtp.gmail.com",465) as smtp:
          smtp.login("kesavaperumal73@gmail.com","keselvan")
          smtp.send_message(msg)
      messagebox.showinfo("Thank you","Meaasgae Sent Sucessfully!")
      mixer.music.load(os.getcwd()+"\\sound\\thankyou.mp3")
      mixer.music.play()
      os._exit(0)
    except:
     mixer.music.load(os.getcwd()+"\\sound\\internet_on.mp3")
     mixer.music.play()
     messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")

if "___name__"=="__main__":
   a=sorry_fb()

