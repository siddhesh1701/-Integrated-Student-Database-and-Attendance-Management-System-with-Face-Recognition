from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import _mysql_connector
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        #firstimgae
        img=Image.open(r"G:\facedetection\college_image\train\img1.jpg")
        img=img.resize((1530,325),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=325)
        
        
        #secondimgae
        img2=Image.open(r"G:\facedetection\college_image\train\img2.png")
        img2=img2.resize((1530,325),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=440,width=1530,height=325)
        
        #title label
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("time new roman",35,"bold"),bg="yellow",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #button
        b11=Button(self.root,text="TRAIN DATA BUTTON",command=self.train_classifier,cursor="hand2",font=("time new roman",25,"bold"),bg="black",fg="yellow")
        b11.place(x=0,y=380,width=1530,height=60)
        
    #TRAINING THE DATA VIA LBPH ALGO
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')  #datatype of array uint8
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("TRAINING",imageNp)
            cv2.waitKey(1)==13 #to close the window after clicking enter buttton
        ids=np.array(ids)
        
        # train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed")
        os.system("python main.py")
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()                
    
    
    
    #install pip3 install opencv-contrib-python if opencv not working