from selenium import webdriver
import os,time
from bs4 import BeautifulSoup
from pynput.keyboard import Key,Controller
from tkinter import messagebox as m
from pygame import mixer
import package.facebook_spam as facebook_spam
obj=facebook_spam.sorry_fb()
def tiny_fun(feedback):
     storage_path=os.getcwd()+"\\text file"
     try:
        mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
        mixer.music.play()
        board=Controller()
        file3=open(storage_path+"\\tinyurl.txt","w")
        file2=open(storage_path+"\\shortenurl.txt","r")
        driver = webdriver.Chrome()
        driver.get("https://tinyurl.com/")
        mu=0
        for i in file2.readlines():
            driver.find_element_by_id("url").clear()
            elem2=driver.find_element_by_id("url")
            elem2.send_keys(str(i))
            board.press(Key.enter)
            board.release(Key.enter)
            time.sleep(1)
            soup=BeautifulSoup(driver.page_source,features="html.parser")
            
            for k in soup.find_all("a",{"id":"copy_div"}):
                file3.write(k["data-clipboard-text"])
                file3.write("\n")
                time.sleep(5)
                if(mu>4):
                      mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
                      mixer.music.play()
                mu+=1
       
        file3.close()
        file2.close()
        driver.close()
        return 1
     except :
          mixer.music.load(os.getcwd()+"\\sound\\sbitly_drive.mp3")
          mixer.music.play()
          m=m.showinfo("BOT","OOPS! Problem In Tiny URL ")
          obj.mail(0,feedback)
          return 0    
if "__name__"=="__main__":
  tiny_fun()

