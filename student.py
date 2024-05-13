from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        
        #======variables==
        self.var_Dep=StringVar()
        self.var_Course=StringVar()
        self.var_Year=StringVar()
        self.var_Sem=StringVar()
        self.var_id=StringVar()
        self.var_Name=StringVar()
        self.var_Div=StringVar()
        self.var_Roll=StringVar()
        self.var_Email=StringVar()
        self.var_Mobileno=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_Address=StringVar()
        self.var_Facultyname=StringVar()
        
        
        
        
        #firstimgae
        img=Image.open(r"G:\facedetection\college_image\student\images1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img1=Image.open(r"G:\facedetection\college_image\student\image3.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #thirdimage
        img2=Image.open(r"G:\facedetection\college_image\student\image2.png")
        img2=img2.resize((650,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        #backgroundimage
        
        img3=Image.open(r"G:\facedetection\college_image\student\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        #title label
        title_lbl=Label(bg_img,text="STUDENT DETAILS MANAGEMENT",font=("time new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=7,y=55,width=1510,height=600)
        
        #leftsideframe
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)
        
        img_left=Image.open(r"G:\facedetection\college_image\student\img1.jpg")
        img_left=img_left.resize((780,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=745,height=130)
        
        Currentcou_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new romen",12,"bold"))
        Currentcou_frame.place(x=5,y=135,width=745,height=120)
        
        #departmentlabel
        dep_label=Label(Currentcou_frame,text="Department",font=("times new romen",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(Currentcou_frame,textvariable=self.var_Dep,font=("times new romen",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Engineering","Computer Engineering AI","Electronics and Communication Engineering","Mechanical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #course
        course_label=Label(Currentcou_frame,text="Course",font=("times new romen",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Currentcou_frame,textvariable=self.var_Course,font=("times new romen",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BTECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        year_label=Label(Currentcou_frame,text="Admission Year",font=("times new romen",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(Currentcou_frame,textvariable=self.var_Year,font=("times new romen",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #semester
        sem_label=Label(Currentcou_frame,text="Semester",font=("times new romen",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(Currentcou_frame,textvariable=self.var_Sem,font=("times new romen",12,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","Semester 1","Semester 2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #student information
        
        Studentinfo_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new romen",12,"bold"))
        Studentinfo_frame.place(x=5,y=260,width=745,height=290)
        
        #student id
        student_Id_label=Label(Studentinfo_frame,text="Student ID:",font=("times new romen",10,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentId_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_id,width=20,font=("times new romen",10,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5, sticky=W)
    
        #student name
        student_name_label=Label(Studentinfo_frame,text="Student Name:",font=("times new romen",10,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Name,width=20,font=("times new romen",10,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class divsion
        student_div_label=Label(Studentinfo_frame,text="Division:",font=("times new romen",10,"bold"),bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(Studentinfo_frame,textvariable=self.var_Div,font=("times new romen",12,"bold"),width=14,state="readonly")
        div_combo["values"]=("Select","A","B","C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
         #rollno
        student_roll_label=Label(Studentinfo_frame,text="Roll no:",font=("times new romen",10,"bold"),bg="white")
        student_roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        studentroll_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Roll,width=20,font=("times new romen",10,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
         #email
        student_email_label=Label(Studentinfo_frame,text="Email:",font=("times new romen",10,"bold"),bg="white")
        student_email_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        studentemail_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Email,width=20,font=("times new romen",10,"bold"))
        studentemail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
         #mobileno
        student_mobile_label=Label(Studentinfo_frame,text="Mobile no:",font=("times new romen",10,"bold"),bg="white")
        student_mobile_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        studentmob_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Mobileno,width=20,font=("times new romen",10,"bold"))
        studentmob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
         #dob
        student_dob_label=Label(Studentinfo_frame,text="Date of birth:",font=("times new romen",10,"bold"),bg="white")
        student_dob_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        studentdob_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_dob,width=20,font=("times new romen",10,"bold"))
        studentdob_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        student_gender_label=Label(Studentinfo_frame,text="Gender:",font=("times new romen",10,"bold"),bg="white")
        student_gender_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
         
        gen_combo=ttk.Combobox(Studentinfo_frame,textvariable=self.var_gen,font=("times new romen",12,"bold"),width=14,state="readonly")
        gen_combo["values"]=("Select","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #address
        student_add_label=Label(Studentinfo_frame,text="Address:",font=("times new romen",10,"bold"),bg="white")
        student_add_label.grid(row=5,column=0,padx=10,pady=5,sticky=W)
        
        studentadd_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Address,width=20,font=("times new romen",10,"bold"))
        studentadd_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)
        
         #faculty
        student_teacher_label=Label(Studentinfo_frame,text="FacultyName:",font=("times new romen",10,"bold"),bg="white")
        student_teacher_label.grid(row=5,column=2,padx=10,pady=5,sticky=W)
        
        studentteach_entry=ttk.Entry(Studentinfo_frame,textvariable=self.var_Facultyname,width=20,font=("times new romen",10,"bold"))
        studentteach_entry.grid(row=5,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #radiobutton
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(Studentinfo_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        Radiobutton1.grid(row=7,column=0)
        
        Radiobutton2=ttk.Radiobutton(Studentinfo_frame,variable=self.var_radio1,text="No photo sample",value="No")
        Radiobutton2.grid(row=7,column=1)
        
        #buttonframe
        btn_frame=Frame(Studentinfo_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=187,width=738,height=40)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="update",command=self.update_data,width=18,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=16,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)
        
        btn1_frame=Frame(Studentinfo_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=2,y=225,width=738,height=40)
    
        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        take_photo_btn.grid(row=1,column=0)
        
        update_photo_btn=Button(btn1_frame,text="Update Photo sample",width=36,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        update_photo_btn.grid(row=1,column=1)
        
    
        
        
         #rightsideframe
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new romen",12,"bold",))
        right_frame.place(x=780,y=10,width=715,height=580)
        
        img_right=Image.open(r"G:\facedetection\college_image\student\rgb1.jpg")
        img_right=img_right.resize((780,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=700,height=130)
        
        #search system
        Searchsystem_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new romen",12,"bold"))
        Searchsystem_frame.place(x=5,y=135,width=700,height=70)
        
        search_label=Label(Searchsystem_frame,text="Search By",font=("times new romen",15,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Searchsystem_frame,textvariable=self.var_com_search,font=("times new romen",15,"bold"),width=9,state="readonly")
        search_combo["values"]=("Select","Name","Mobile No","id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search1=StringVar()
        search_entry=ttk.Entry(Searchsystem_frame,textvariable=self.var_search1,width=15,font=("times new romen",15,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Searchsystem_frame,command=self.search_data,text="Search",width=11,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        search_btn.grid(row=0,column=3,padx=4)
        
        showall_btn=Button(Searchsystem_frame,command=self.fetch_data,text="Show All",width=11,font=("times new romen",12,"bold"),bg="yellow",fg="black")
        showall_btn.grid(row=0,column=4,padx=4)
        
        #-----------------tableframe------------
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=700,height=330)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("Dep","Course","Year","Sem","id","Name","Division","Roll","Email","Mobileno","gen","dob","Address","Facultyname","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Admission Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll no")
        self.student_table.heading("Email",text="Email id")
        self.student_table.heading("Mobileno",text="Mobile no")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="Date of birth")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Facultyname",text="Faculty Name")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=120)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Mobileno",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Facultyname",width=100)
        self.student_table.column("photo",width=150)
     
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #--------function decalaration to add data----
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_Dep.get(),
                                                                                                                self.var_Course.get(),
                                                                                                                self.var_Year.get(),
                                                                                                                self.var_Sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_Name.get(),
                                                                                                                self.var_Div.get(),
                                                                                                                self.var_Roll.get(),
                                                                                                                self.var_Email.get(),
                                                                                                                self.var_Mobileno.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_Address.get(),
                                                                                                                self.var_Facultyname.get(),
                                                                                                                self.var_radio1.get()
                                                                                                         ))   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been successfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
           
    #----fetch data from mysql to system----
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()        
        
    #get cursor 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_Dep.set(data [0]),
        self.var_Course.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Div.set(data[6]),
        self.var_Roll.set(data[7]),
        self.var_Email.set(data[8]),
        self.var_Mobileno.set(data[9]),
        self.var_gen.set(data[10]),
        self.var_dob.set(data[11]),
        self.var_Address.set(data[12]),
        self.var_Facultyname.set(data[13]),
        self.var_radio1.set(data[14])
    
    
    
    #delete button
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","DO you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                    my_cursor=conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted the student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
   
   
    #reset button
    def reset_data(self):
        self.var_Dep.set("Select Department"),
        self.var_Course.set("Select Course"),
        self.var_Year.set("Select Year"),
        self.var_Sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_Name.set(""),
        self.var_Div.set("Select Division"),
        self.var_Roll.set(""),
        self.var_Email.set(""),
        self.var_Mobileno.set(""),
        self.var_gen.set("Male"),
        self.var_dob.set(""),
        self.var_Address.set(""),
        self.var_Facultyname.set(""),
        self.var_radio1.set("")
                     
    #update buttuon
    def update_data(self):
        if (self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_id.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                    my_cursor=conn.cursor()
                    sql = "Update student set Dep = %s , Course = %s , Year = %s , Sem =%s , Name = %s , Division = %s , Roll = %s , Email = %s , Mobileno = %s , gen = %s , dob = %s , Address = %s , Facultyname = %s , photo = %s where id = %s"
                    data = (self.var_Dep.get(),self.var_Course.get(), self.var_Year.get(),self.var_Sem.get(),self.var_Name.get(),self.var_Div.get(),self.var_Roll.get(),self.var_Email.get(),self.var_Mobileno.get(),self.var_gen.get(),self.var_dob.get(),self.var_Address.get(),self.var_Facultyname.get(),self.var_radio1.get(),self.var_id.get())
                    my_cursor.execute(sql,data)
                
                else:
                    if not Update:
                        return    
                   
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Success","Student details Successfully updated",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    
    
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or  self.var_search1.get()=="":
            messagebox.showerror("Error","please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                my_cursor=conn.cursor()
          
                  
                search_term = self.var_search1.get()
                column_name = self.var_com_search.get()

                query = "SELECT * FROM student WHERE {} LIKE '%{}%'".format(column_name, search_term)

                my_cursor.execute(query)


                
                
                
                
                
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)       
                
                
                
                
   #---- generate data set or take photo samples__
   
    def generate_dataset(self):
        if (self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_id.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Division=%s,Roll=%s,Email=%s,Mobileno=%s,gen=%s,dob=%s,Address=%s,Facultyname=%s,photo=%s where id=%s",(
                                                                                                                                                                                                        self.var_Dep.get(),
                                                                                                                                                                                                        self.var_Course.get(),
                                                                                                                                                                                                        self.var_Year.get(),
                                                                                                                                                                                                        self.var_Sem.get(),
                                                                                                                                                                                                        self.var_Name.get(),
                                                                                                                                                                                                        self.var_Div.get(),
                                                                                                                                                                                                        self.var_Roll.get(),
                                                                                                                                                                                                        self.var_Email.get(),
                                                                                                                                                                                                        self.var_Mobileno.get(),
                                                                                                                                                                                                        self.var_gen.get(),
                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                        self.var_Address.get(),
                                                                                                                                                                                                        self.var_Facultyname.get(),
                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                        self.var_id.get()==id+1
                                                                                                                                                                                                   ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
# face classifier
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0) 
             
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        faces=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,faces)
                        cv2.putText(faces, str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)     
                 
                           
                       

                
                
                
                
                
                      
        
if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()        