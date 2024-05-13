from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("DEVELOPER INFORMATION")
        
        #title label
        title_lbl=Label(self.root,text="DEVELOPER INFORMATION",font=("time new roman",35,"bold"),bg="Yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #backgroundimage
        
        img=Image.open(r"G:\facedetection\college_image\attendace11\img4.jpg")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=45,width=1530,height=750)
        
        #frame
        main_frame=Frame(f_lbl,bg="white",bd=2)
        main_frame.place(x=1100,y=50,width=400,height=180)
    
        
        img_left=Image.open(r"G:\facedetection\college_image\student\img5.jpg")
        img_left=img_left.resize((200,150),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f1_lbl=Label(main_frame,image=self.photoimg_left)
        f1_lbl.place(x=190,y=10,width=200,height=150)
        
        

        name_label=Label(main_frame,text="SIDDHESH SALUNKHE",font=("times new bold",10,"bold"))
        name_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
       
        paragraph_label =Label(main_frame,text="Python developer \n AI ML \n Cloud computing ",font=("times new romen",10,"bold"))
        paragraph_label.grid(row=300,column=0,padx=10,pady=5,sticky=W)
        
        link_btn = Button(main_frame, text="LinkedIn", command=self.open_link, width=15, font=("times new romen", 12, "bold"), bg="yellow", fg="black")
        link_btn.grid(row=350, column=0)

        
        

    def open_link(self):
        webbrowser.open("https://www.linkedin.com/in/siddhesh-salunkhe-141368191/")
    
     
   


  
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()          
        