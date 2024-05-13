from tkinter import*
from tkinter import ttk

from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("HELP")
        
        #title label
        title_lbl=Label(self.root,text="HELP INFORMATION",font=("time new roman",35,"bold"),bg="Yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #backgroundimage
        
        img=Image.open(r"G:\facedetection\college_image\attendace11\img6.png")
        img=img.resize((1530,710),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=45,width=1530,height=750)
        
        #title label
        title_lbl=Label(self.root,text="Email:siddsalunkhe1701@gmail.com",font=("time new roman",45,"bold"),bg="white",fg="black")
        title_lbl.place(x=150,y=150,width=1300,height=45)
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()          
                