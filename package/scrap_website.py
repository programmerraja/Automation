"""This where program begin"""

import os
os.chdir(os.getcwd()+"\\package")
from bs4 import BeautifulSoup as b
import requests as r
import webbrowser as web
import tkinter as t
from tkinter import scrolledtext
from tkinter import messagebox
import package.Tiny_URl  as Tiny_URl 
import package.Sbitly_website as Sbitly_website
import package.facebook_share as facebook_share
import package.facebook_spam as facebook_spam
import time
from pygame import mixer
import package.rps as rps
import pygame

mixer.init()
pygame.init()


class scrap_web:
  def __init__(s):
      s.root=t.Tk()
      s.src=t.IntVar()
      s.no=t.StringVar()
      s.src.set(1)
      s.color="#5cda99"
      s.root.wm_resizable(0,0)
      s.root.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
      s.root.configure(bg=s.color)
      s.root.title("Automation Of Online Jobs")
      s.root.geometry("630x650+320+30")
      mixer.music.load(os.getcwd()+"\\sound\\scrap1.mp3")
      mixer.music.play()
      s.label_intro=t.Label(s.root,text="Select The Website Number  \n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.label_intro.place(x=10,y=150)
      #image
      s.image=t.PhotoImage(file=os.getcwd()+"\\image\\web scrap.png")
      s.label_img=t.Label(s.root,image=s.image,height=130,width=600,bg="white").pack()


      s.label1=t.Label(s.root,text="1.house of bots \n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.label1.place(x=10,y=180)
      
      s.labe2_intro=t.Label(s.root,text="2.fossbytes\n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.labe2_intro.place(x=10,y=200)
      s.labe3_intro=t.Label(s.root,text="3.hackernews\n".upper(),font=("arieal",8,"bold"),bg=s.color)
      s.labe3_intro.place(x=10,y=220)
      s.labe4_intro=t.Label(s.root,text="4.pcmag\n".upper(),font=("arieal",8,"bold",),bg=s.color)
      s.labe4_intro.place(x=10,y=240)
      
      s.label5=t.Label(s.root,text="Enter your choice:",font=("arieal",8,"bold"),bg=s.color)
      s.label5.place(x=10,y=260)
      s.enter_webno=t.Entry(s.root,font=("arieal",8,"bold"),relief="sunken",textvariable=s.src)
      s.enter_webno.place(x=140,y=260,height=20,width=100)
      s.convert_button=t.Button(s.root,text="Enter",command=lambda:s.start(),fg="red",relief="raised")
      s.convert_button.place(x=250,y=260,height=20,width=70)

      s.image1=t.PhotoImage(file=os.getcwd()+"\\image\\cse world.png")
       
      s.label_img1=t.Label(s.root,image=s.image1,bg="white",height=120,width=230).place(x=320,y=140)
      
      s.label6=t.Label(s.root,text="Enter the numbers:",font=("arieal",8,"bold"),bg=s.color)
      s.label6.place(x=20,y=600)
  

      s.text = scrolledtext.ScrolledText(s.root,height=20,width=90,wrap=t.WORD,bg="#ff7188",fg="#000000",font=("garamond",8,"bold"),border=5)
      s.text.place(x=10,y=280)

      
      s.enter_headno=t.Entry(s.root,font=("arieal",8,"bold"),relief="raised",textvariable=s.no)
      s.enter_headno.place(x=160,y=600,height=20,width=100)

      s.exit_button=t.Button(s.root,text="Finished",command=lambda:s.quit(),fg="red",relief="raised")
      s.exit_button.place(x=400,y=600,height=20,width=75)
      #files
      s.file_storage_path=os.getcwd()+"\\text file"
      s.file=open(s.file_storage_path+"\\orginal_link.txt","w")
     
      s.toplevel=t.Toplevel(s.root)
      s.toplevel.title("BOT")
      s.toplevel.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
      s.toplevel.geometry("230x250+0+0")
      s.images=t.PhotoImage(file=os.getcwd()+"\\image\\bot.png")
      
      
      s.label=t.Label(s.toplevel,image=s.images).pack()
      label2=t.Label(s.toplevel,text="NAME: Chotu 7.0 ",font=("garamond",12,"bold"),fg="red").pack()
       
      s.root.mainloop()
  def pcmag(s):
        try: 
         mixer.music.load(os.getcwd()+"\\sound\\scrap2.mp3")
         mixer.music.play()
         s.p=r.get("https://www.pcmag.com").text
         s.soup=b(s.p,features="html.parser")
         k=1
         s.head1=[]
         s.link1=[]
         s.text.insert(t.INSERT,"\t\tThe contents  in pcmag are  \n \n".upper())
         for i in s.soup.find_all("h2"):
           if i.find("a")!=None:
               s.head1.append(i.text)
               s.text.insert(t.INSERT,str(k)+"."+i.text+"\n\n")
        
               s.link1.append(i.find("a").get("href"))
               k+=1
         s.sumbit_button=t.Button(s.root,text="Sumbit",command=lambda:s.printf(s.link1,k,s.head1),fg="red",relief="sunken")
         s.sumbit_button.place(x=300,y=600,height=20,width=70)
        except:
          mixer.music.load(os.getcwd()+"\\sound\\internet_on.mp3")
          mixer.music.play()
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
      
         
  def printf(s,link,k,head1,w=0):
   try:
    link_data=s.no.get()
    if(w!=1):
      for i in link_data.split(","):
              s.file.write(""+str(link[int(i)-1])+"\n")
       
    else:
        for i in link_data.split(","):
           
           s.file.write("https://www.houseofbots.com"+str(link[int(i)-1])+"\n")
       
    s.file.close()
    s.text.delete("1.0",t.END)
    s.enter_headno.delete(0,t.END)
    s.enter_webno.delete(0,t.END)
    
    s.file=open(s.file_storage_path+"\\orginal_link.txt","a")
   except:
    mixer.music.load(os.getcwd()+"\\sound\\valid_num.mp3")
    mixer.music.play()
    messagebox.showinfo("ERROR","Enter A Valid  Number Plse")
  
  def houseofbots(s):
        mixer.music.load(os.getcwd()+"\\sound\\scrap2.mp3")
        mixer.music.play(start=1.0)
        try:
         s.p=r.get("https://www.houseofbots.com").text
         s.soup=b(s.p,features="html.parser")
         k=1
         s.head1=[]
         s.link2=[]
         s.text.insert(t.INSERT,"\t\tThe contents  in house of bots are \n \n".upper())
         for i in s.soup.find_all("li"):
            if i.find("h4")!=None:
              s.head1.append(i.find("h4").text)
              s.text.insert(t.INSERT,str(k)+"."+i.find("h4").text+"\n\n")
              s.link2.append(i.find("a").get("href"))
              k+=1
         s.sumbit_button=t.Button(s.root,text="Sumbit",command=lambda:s.printf(s.link2,k,s.head1,1),fg="red",relief="sunken")
         s.sumbit_button.place(x=300,y=600,height=20,width=70)
        except:
          mixer.music.load(os.getcwd()+"\\sound\\internet_on.mp3")
          mixer.music.play()
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
         
  def fossbytes(s):
      mixer.music.load(os.getcwd()+"\\sound\\scrap2.mp3")
      mixer.music.play(start=1.0)
      try:
       s.p=r.get("https://fossbytes.com").text
       s.soup=b(s.p,features="html.parser")
       k=1
       s.link3=[]
       s.head1=[]
       s.text.insert(t.INSERT,"\t\tThe contents  in fossbytes are \n\n".upper())
       for i in s.soup.find_all("h3"):
          s.text.insert(t.INSERT,str(k)+"."+i.text+"\n\n")
          s.head1.append(i.text)
          s.link3.append(i.find("a").get("href"))
          k+=1
       s.sumbit_button=t.Button(s.root,text="Sumbit",command=lambda:s.printf(s.link3,k,s.head1),fg="red",relief="sunken")
       s.sumbit_button.place(x=300,y=600,height=20,width=70)
      except:
          mixer.music.load(os.getcwd()+"\\sound\\internet_on.mp3")
          mixer.music.play()
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")
          
  def hackernews(s):
       mixer.music.load(os.getcwd()+"\\sound\\scrap2.mp3")
       mixer.music.play(start=1.0)
       try:
        s.p=r.get("https://thehackernews.com").text
        s.soup=b(s.p,features="html.parser")
        k=1
        s. head1=[]
        s. link4=[]
        s.text.insert(t.INSERT,"\t\tThe contents  in hacker news are\n \n".upper())
        for i in s.soup.find_all("h2"):
             s.text.insert(t.INSERT,str(k)+"."+i.text+"\n\n")
             s.head1.append(i.text)
             k+=1
        k=0 
        for i in s.soup.find_all("a",class_='story-link'):
           s.link4.append(i.get("href"))
           k+=1
        s.sumbit_button=t.Button(s.root,text="Sumbit",command=lambda:s.printf(s.link4,k,s.head1),fg="red",relief="sunken")
        s.sumbit_button.place(x=300,y=600,height=20,width=70)
       except:
          mixer.music.load(os.getcwd()+"\\sound\\internet_on.mp3")
          mixer.music.play()
          messagebox.showinfo("ERROR","Plse Make Sure You Have Internet Connection ")  
  def start(s):
    try:
     c=s.src.get()
     if(c==1):
        s.houseofbots()
     elif(c==2):
        s.fossbytes()
     elif(c==3):
      s.hackernews()
     elif(c==4):
        s.pcmag()
     else:
      mixer.music.load(os.getcwd()+"\\sound\\choose_valid.mp3")
      mixer.music.play()
      messagebox.showinfo("ERROR","Choose Valid Option Plse")
    except:
        mixer.music.load(os.getcwd()+"\\sound\\valid_num.mp3")
        mixer.music.play()
        messagebox.showinfo("ERROR","Enter A Valid Number Plse")  
  def quit(s):
    s.root.withdraw()
    s.file.close()
    root=t.Tk()
    root.withdraw()
    mixer.music.load(os.getcwd()+"\\sound\\step-1.mp3")
    mixer.music.play()
    messagebox.showinfo("BOT","Yes! Step 1  Completed Successfully ")
    mixer.music.load(os.getcwd()+"\\sound\\step_2ads.mp3")
    mixer.music.play()
    messagebox.showinfo("BOT","Step 2 Is Making ADS Url!")
    obj= Sbitly_website.test_bitly(s.root)
    if(obj.test()==1):
       if(obj.teardown()==1):
               mixer.music.load(os.getcwd()+"\\sound\\step2.mp3")
               mixer.music.play()
               messagebox.showinfo("BOT","Yes! Step 2  Completed Successfully ")
               time.sleep(2)
               mixer.music.load(os.getcwd()+"\\sound\\step3fb.mp3")
               mixer.music.play()
               messagebox.showinfo("BOT","Step 3 Is Making Non Spam URL To Post In Facebook")
               if(Tiny_URl.tiny_fun(s.root)==1):
                    mixer.music.load(os.getcwd()+"\\sound\\step3.mp3")
                    mixer.music.play()
                    messagebox.showinfo("Bot","Step 3 Is   Completed Sucessfully!")
                    mixer.music.load(os.getcwd()+"\\sound\\final.mp3")
                    mixer.music.play()
                    #obj=facebook_spam()
                    messagebox.showinfo("Bot","Final Step Is Sharing Your Link On Facebook!")
                    obj=facebook_share.test_fb(s.root)
                    if(obj.test()==1):
                      if( obj.teardown()==1):
                        mixer.music.load(os.getcwd()+"\\sound\\finalfb.mp3")
                        mixer.music.play()
                        messagebox.showinfo("Bot","Yes! Final Step  Completed Sucessfully !")
                        os._exit(0)


    
def main():
       root=t.Tk()
       root.wm_resizable(0,0)
       images=t.PhotoImage(file=os.getcwd()+"\\image\\bot.png")
       label=t.Label(root,image=images).pack()
       root.wm_iconbitmap(os.getcwd()+"\\image\\bot_icon.ico")
       root.geometry("230x250+0+0")
       mixer.music.load(os.getcwd()+"\\sound\\intro_bot_g.mp3")
       mixer.music.play()
       label2=t.Label(root,text="NAME: Chotu 7.0 ",font=("garamond",12,"bold"),fg="red").pack()
       msg1=messagebox.showinfo("BOT","HAI I AM YOUR BOT NAME CHOTU VERSION 7.0 ",icon="info")
       msg2=messagebox.askquestion("BOT","Are You Like To Automate The Online Jobs")
       
       if(msg2=="yes"):
         mixer.music.load(os.getcwd()+"\\sound\\intro.mp3")
         mixer.music.play()
         msg3=messagebox.showinfo("BOT","step1: select the  link from famous site")
         root.destroy()
         obj=scrap_web()
       else:
         mixer.music.stop()
         msg3=messagebox.showinfo("BOT","YOU ARE HARD WORKER !")
         msg4=messagebox.askquestion("BOT","Would like To Play With Me")
         if(msg4=="yes"):
           root.destroy()
           g=rps.game()
         root.destroy()
    
       


