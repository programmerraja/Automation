import os,time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox as msg
import package.passwords as passwords
from pygame import mixer
import package.facebook_spam as facebook_spam
obj=facebook_spam.sorry_fb()
class test_bitly:
    try:
      storage_path=os.getcwd()+"\\text file"
      
      def __init__(self,feedback):
        self.feedback=feedback
        mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
        mixer.music.play()
        try:
         self.driver=webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
         self.driver.get("https://sbitly.com/auth/signin")
         self.file =open(test_bitly.storage_path+"\\orginal_link.txt","r")
         self.file2=open(test_bitly.storage_path+"\\shortenurl.txt","w")
        except:
            mixer.music.load(os.getcwd()+"\\sound\\sbitly_drive.mp3")
            mixer.music.play()
            msg.showinfo("ERROR","Something Went Wrong While Opening In Chrome Drive In Bitly Code")
            obj.mail(o,self.feedback)
      def test(self):
          mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
          mixer.music.play(start=30)
          try:
               self.elem =self.driver.find_element_by_name("username")
               self.elem.clear()
               self.elem.send_keys(passwords.user_name)
               self.elem.send_keys(Keys.RETURN)
               self.elem2=self.driver.find_element_by_name("password")
               self.elem2.clear()
               self.elem2.send_keys(passwords.password_bitly)
               self.elem2.send_keys(Keys.RETURN)
               try:
                    self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Log out'])[1]/following::span[1]").click()
               except:
                   pass
               finally:
                for i in self.file.readlines():
                   self.link=self.driver.find_element_by_name("url")
                   self.link.send_keys(str(i))
                   self.driver.find_element_by_id("shorten").submit()
                   time.sleep(5)
                   self.soup=BeautifulSoup(self.driver.page_source,features="html.parser")
                   for k in self.soup.find_all("input",{"class":"form-control input-lg"}):
                         time.sleep(2)
                         self.file2.write(k["value"]+"\n")  
                         time.sleep(5)
                   self.link.clear()
                   time.sleep(5)
                return 1

                
          except:
                 mixer.music.load(os.getcwd()+"\\sound\\log_in_sbitly.mp3")
                 mixer.music.play() 
                 msg.showinfo("ERROR","Loging Failed In Sbitly Website")
                 obj.mail(0,self.feedback)
                 return 0
      def teardown(self):
          mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
          mixer.music.play(start=1.0)
          try:
               self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='English (United States)'])[1]/following::span[1]").click()
               self.driver.find_element_by_link_text("Log out").click()
               time.sleep(2)
               self.file2.close()
               self.file.close()
               self.driver.close()
               return 1
               
          except:
               mixer.music.load(os.getcwd()+"\\sound\\log_out_sbitly.mp3")
               mixer.music.play()
               msg.showinfo("ERROR","Log Out Failed In Bitly Code")
               obj.mail(0,self.feedback)
               return 0
    except:
          mixer.music.load(os.getcwd()+"\\sound\\sbitly_error.mp3")
          mixer.music.play()
          m=msg.showinfo("BOT","Sounds Bad! In Sbitly Code")
          obj.mail(0,self.feedback)  
if "__name__"=="__main__":
  obj=test_bitly()
  obj.test()
  obj.teardown()


