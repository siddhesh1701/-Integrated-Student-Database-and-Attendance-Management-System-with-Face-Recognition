from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
from student import student
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from help import Help
from developer import Developer
from time import strftime
from datetime import datetime
import os

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        
    #background color
    
        self.root.configure(bg="black")
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"G:\facedetection\college_image\main\login.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lbl_img1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=95,y=100)
        
        #labels
        user_name_lbl=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="black",bg="white")
        user_name_lbl.place(x=110,y=165)
        
        self.user_name=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.user_name.place(x=40,y=200,width=250)
        
        
        passw_lbl=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="black",bg="white")
        passw_lbl.place(x=110,y=250)
        
        self.passw_lbl=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.passw_lbl.place(x=40,y=290,width=250)
        
        #image icon
        
        img2=Image.open(r"G:\facedetection\college_image\main\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lbl_img2.place(x=695,y=339,width=25,height=25)
        
        img3=Image.open(r"G:\facedetection\college_image\main\passw.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lbl_img3.place(x=695,y=428,width=25,height=25)
        
        
        #login button
        login_btn=Button(frame,text="Login",command=self.Login,font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="white",activeforeground="red")
        login_btn.place(x=110,y=340,width=120,height=35)
        
        #register btn
        register_btn=Button(frame,text="Register New User",command=self.registerr_window,font=("times new roman",10,"bold"),borderwidth=0, fg="black",bg="white",activebackground="white",activeforeground="black")
        register_btn.place(x=20,y=395,width=120)
        
        
        #Passwn btn
        passw_btn=Button(frame,text="Forgot Password",command=self.forgot_password,font=("times new roman",10,"bold"),borderwidth=0, fg="black",bg="white",activebackground="white",activeforeground="black")
        passw_btn.place(x=14,y=420,width=120)
     
    def registerr_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Window(self.new_window) 
    
        
        #login system button
    def Login(self):
        if self.user_name.get()=="" or self.passw_lbl.get()=="":
            messagebox.showerror("Error","All Fields Are Required")
        
        elif self.user_name.get()=="siddhesh" and self.passw_lbl.get()=="1234":
            messagebox.showinfo("Success","You are login successfully")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="my_data") 
            my_cursor=conn.cursor()
            query=("SELECT * FROM regi WHERE email = %s AND passw = %s")
            values = (self.user_name.get(), self.passw_lbl.get())
            my_cursor.execute(query, values)
            row= my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Acess only admin") 
                if open_main>0:
                  
                  
                  self.new_window=Toplevel(self.root)
                  self.app=Face_Recognition_System(self.new_window)
                else:
                  if not open_main:
                    return
            conn.commit()
            conn.close()  
  #reset password
    def reset_passwc(self):
      
        
      if self.combo_secq.get()=="Select":
        messagebox.showerror("Error","Select Security Question",parent=self.root2)
      elif self.secq.get()=="":
        messagebox.showerror("Error","Please enter the answer",parent=self.root2)
      elif self.newpassw.get()=="":
        messagebox.showerror("Error","Please enter the new password",parent=self.root2)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="my_data") 
        my_cursor=conn.cursor()
        query1=("select * from regi where email=%s and squestion=%s and sanswer=%s")
        value1=(self.user_name.get(),self.combo_secq.get(),self.secq.get(),)
        my_cursor.execute(query1,value1)
        row=my_cursor.fetchone()
        
        if row==None:
          messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
        else:
          query2=("update regi set passw=%s where email=%s")
          value2=(self.newpassw.get(),self.user_name.get(),)
          my_cursor.execute(query2,value2)
          conn.commit()
          conn.close()
          messagebox.showinfo("Info","your password has been reset,please login using new password",parent=self.root2)
          self.root2.destroy()
                      
            
            
            
            
            
            
            
            
            
            
            
    
    def forgot_password(self):
      if self.user_name.get()=="":
        messagebox.showerror("Error","Please Enter th Email address to reset password")
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="my_data") 
        my_cursor=conn.cursor()
        query=("Select * from regi where email=%s")
        value=(self.user_name.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        #print(row)
        
        if row==None:
          messagebox.showerror("My Error","Please Enter The Valid Username")
        else:
          conn.close()
          self.root2=Toplevel()
         
          self.root2.title("Forgot Password")
          self.root2.geometry("340x450+610+170")
          self.root2.configure(bg="white")
          l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="red")
          l.place(x=0,y=10,relwidth=1)
          
          sec_lbl=Label(self.root2,text=" Select Security Question ",font=("times new roman",15,"bold"),fg="black",bg="white")
          sec_lbl.place(x=50,y=80)
            
          self.combo_secq=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
          self.combo_secq["values"]=("Select","Your Birth Place","Your Pet Name","Your favourite Person")
          self.combo_secq.place(x=50,y=110,width=250) 
          self.combo_secq.current(0)
                    
            #label6
          secq_lbl=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
          secq_lbl.place(x=50,y=150)
            
          self.secq=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
          self.secq.place(x=50,y=180,width=250)  
                
          newpassw_lbl=Label(self.root2,text="New password",font=("times new roman",15,"bold"),fg="black",bg="white")
          newpassw_lbl.place(x=50,y=220)
            
          self.newpassw=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
          self.newpassw.place(x=50,y=250,width=250)  
          
          resetpass_btn=Button(self.root2,text="Reset password",command=self.reset_passwc,font=("times new roman",10,"bold"),bd=3,relief=RIDGE, fg="white",bg="red",activebackground="white",activeforeground="black")
          resetpass_btn.place(x=100,y=300,width=120,height=35)
        
          
                        
                    
                       
            

