from email import message
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class person:
    def __init__(self, sql6495470):
        self.sql6495470 = sql6495470
        self.sql6495470.geometry("1530x900+0+0")
        self.sql6495470.title("Face Recognition System")
        
        
        #-------------------All of the Variables-----------------------
        self.var_person=StringVar()
        self.var_state=StringVar()
        self.var_age=StringVar()
        self.var_arrest=StringVar()
        self.var_personid=StringVar()
        self.var_personname=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_case=StringVar()
        self.var_jail=StringVar()
        
        

        title=Label(text="PERSON DETAILS",font=("times new roman",55,"bold"),bg="red",fg="blue")
        title.place(x=0,y=0,width=1530,height=100)

        frame=Frame(bd=2,bg="white")
        frame.place(x=0,y=100,width=1500,height=600)

        leftframe=LabelFrame(frame,bd=2,relief=RAISED,text="Person Details",font=("times new roman",12,"bold"))
        leftframe.place(x=10,y=10,width=660,height=570)




        currentframe=LabelFrame(leftframe,bd=2,relief=RAISED,text="Current Information",font=("times new roman",12,"bold"))
        currentframe.place(x=5,y=10,width=640,height=120)

#Person Type
        label1=Label(currentframe,text="Person Type",font=("times new roman",14,"bold"),bg="white")
        label1.grid(row=0,column=0,padx=10)

        per_combo=ttk.Combobox(currentframe,textvariable=self.var_person,font=("times new roman",12,"bold"),state="read only")
        per_combo["values"]=("Select Person type","Lost Person","Terrorist","Criminal","International Criminal","Wanted","Other")
        per_combo.current(0)
        per_combo.grid(row=0,column=1,padx=2,pady=10)

#State
        label2=Label(currentframe,text="State",font=("times new roman",14,"bold"),bg="white")
        label2.grid(row=0,column=2,padx=10)

        state_combo=ttk.Combobox(currentframe,textvariable=self.var_state,font=("times new roman",12,"bold"),state="read only")
        state_combo["values"]=("Select State or UT","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","National Capital Territory of Delhi","Lakshadweep","Pondicherry")
        state_combo.current(0)
        state_combo.grid(row=0,column=3,padx=2,pady=10)

#age
        label3=Label(currentframe,text="Age",font=("times new roman",14,"bold"),bg="white")
        label3.grid(row=1,column=0,padx=10)

        combo=ttk.Combobox(currentframe,textvariable=self.var_age,font=("times new roman",12,"bold"),state="read only")
        combo["values"]=("Select Age","0-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100","100+")
        combo.current(0)
        combo.grid(row=1,column=1,padx=2,pady=10)

#Arrest
        label4=Label(currentframe,text="Whether Arrest or not",font=("times new roman",14,"bold"),bg="white")
        label4.grid(row=1,column=2,padx=10)

        combo=ttk.Combobox(currentframe,textvariable=self.var_arrest,font=("times new roman",12,"bold"),state="read only")
        combo["values"]=("Select","Yes","No","Not Applicable")
        combo.current(0)
        combo.grid(row=1,column=3,padx=2,pady=10)


        currentinfo=LabelFrame(leftframe,bd=2,relief=RAISED,text="Information",font=("times new roman",14,"bold"))
        currentinfo.place(x=5,y=160,width=640,height=350 )

#personid
        label5=Label(currentinfo,text="Serial No.",font=("times new roman",14,"bold"),bg="white")
        label5.grid(row=0,column=0,padx=10,pady=5)

        personid_entry=ttk.Entry(currentinfo,textvariable=self.var_personid,width=20,font=("times new roman",14,"bold"))
        personid_entry.grid(row=0,column=1,padx=10,pady=5)

#person name
        label5=Label(currentinfo,text="Person Name",font=("times new roman",14,"bold"),bg="white")
        label5.grid(row=0,column=2,padx=10,pady=5)

        label5_entry=ttk.Entry(currentinfo,textvariable=self.var_personname,width=20,font=("times new roman",14,"bold"))
        label5_entry.grid(row=0,column=3,padx=10,pady=5)

