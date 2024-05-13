from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        
      login_btn=Button(frame,text="Login Now",font=("times new roman",15,"bold"),borderwidth=0, fg="black",bg="blue",activebackground="pink",activeforeground="red")
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
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    app=Register_Window(root)
    root.mainloop()        