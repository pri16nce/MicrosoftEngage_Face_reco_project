import imghdr
from re import M
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import waitKey
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime




class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
  
        title=Label(self.root,text="FACE RECOGNITION",font=("times new roman",55,"bold"),bg="blue",fg="white")
        title.place(x=0,y=0,width=1530,height=60) 
  
  
  #1st image data
        img4=Image.open("images/12.jpg")
        img4=img4.resize((650,700),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img4)
        
        Topimage=Label(self.root,image=self.photoimage)
        Topimage.place(x=0,y=65,width=650,height=700)
        
   #2nd image data
        img5=Image.open("images/13.jpg")
        img5=img5.resize((950,700),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img5)
        
        Topimage1=Label(self.root,image=self.photoimage1)
        Topimage1.place(x=650,y=65,width=950,height=700)
        
     #button
    
        b1_1=Button(Topimage1,text="FACE  RECOGNITION",cursor="hand",command=self.face_recog,font=("times new roman",18,"bold"),fg="blue")
        b1_1.place(x=350,y=600,width=220,height=40)   
        
        
#------------saving data if person found in the excel----------------     
    def mark_found(self,i,j,k,l):
        with open("personspotted.csv","r+",newline="\n")as f:
            mydatalist=f.readlines()
            namelist=[]
            for line in mydatalist:
                entry=line.split((","))
                namelist.append(entry[0])
            if((i not in namelist) and (j not in namelist) and (k not in namelist) and (l not in namelist)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{j},{k},{l},{dtString},{d1},Preset")
                
        
        
        
        
        
        
        
        
#----------------face-recognition-------------------------
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,txt,recognizer1):
          gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
          
          coord=[]
          
          for (x,y,w,h) in features:
              cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
              id,predict=recognizer1.predict(gray_image[y:y+h,x:x+w])
              confidence=int((100*(1-predict/300)))
              
              conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
              mycursor=conn.cursor()
              
              mycursor.execute("select PersonName from Person where PersonID="+str(id))
              i=mycursor.fetchone()
              i="+".join(i)
              
              mycursor.execute("select PersonType from Person where PersonID="+str(id))
              j=mycursor.fetchone()
              j="+".join(j)
              
              mycursor.execute("select State from Person where PersonID="+str(id))
              k=mycursor.fetchone()
              k="+".join(k)
              
              mycursor.execute("select Arrest from Person where PersonID="+str(id))
              l=mycursor.fetchone()
              l="+".join(l)
              
              
              
              
              if confidence>77:
                  cv2.putText(img,f"PersonName:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"PersonType:{j}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"State:{k}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  cv2.putText(img,f"Arrest:{l}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                  self.mark_found(i,j,k,l)
              else:
                  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                  cv2.putText(img,"Unknown",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   
        
        
              coord=[x,y,w,h]
        
        def recogn(img,recognizer1,faceCascade):
         coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",recognizer1)
         return img
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer1=cv2.face.LBPHFaceRecognizer_create()
        recognizer1.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recogn(img,recognizer1,faceCascade)
            cv2.imshow("Welcome to Face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        
        
if __name__ == "__main__":
    root = Tk()
    obj =face_recognition(root)
    root.mainloop()   