#gender
        label6=Label(currentinfo,text="Gender",font=("times new roman",14,"bold"),bg="white")
        label6.grid(row=1,column=0,padx=10,pady=5)

        label6_entry=ttk.Entry(currentinfo,textvariable=self.var_gender,width=20,font=("times new roman",14,"bold"))
        label6_entry.grid(row=1,column=1,padx=10,pady=5)

#DOB
        label7=Label(currentinfo,text="DOB",font=("times new roman",14,"bold"),bg="white")
        label7.grid(row=1,column=2,padx=10,pady=5)

        label7_entry=ttk.Entry(currentinfo,textvariable=self.var_dob,width=20,font=("times new roman",14,"bold"))
        label7_entry.grid(row=1,column=3,padx=10,pady=5)

#phone
        label8=Label(currentinfo,text="Phone Number",font=("times new roman",14,"bold"),bg="white")
        label8.grid(row=2,column=0,padx=10,pady=5)

        label8_entry=ttk.Entry(currentinfo,textvariable=self.var_phone,width=20,font=("times new roman",14,"bold"))
        label8_entry.grid(row=2,column=1,padx=10,pady=5)

#Address
        label9=Label(currentinfo,text="Address",font=("times new roman",14,"bold"),bg="white")
        label9.grid(row=2,column=2,padx=10,pady=5)

        label9_entry=ttk.Entry(currentinfo,textvariable=self.var_address,width=20,font=("times new roman",14,"bold"))
        label9_entry.grid(row=2,column=3,padx=10,pady=5)

#Cases
        label10=Label(currentinfo,text="Cases",font=("times new roman",14,"bold"),bg="white")
        label10.grid(row=3,column=0,padx=10,pady=5)

        label10_entry=ttk.Entry(currentinfo,textvariable=self.var_case,width=20,font=("times new roman",14,"bold"))
        label10_entry.grid(row=3,column=1,padx=10,pady=5)

#jail
        label11=Label(currentinfo,text="JailHistory",font=("times new roman",14,"bold"),bg="white")
        label11.grid(row=3,column=2,padx=10,pady=5)

        label11_entry=ttk.Entry(currentinfo,textvariable=self.var_jail,width=20,font=("times new roman",14,"bold"))
        label11_entry.grid(row=3,column=3,padx=10,pady=5)

#radio buttons 
        
        self.var_rad1=StringVar()
        rad_button1=ttk.Radiobutton(currentinfo,variable=self.var_rad1,text="Take Photo Sample",value="Yes")
        rad_button1.grid(row=6,column=0)
        
       
        rad_button2=ttk.Radiobutton(currentinfo,variable=self.var_rad1,text="No Photo Sample",value="No")
        rad_button2.grid(row=6,column=1)
        

