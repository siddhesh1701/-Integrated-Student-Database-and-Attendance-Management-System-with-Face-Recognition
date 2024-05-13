from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import os
import numpy as np
import cv2


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        
        #title label
        title_lbl=Label(self.root,text="FACE RECOGNITION SYSTEM",font=("time new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
         #firstimgae
        img1=Image.open(r"G:\facedetection\college_image\facerecognition\IMG1.png")
        img1=img1.resize((950,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
        
        #secondimgae
        img2=Image.open(r"G:\facedetection\college_image\facerecognition\img2.jpg")
        img2=img2.resize((650,700),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl1=Label(self.root,image=self.photoimg2)
        f_lbl1.place(x=0,y=55,width=650,height=700)
        
        #button
        b11=Button(f_lbl,text="Face recognition",command=self.face_recog, cursor="hand2",font=("time new roman",15,"bold"),bg="white",fg="black")
        b11.place(x=420,y=620,width=200,height=40)
    
    #-----attendance system---
    def mark_attendance(self,r,n,d):
        with open("attend.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])

            if((r not in name_list) and (n not in name_list) and (d not in name_list)):    

                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present")
               
    
    
    
    
    
        
    #face recognition system  
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="9172834591",database="face_recognition") 
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Name from student where id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                
                
                
                
                
                
                if confidence>77:
                    
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"unknown face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),1)    
                coord=[x,y,w,h] 
 
            return coord   
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.2,10,(255,25,255),"faces",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")   
        
        video_cap=cv2.VideoCapture(0)
        if not video_cap.isOpened():
            
            print("Error: Could not open video capture device.")
            return
        
        while True:
            ret,img=video_cap.read()
            if not ret:
                print("Error: Failed to read video frame.")
                break
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                
                
            
            
        

        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()           