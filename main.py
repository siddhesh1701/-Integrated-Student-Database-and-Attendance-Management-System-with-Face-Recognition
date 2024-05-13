from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from help import Help
from developer import Developer
from time import strftime
from datetime import datetime
import os


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        #firstimgae
        img=Image.open(r"G:\facedetection\college_image\main\images1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"G:\facedetection\college_image\main\image3.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #thirdimage
        img2=Image.open(r"G:\facedetection\college_image\main\image2.png")
        img2=img2.resize((650,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #backgroundimage
        
        img3=Image.open(r"G:\facedetection\college_image\main\bg1.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title label
        title_lbl=Label(bg_img,text="INTEGRATED STUDENT DATABASE AND ATTENDANCE MANAGEMENT SYSTEM WITH FACE RECOGNITION",font=("time new roman",16,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #timelive clock
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl= Label(title_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()    
        
        
        #studentbutton1
        img4=Image.open(r"G:\facedetection\college_image\main\b1.png")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        #button1detils
        b11=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b11.place(x=200,y=320,width=220,height=40)
        
        #facedetection
        img5=Image.open(r"G:\facedetection\college_image\main\b2.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)
        
        #button2detils
        b21=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b21.place(x=500,y=320,width=220,height=40)
        
         #attendancebutton
        img6=Image.open(r"G:\facedetection\college_image\main\b3.png")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b3=Button(bg_img,image=self.photoimg6,command=self.attend_data,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
        
        #button3detils
        b31=Button(bg_img,text="Attendance",command=self.attend_data,cursor="hand2",font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b31.place(x=800,y=320,width=220,height=40)
        
        
        #helpbutton
        img7=Image.open(r"G:\facedetection\college_image\main\b4.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help_data)
        b4.place(x=1100,y=100,width=220,height=220)
        
        #button4detils
        b41=Button(bg_img,text="help",cursor="hand2",command=self.Help_data,font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b41.place(x=1100,y=320,width=220,height=40)
        
        #train face button
        img8=Image.open(r"G:\facedetection\college_image\main\b5.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_dataset)
        b5.place(x=200,y=380,width=220,height=220)
        
        #button5detils
        b51=Button(bg_img,text="Train Data",command=self.train_dataset,cursor="hand2",font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b51.place(x=200,y=580,width=220,height=40)
        
        #photo face button
        img9=Image.open(r"G:\facedetection\college_image\main\b6.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)
        
        #button6detils
        b61=Button(bg_img,text="PhotoFace",cursor="hand2",command=self.open_img,font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b61.place(x=500,y=580,width=220,height=40)
        
        #developerbutton
        img10=Image.open(r"G:\facedetection\college_image\main\b7.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)
        
        #button7detils
        b71=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b71.place(x=800,y=580,width=220,height=40)
        
        #exitbutton
        img11=Image.open(r"G:\facedetection\college_image\main\b8.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.I_exit)
        b8.place(x=1100,y=380,width=220,height=220)
        
        #button8detils
        b81=Button(bg_img,text="Exit",cursor="hand2",command=self.I_exit,font=("time new roman",15,"bold"),bg="yellow",fg="black")
        b81.place(x=1100,y=580,width=220,height=40)
        
    def open_img(self):
        os.startfile("data")   
        
      
        
        
        
        #------function buttun----

    def student_details(self):
        
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
    def train_dataset(self):
         
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)    
        
    def face_data(self):
         
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window) 
        
    def attend_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 
    
    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 
             
    def I_exit(self):
        self.I_exit=tkinter.messagebox.askyesno("Face recognition","Are you sure want to exit",parent=self.root)
        if self.I_exit>0:
            self.root.destroy()
        else:
            return       
            
       
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()        