#btn frame
        button_frame=Frame(currentinfo,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=210,width=620,height=40)

        savebutton=Button(button_frame,text="Save",command=self.adding_data,width=17,font=("times new roman",14,"bold"),bg="blue",fg="black")
        savebutton.grid(row=0,column=0)

        updatebutton=Button(button_frame,text="Update",command=self.update_data,width=17,font=("times new roman",14,"bold"),bg="blue",fg="black")
        updatebutton.grid(row=0,column=1)

        resetbutton=Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",14,"bold"),bg="blue",fg="black")
        resetbutton.grid(row=0,column=2)

        deletebutton=Button(button_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",14,"bold"),bg="blue",fg="black")
        deletebutton.grid(row=0,column=3)

        button_frame1=Frame(currentinfo,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0,y=270,width=620,height=35)

        takephotobutton=Button(button_frame1,command=self.gen_data,text="Take Photo Sample",width=39,font=("times new roman",14,"bold"),bg="blue",fg="black")
        takephotobutton.grid(row=0,column=0)

        updatephotobutton=Button(button_frame1,text="Update Photo Sample",width=39,font=("times new roman",14,"bold"),bg="blue",fg="black")
        updatephotobutton.grid(row=0,column=1)

        rightframe=LabelFrame(frame,bd=2,relief=RAISED,text="Person Details",font=("times new roman",12,"bold"))
        rightframe.place(x=720,y=10,width=660,height=570)

#--------Searching System------------
        search_frame=LabelFrame(rightframe,bd=2,relief=RAISED,text="Search Information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=10,width=640,height=70)

        label12=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="blue",fg="white")
        label12.grid(row=0,column=0,padx=10,pady=5)
#search
        self.var_comb_search=StringVar()
        searchcombo=ttk.Combobox(search_frame,textvariable=self.var_comb_search,font=("times new roman",12,"bold"),state="read only",width=15)
        searchcombo["values"]=("Select","PersonName","PersonID")
        searchcombo.current(0)
        searchcombo.grid(row=0,column=1,padx=2,pady=10)

        self.var_search=StringVar()
        search1_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",14,"bold"))
        search1_entry.grid(row=0,column=2,padx=10,pady=5)

        search_button=Button(search_frame,command=self.searchdata,text="Search",width=12,font=("times new roman",14,"bold"),bg="blue",fg="black")
        search_button.grid(row=0,column=3,padx=4)

        showall_button=Button(search_frame,command=self.fetchdata,text="Show All",width=12,font=("times new roman",14,"bold"),bg="blue",fg="black")
        showall_button.grid(row=0,column=4,padx=4)

#--------Frame of database-----------

        table=Label(rightframe,bd=2,relief=RIDGE,bg="white")
        table.place(x=5,y=100,width=650,height=450)

        scroll_x=ttk.Scrollbar(table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table,orient=VERTICAL)
        self.table_person=ttk.Treeview(table,column=("PersonType","State","Age","Arrest","PersonID","PersonName","DOB","PhoneNo","Address","Gender","Cases","JailHistory","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table_person.xview)
        scroll_y.config(command=self.table_person.yview)
        
        self.table_person.heading("PersonType",text="PersonType")
        self.table_person.heading("State",text="State")
        self.table_person.heading("Age",text="Age")
        self.table_person.heading("Arrest",text="Arrest")
        self.table_person.heading("PersonID",text="PersonID")
        self.table_person.heading("PersonName",text="PersonName")
        self.table_person.heading("DOB",text="DOB")
        self.table_person.heading("PhoneNo",text="PhoneNo")
        self.table_person.heading("Address",text="Address")
        self.table_person.heading("Gender",text="Gender")
        self.table_person.heading("Cases",text="Cases")
        self.table_person.heading("JailHistory",text="JailHistory")
        self.table_person.heading("Photo",text="Photo")
        self.table_person["show"]="headings"
        
        self.table_person.column("PersonType",width=100)
        self.table_person.column("State",width=100)
        self.table_person.column("Age",width=100)
        self.table_person.column("Arrest",width=100)
        self.table_person.column("PersonID",width=100)
        self.table_person.column("PersonName",width=100)
        self.table_person.column("DOB",width=100)
        self.table_person.column("PhoneNo",width=100)
        self.table_person.column("Address",width=100)
        self.table_person.column("Gender",width=100)
        self.table_person.column("Cases",width=100)
        self.table_person.column("JailHistory",width=100)
        self.table_person.column("Photo",width=150)
        
        
        
        self.table_person.pack(fill=BOTH,expand=1)
        self.table_person.bind("<ButtonRelease>",self.get_cursor)
        self.fetchdata()
        
        #-----------------------declaration of function------------------
    def adding_data(self):
        if self.var_person.get()=="Select Person type" or self.var_personname.get()=="" or self.var_personid.get()=="":
            messagebox.showerror("Error","All field are required")
        else:  
                   try:  
                        conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
                        mycursor=conn.cursor()
                        mycursor.execute("insert into Person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                     
                                                                                                 self.var_person.get(),
                                                                                                 self.var_state.get(),
                                                                                                 self.var_age.get(),
                                                                                                 self.var_arrest.get(),
                                                                                                 self.var_personid.get(),
                                                                                                 self.var_personname.get(),
                                                                                                 self.var_dob.get(),
                                                                                                 self.var_phone.get(),
                                                                                                 self.var_address.get(),
                                                                                                 self.var_gender.get(),
                                                                                                 self.var_case.get(),
                                                                                                 self.var_jail.get(),
                                                                                                 self.var_rad1.get()               
                                                                                              ))
                        conn.commit()
                        self.fetchdata()
                        conn.close()
                        messagebox.showinfo("Success","Person Details has added successfully in the database.",parent=self.sql6495470)
                                
                   except Exception as es:
                        messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.sql6495470)
        
  #---------------data fetch-----------------
  
    def fetchdata(self):
         conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
         mycursor=conn.cursor()
         mycursor.execute("select * from Person")
         data=mycursor.fetchall()
         
         if len(data)!=0:
             self.table_person.delete(*self.table_person.get_children())
             for i in data:
                     self.table_person.insert("",END,values=i)
             conn.commit()
             conn.close()
             
  #------------------get cursor----------------           
    def get_cursor(self,event=""):
            cursor_focus=self.table_person.focus()
            content=self.table_person.item(cursor_focus)
            data=content["values"]
            
            self.var_person.set(data[0]),
            self.var_state.set(data[1]),  
            self.var_age.set(data[2]),  
            self.var_arrest.set(data[3]),  
            self.var_personid.set(data[4]),  
            self.var_personname.set(data[5]),  
            self.var_dob.set(data[6]),  
            self.var_phone.set(data[7]),  
            self.var_address.set(data[8]),  
            self.var_gender.set(data[9]),        
            self.var_case.set(data[10]),  
            self.var_jail.set(data[11]),  
            self.var_rad1.set(data[12])  
            
#-----------------update function-------------------
    def update_data(self):
             if self.var_person.get()=="Select Person type" or self.var_personname.get()=="" or self.var_personid.get()=="":
                messagebox.showerror("Error","All field are required",parent=self.sql6495470)
             else:
                   try:
                            Update=messagebox.askyesno("Update","Do you want to update this person details.",parent=self.sql6495470)
                            if Update>0:
                                    conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
                                    mycursor=conn.cursor()
                                    mycursor.execute("update Person set PersonType=%s,State=%s,Age=%s,Arrest=%s,PersonName=%s,DOB=%s,PhoneNo=%s,Address=%s,Gender=%s,Cases=%s,JailHistory=%s,Photo=%s where PersonID=%s",(
                                     self.var_person.get(),
                                     self.var_state.get(),
                                     self.var_age.get(),
                                     self.var_arrest.get(),
                                     self.var_personname.get(),
                                     self.var_dob.get(),
                                     self.var_phone.get(),
                                     self.var_address.get(),
                                     self.var_gender.get(),
                                     self.var_case.get(),
                                     self.var_jail.get(),
                                     self.var_rad1.get(),
                                     self.var_personid.get()   
                                                   ))                       
                            else:
                                    if not Update:
                                            return
                            messagebox.showinfo("Success","Person details are updated successfully.") 
                            conn.commit()
                            self.fetchdata()
                            conn.close()    
                   except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.sql6495470)
                                               
