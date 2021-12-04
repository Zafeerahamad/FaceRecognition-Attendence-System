import numpy as np
import cv2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student_detail import Student
import random
import os
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Train Dataset",font=('times new roman',30,'bold'),bg='sky blue',fg='black')
        title_lbl.place(x=0,y=0,width=1366,height=40)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='sky blue',fg='black')
        lbl.place(x=5,y=0,width=110,height=40)
        time()

        # background Image
        img3=Image.open(r"D:\Projects\Attendence_system\images\keyboard.jpg")
        img3=img3.resize((1366,568),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0,y=241,width=1366,height=527)

        img=Image.open(r"D:\Projects\Attendence_system\images\new_img1.jpg")
        img=img.resize((283,400),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        f_label=Label(self.root,image=self.Photoimg)
        f_label.place(x=0,y=41,width=283,height=400)

        img1=Image.open(r"D:\Projects\Attendence_system\images\images (21).jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        f_label1=Label(self.root,image=self.Photoimg1)
        f_label1.place(x=283,y=41,width=800,height=200)

        img2=Image.open(r"D:\Projects\Attendence_system\images\new_img1.jpg")
        img2=img2.resize((283,400),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)
        f_label2=Label(self.root,image=self.Photoimg2)
        f_label2.place(x=1083,y=41,width=283,height=400)

    



        #Button
        b1=Button(bg_img,text="Click here to Train Data",command=self.train_classifier,cursor='hand2',font=('times new roman',25,'bold'),bg='red',fg='white')
        b1.place(x=283,y=0,height=50,width=1083)


    # training method
    def train_classifier(self):
        data_dir=r"D:\Projects\Attendence_system\Training_images"
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')  # it means it is a greyscale image
            img_array=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #print(id)
            #print(os.path)
            #print(os.path.split(image),image)
            faces.append(img_array)
            ids.append(id)
            cv2.imshow('Training',img_array)
            cv2.waitKey(1)==13
        zipping=list(zip(faces,ids))
        random.shuffle(zipping)
        faces,ids=[[i for i,j in zipping],[j for i,j in zipping]]

        ids=np.array(ids)

        #  Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed !")

if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
