from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("ATTENDANCE SYSTEM")
        
        #variables
        self.var_attend_id=StringVar()
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend_sts=StringVar()
        
        
        
        
        #firstimgae
        img=Image.open(r"G:\facedetection\college_image\attendace11\img1.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)
        
        #second image
        img1=Image.open(r"G:\facedetection\college_image\attendace11\img2.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200)
        
        #backgroundimage
        
        img3=Image.open(r"G:\facedetection\college_image\student\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title label
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=7,y=48,width=1510,height=600)
        
        #leftsideframe
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new romen",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open(r"G:\facedetection\college_image\attendace11\img3.jpg")
        img_left=img_left.resize((780,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=745,height=130)
        
        #frame inside left fram
        attend_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        attend_frame.place(x=5,y=135,width=745,height=420)
        
        #label and entry fill
        
        #attendance id
         #student id
        attendance_Id_label=Label(attend_frame,text="Attendance ID:",font=("times new romen",10,"bold"),bg="white")
        attendance_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_attend_id,font=("times new romen",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)
        
        #roll
        roll_Id_label=Label(attend_frame,text="Roll:",font=("times new romen",10,"bold"),bg="white")
        roll_Id_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_roll_no,font=("times new romen",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=5, sticky=W)
        
        #name
        name_label=Label(attend_frame,text="Name:",font=("times new romen",10,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        name_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_name,font=("times new romen",10,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=5, sticky=W)
        
        #department
        department_Id_label=Label(attend_frame,text="Department:",font=("times new romen",10,"bold"),bg="white")
        department_Id_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        department_Id_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_department,font=("times new romen",10,"bold"))
        department_Id_entry.grid(row=1,column=3,padx=10,pady=5, sticky=W)
        
        #time
        time_label=Label(attend_frame,text="Time:",font=("times new romen",10,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_time,font=("times new romen",10,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5, sticky=W)
        
        #date
        date_label=Label(attend_frame,text="Date:",font=("times new romen",10,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        date_entry=ttk.Entry(attend_frame,width=20,textvariable=self.var_date,font=("times new romen",10,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=5, sticky=W)
        
        #attendnace status
        atten_sts_label=Label(attend_frame,text="Attendance status",textvariable=self.var_attend_sts,font=("times new romen",10,"bold"),bg="white")
        atten_sts_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        sts_combo=ttk.Combobox(attend_frame,font=("times new romen",12,"bold"),width=14,state="readonly")
        sts_combo["values"]=("Select","Present","Absent")
        sts_combo.current(0)
        sts_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #buttonframe
        btn_frame=Frame(attend_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=187,width=738,height=40)
        
        import_csv=Button(btn_frame,text="Import csv",command=self.import_Csv,width=23,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        import_csv.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.export_Csv,width=23,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        export_btn.grid(row=0,column=1)
        
        #Update_btn=Button(btn_frame,text="Update",width=18,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        #Update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=24,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)
    
        
        #rightsideframe
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("times new romen",12,"bold",))
        right_frame.place(x=780,y=10,width=715,height=580)
        
        
        #frame inside right frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=520)
        
        
        #scorll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll no")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("status",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
 #fetch data from buttons
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
            #import data csv
    def import_Csv(self):    
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
    #export csv
    
    def export_Csv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),defaultextension='.csv', parent=self.root)
            
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported"+ os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       
                     
   # to change data in the column                 
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_attend_id.set(rows[0]) 
        self.var_roll_no.set(rows[1])
        self.var_name.set(rows[2]) 
        self.var_department.set(rows[3]) 
        self.var_time.set(rows[4]) 
        self.var_date.set(rows[5]) 
        self.var_attend_sts.set(rows[6]) 
        
    def reset_data(self):
        self.var_attend_id.set("") 
        self.var_roll_no.set("")
        self.var_name.set("") 
        self.var_department.set("") 
        self.var_time.set("") 
        self.var_date.set("") 
        self.var_attend_sts.set("") 
        
        
        
            
              
                
        
        
            
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()                