class Register_Window:
    def __init__(self,root):
      
      self.root=root
      self.root.title("Register")
      self.root.geometry("1550x800+0+0")
        
        #=======variables=====
      self.var_fname=StringVar()
      self.var_lname=StringVar()
      self.var_contact=StringVar()
      self.var_email=StringVar()
      self.var_securityQ=StringVar()
      self.var_securityA=StringVar()
      self.var_passw=StringVar()
      self.var_passwc=StringVar()
        
        
        
        
        
        
        
        
        
        
      self.root.configure(bg="black") #background color
        
        #frame
      frame=Frame(self.root,bg="pink")
      frame.place(x=300,y=100,width=800,height=550)
        
      register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="red",bg="pink")
      register_lbl.place(x=15,y=15)
        
        #label_entry1
      fname_lbl=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="pink")
      fname_lbl.place(x=40,y=105)
         
      self.fname=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
      self.fname.place(x=40,y=140,width=250)
        
          #label_entry2
      lname_lbl=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="pink")
      lname_lbl.place(x=450,y=105)
         
      self.lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
      self.lname.place(x=450,y=140,width=250)
        
        #label_entry3
      cname_lbl=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="pink")
      cname_lbl.place(x=40,y=195)
         
      self.cname=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
      self.cname.place(x=40,y=230,width=250)
        
        #label4
      mail_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="pink")
      mail_lbl.place(x=450,y=195)
         
      self.mail=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
      self.mail.place(x=450,y=230,width=250)
        
        #laabel5
      sec_lbl=Label(frame,text=" Select Security Question ",font=("times new roman",15,"bold"),fg="black",bg="pink")
      sec_lbl.place(x=35,y=285)
        
      self.combo_secq=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
      self.combo_secq["values"]=("Select","Your Birth Place","Your Pet Name","Your favourite Person")
      self.combo_secq.place(x=40,y=320,width=250) 
      self.combo_secq.current(0)
                
        #label6
      secq_lbl=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="pink")
      secq_lbl.place(x=450,y=285)
         
      self.secq=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
      self.secq.place(x=450,y=320,width=250)
        
         #label_entry7
      passwrd_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="pink")
      passwrd_lbl.place(x=38,y=365)
         
      self.passwrd=ttk.Entry(frame,textvariable=self.var_passw,font=("times new roman",15,"bold"))
      self.passwrd.place(x=40,y=400,width=250)
        
        #label8
      cpass_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="pink")
      cpass_lbl.place(x=450,y=365)
         
      self.cpass=ttk.Entry(frame,textvariable=self.var_passwc,font=("times new roman",15,"bold"))
      self.cpass.place(x=450,y=400,width=250)
        
        #check btn
      self.var_check=IntVar()
      self.check_btn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",15,"bold"),bg="pink",onvalue=1,offvalue=0)
      self.check_btn.place(x=40,y=450)
        
        #register btn
        
      register1_btn=Button(frame,text="Register",command=self.register_data,font=("times new roman",15,"bold"),borderwidth=0, fg="black",bg="red",activebackground="pink",activeforeground="red")
      register1_btn.place(x=450,y=450,width=120,height=35)
        
      login_btn=Button(frame,text="Login Now",command=self.return_login,font=("times new roman",15,"bold"),borderwidth=0, fg="black",bg="blue",activebackground="pink",activeforeground="red")
      login_btn.place(x=600,y=450,width=120,height=35)
  
  #======function declaration======
    def register_data(self):
      if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_passw.get()=="" or self.var_securityQ.get()=="Select" or self.var_passwc.get()=="" or self.var_securityA.get()=="":
        messagebox.showerror("Error","All Fields are Required")
      elif self.var_passw.get()!=self.var_passwc.get():
        messagebox.showerror("Error","Password & Confirm Password must be same")
      elif self.var_check.get()==0:
        messagebox.showerror("Error","Please select the checkbox")
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="my_data") 
        my_cursor=conn.cursor()
        query=("select * from regi where email=%s")
        value=(self.var_email.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
      
        if row!=None:
          messagebox.showerror("Error","User already exist,please try another mail")
        else:
          my_cursor.execute("insert into regi values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                      self.var_fname.get(),
                                                                                      self.var_lname.get(),
                                                                                      self.var_contact.get(),
                                                                                      self.var_email.get(),
                                                                                      self.var_securityQ.get(),
                                                                                      self.var_securityA.get(),
                                                                                      self.var_passw.get(),
                                                                                      self.var_passwc.get(),
                                                                                      
                ))
                                                                                                                
                                                                                                               
        conn.commit()       
        conn.close()
        messagebox.showinfo("Success","Register Successfull",parent=self.root)               
    def return_login(self):
      self.root.destroy()

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
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
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
            
            

if __name__=="__main__":
    main()
    