#-----------------------Delete function--------------------------
    def delete_data(self):
            if self.var_personid.get=="":
                    messagebox.showerror("Error","Person ID is required.",parent=self.sql6495470)
            else:
                    try:
                            delete=messagebox.askyesno("Person details delete page","Do you want to delete this person data",parent=self.sql6495470)
                            if delete>0:
                                    conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
                                    mycursor=conn.cursor()
                                    sql="delete from Person where PersonID=%s"
                                    val=(self.var_personid.get(),)
                                    mycursor.execute(sql,val)
                            else:
                                    if not delete:
                                            return
                                    
                            conn.commit()
                            self.fetchdata()
                            conn.close()
                            messagebox.showinfo("Deleted","Successfully person details are deleted.",parent=self.sql6495470)
                    except Exception as es:
                           messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.sql6495470) 
                           
                           
 #-----------------------------Reset function------------------------
                           
    def reset_data(self):
            self.var_person.set("Select Person Type")
            self.var_state.set("Select State or UT")
            self.var_age.set("Select Age")
            self.var_arrest.set("Select")
            self.var_personid.set("")
            self.var_personname.set("")
            self.var_gender.set("")
            self.var_dob.set("")
            self.var_phone.set("")
            self.var_address.set("")
            self.var_case.set("")
            self.var_jail.set("")
            self.var_rad1.set("")
            
                           
