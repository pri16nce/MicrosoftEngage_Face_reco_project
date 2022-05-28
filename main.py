from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from person import person
import os
import subprocess 
from train import train
from facerecognition import face_recognition
import tkinter



class Face_reco:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        
        
        #1st pic
        img1=Image.open("images/3.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.picimg=ImageTk.PhotoImage(img1)
        
        flabel=Label(self.root,image=self.picimg)
        flabel.place(x=0,y=0,width=500,height=130)
        
        #2ndpic
        img2=Image.open("images/1.jpeg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.picimg1=ImageTk.PhotoImage(img2)
        
        flabel=Label(self.root,image=self.picimg1)
        flabel.place(x=500,y=0,width=500,height=130)
        
        
        #3rd pic
        img3=Image.open("images/4.png")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.picimg2=ImageTk.PhotoImage(img3)
        
        flabel=Label(self.root,image=self.picimg2)
        flabel.place(x=1000,y=0,width=500,height=130)
        
        
        #bgimage
        
        img4=Image.open("images/5.jpg")
        img4=img4.resize((1450,900),Image.ANTIALIAS)
        self.bgimage=ImageTk.PhotoImage(img4)
        
        bglabel=Label(self.root,image=self.bgimage)
        bglabel.place(x=0,y=130,width=1450,height=900)

        title=Label(bglabel,text="FACE RECOGNITION SECURITY SYSTEM",font=("times new roman",55,"bold"),bg="blue",fg="white")
        title.place(x=0,y=0,width=1530,height=60)
        

#button1
        img5=Image.open("images/6.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.buttonimage1=ImageTk.PhotoImage(img5)
        b1=Button(bglabel,image=self.buttonimage1,command=self.person_details,cursor="hand")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bglabel,text="Person details",cursor="hand",command=self.person_details,font=("times new roman",30,"bold"),fg="blue")
        b1_1.place(x=200,y=300,width=220,height=40)

#button2
        img6=Image.open("images/2.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.buttonimage2=ImageTk.PhotoImage(img6)
        b2=Button(bglabel,image=self.buttonimage2,cursor="hand",command=self.face_data)
        b2.place(x=600,y=100,width=220,height=220)
        b2_1=Button(bglabel,text="Face Detector",cursor="hand",command=self.face_data,font=("times new roman",30,"bold"),fg="blue")
        b2_1.place(x=600,y=300,width=220,height=40)

        

#button3
        img7=Image.open("images/7.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.buttonimage3=ImageTk.PhotoImage(img7)
        b3=Button(bglabel,image=self.buttonimage3,cursor="hand",command=self.open_data)
        b3.place(x=1000,y=100,width=220,height=220)
        b3_1=Button(bglabel,text="Data",cursor="hand",command=self.open_data,font=("times new roman",30,"bold"),fg="blue")
        b3_1.place(x=1000,y=300,width=220,height=40)


#button4
        img8=Image.open("images/8.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.buttonimage4=ImageTk.PhotoImage(img8)
        b4=Button(bglabel,image=self.buttonimage4,command=self.train,cursor="hand")
        b4.place(x=200,y=400,width=220,height=220)
        b4_1=Button(bglabel,text="Train Data",command=self.train,cursor="hand",font=("times new roman",30,"bold"),fg="blue")
        b4_1.place(x=200,y=600,width=220,height=40)
        
#button5
        img9=Image.open("images/9.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.buttonimage5=ImageTk.PhotoImage(img9)
        b5=Button(bglabel,image=self.buttonimage5,cursor="hand",command=self.open_image)
        b5.place(x=600,y=400,width=220,height=220)
        b5_1=Button(bglabel,text="Photos",cursor="hand",command=self.open_image, font=("times new roman",30,"bold"),fg="blue")
        b5_1.place(x=600,y=600,width=220,height=40)

 #button6
        img10=Image.open("images/10.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.buttonimage6=ImageTk.PhotoImage(img10)
        b6=Button(bglabel,image=self.buttonimage6,cursor="hand",command=self.exiting)
        b6.place(x=1000,y=400,width=220,height=220)
        b6_1=Button(bglabel,text="Exit",cursor="hand",command=self.exiting,font=("times new roman",30,"bold"),fg="blue")
        b6_1.place(x=1000,y=600,width=220,height=40)    
        
    def open_image(self):
            FileName = "data"
            subprocess.call(['open', FileName])
            
    def open_data(self):
            FileName = "personspotted.csv"
            subprocess.call(['open', FileName])
      #---------exit function-------------\
    def exiting(self):
            self.exiting=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit.",parent=self.root) 
            if self.exiting>0:
              self.root.destroy()
            
            else:
                    return
                           
        
        #---------------------Person details----------------------------
    def person_details(self):
        self.new_window=Toplevel(self.root)
        self.app1=person(self.new_window)
        
        #--------------------train data function call--------
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app2=train(self.new_window)
        
        #--------------------face data function call-----------
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app3=face_recognition(self.new_window)    
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_reco(root)
    root.mainloop()
