from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from tkinter import messagebox
import tkinter as t
from pygame import mixer
import package.passwords as passwords
import package.facebook_spam as facebook_spam

import tkinter as t
class test_fb:

      storage_path=os.getcwd()+"\\text file"
      
      def __init__(self,feedback):
       self.feedback=feedback
       mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
       mixer.music.play(start=0.45)
       try:
         self.driver=webdriver.Chrome(os.getcwd()+"\\chromedriver.exe")
         self.driver.get("https://facebook.com/home.php")
         self.file2=open(test_fb.storage_path+"\\tinyurl.txt","r")
         self.test()
       except:
            
             mixer.music.load(os.getcwd()+"\\sound\\fb_login.mp3")
             mixer.music.play()
             messagebox.showinfo("ERROR","Something Went Wrong In Opening Chrome Driver")
             obj.mail(0,self.feedback)
            
      def test(self):
            mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
            mixer.music.play(start=0.45)
            try:
               self.elem =self.driver.find_element_by_name("email")
               self.elem.clear()
               self.elem.send_keys(passwords.fb_name)
               
               self.elem2=self.driver.find_element_by_name("pass")
               self.elem2.clear()
               self.elem2.send_keys(passwords.fb_pass)
               self.elem2.send_keys(Keys.RETURN)
               time.sleep(60)
               for i in self.file2.readlines():
                     self.driver.find_element_by_xpath("//textarea[@name='xhpc_message']").click()
                     self.driver.find_element_by_xpath("//textarea[@name='xhpc_message']").clear()
                     self.driver.find_element_by_xpath("//textarea[@name='xhpc_message']").send_keys(str(i))
                     self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='caution-solid'])[1]/following::button[1]").click()
                     time.sleep(1)
            except:
                  mixer.music.load(os.getcwd()+"\\sound\\share_link.mp3")
                  mixer.music.play()
                  messagebox.showinfo("ERROR","Something Went Wrong In Sharing ")
                  self.file2.close()
                  self.driver.close()
                  obj.mail(0,self.feedback)
                  return 0
                  
      def teardown(self):
            mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
            mixer.music.play(start=0.45)
            try:
               self.driver.find_element_by_id("userNavigationLabel").click()
               self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Settings'])[3]/following::span[2]").click()
               self.driver.find_element_by_link_text("Log out").click()
               time.sleep(2)
               self.file2.close()
               self.file.close()
               self.driver.close()
               return 1
            except:
                   mixer.music.load(os.getcwd()+"\\sound\\log_out.mp3")
                   mixer.music.play()
                   messagebox.showinfo("ERROR","Something Went Wrong In Log Out In Facebook")
                   mixer.music.load(os.getcwd()+"\\sound\\bgm.mp3")
                   mixer.music.play(start=0.45)
                   self.file2.close()
                   self.file.close()
                   self.driver.close()
                   obj.mail(0,self.feedback)
                   return 0
  
if "___name__"=="__main__":
   obj=test_fb()
   obj.test()
   obj.teardown()


