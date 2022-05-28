from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")
        
        title=Label(self.root,text="TRAIN DATA SET",font=("times new roman",55,"bold"),bg="blue",fg="white")
        title.place(x=0,y=0,width=1530,height=60)
        
        img4=Image.open("images/5.jpg")
        img4=img4.resize((1530,350),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img4)
        
        Topimage=Label(self.root,image=self.photoimage)
        Topimage.place(x=0,y=65,width=1530,height=350)
        
    #button
    
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train,cursor="hand",font=("times new roman",30,"bold"),fg="blue")
        b1_1.place(x=0,y=400,width=1440,height=40)   
        
        
    #bottom image
        img5=Image.open("images/11.jpg")
        img5=img5.resize((1530,350),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img5)
        
        Topimage=Label(self.root,image=self.photoimage1)
        Topimage.place(x=0,y=450,width=1530,height=350)
     
    def train(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')    #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)   
        
        #---------train classifier and saving
    
        recognizer1 = cv2.face.LBPHFaceRecognizer_create()
        recognizer1.train(faces,ids)
        recognizer1.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets is completed.")
        
        
        
        
        
        
   
if __name__ == "__main__":
    root = Tk()
    obj =train(root)
    root.mainloop()        