#----------------------taking photo / generating dataset-------------------
                           
    def gen_data(self):
            if self.var_person.get()=="Select Person type" or self.var_personname.get()=="" or self.var_personid.get()=="":
                     messagebox.showerror("Error","All field are required")
            else:   
                 
                    try:
                            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
                            mycursor=conn.cursor()
                            mycursor.execute("select * from Person")
                            myresult=mycursor.fetchall()
                            id=0
                            for x in myresult:
                                    id+=1
                            mycursor.execute("update Person set PersonType=%s,State=%s,Age=%s,Arrest=%s,PersonName=%s,DOB=%s,PhoneNo=%s,Address=%s,Gender=%s,Cases=%s,JailHistory=%s,Photo=%s where PersonID=%s",(
                             self.var_person.get(),
                             self.var_state.get(),
                             self.var_age.get(),
                             self.var_arrest.get(),
                             self.var_personname.get(),
                             self.var_dob.get(),
                             self.var_phone.get(),
                             self.var_address.get(),
                             self.var_gender.get(),
                             self.var_case.get(),
                             self.var_jail.get(),
                             self.var_rad1.get(),
                             self.var_personid.get()==id+1    
                            ))                       
                            conn.commit()
                            self.fetchdata()
                            self.reset_data()
                            conn.close()
         #-----------------Loading frontal face xml file from opencv----------------------------
                            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                            
                            def face_crop(img):
                                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                                    #scaling factor=1.3
                                    #minimum neighbour=5
                                    
                                    for (x,y,w,h) in faces:
                                            face_crop=img[y:y+h,x:x+w]
                                            return face_crop
                                    
                            cap=cv2.VideoCapture(0)
                            image_id=0
                            while True:
                                    ret,myframe=cap.read()
                                    if face_crop(myframe) is not None:
                                            image_id+=1
                                            face=cv2.resize(face_crop(myframe),(450,450))
                                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                                            file_name_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                                            cv2.imwrite(file_name_path,face)    
                                            cv2.putText(face,str(image_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                                            cv2.imshow("Cropped face",face)  
                                    
                                    if cv2.waitKey(1)==13 or int(image_id)==100:
                                            break
                            cap.release()
                            cv2.destroyAllWindows()
                            messagebox.showinfo("Result","Generating data sets completed!!")
                            
                    except Exception as es:
                           messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.sql6495470)                 
                                    
     #---------------------------------search data---------------------------------
    def searchdata(self):
            if self.var_comb_search.get()=="" or self.var_search.get()=="":
                    messagebox.showerror("Error","Please select an option!!")
            else:
                    try:
                            conn=mysql.connector.connect(host="sql6.freemysqlhosting.net",username="sql6495470",password="97AwqtmU3p",database="sql6495470")
                            mycursor=conn.cursor()
                            mycursor.execute("select * from Person where " +str(self.var_comb_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                            data=mycursor.fetchall()
                            if len(data)!=0:
                                    self.table_person.delete(*self.table_person.get_children())
                                    for i in data:
                                            self.table_person.insert("",END,values=i)
                                    conn.commit()
                            conn.close()        
                    except Exception as es:
                           messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.sql6495470)                
                            
                            
 
 
 
 
if __name__ == "__main__":
    sql6495470 = Tk()
    obj =person(sql6495470)
    sql6495470.mainloop()
