import tkinter
from tkinter import messagebox
import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student_detail import Student
from train import Train
from recognition import Face_r
from attendence import Attendence
from developer import Developer
from help import Help

import os


class Face_recognition_system:
    def __init__(self,root) :
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        img=Image.open(r"D:\Projects\Attendence_system\images\img1.jpg")
        img=img.resize((800,200),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        f_label=Label(self.root,image=self.Photoimg)
        f_label.place(x=0,y=0,width=283,height=200)

        img1=Image.open(r"D:\Projects\Attendence_system\images\university_img1.jpg")
        img1=img1.resize((800,200),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        f_label1=Label(self.root,image=self.Photoimg1)
        f_label1.place(x=283,y=0,width=800,height=200)

        img2=Image.open(r"D:\Projects\Attendence_system\images\img1.jpg")
        img2=img2.resize((800,200),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)
        f_label2=Label(self.root,image=self.Photoimg2)
        f_label2.place(x=1083,y=0,width=283,height=200)

        # background Image
        img3=Image.open(r"D:\Projects\Attendence_system\images\keyboard.jpg")
        img3=img3.resize((1366,568),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0,y=200,width=1366,height=568)

        # title label
        title_lbl=Label(bg_img,text="FACE RCOGNITION ATTENDENCE SYSTEM SOFTWARE",font=('times new roman',30,'bold'),bg='white',fg='blue')
        title_lbl.place(x=0,y=0,width=1366,height=40)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='white',fg='blue')
        lbl.place(x=5,y=0,width=110,height=50)
        time()


        #student Detail button 
        img4=Image.open(r"D:\Projects\Attendence_system\images\download.jpg")
        img4=img4.resize((180,160),Image.ANTIALIAS)
        self.Photoimg4=ImageTk.PhotoImage(img4)
        stud_img=Button(bg_img,command=self.student_details,image=self.Photoimg4,cursor='hand2')
        stud_img.place(x=150,y=50,width=180,height=160)

        # button 
        b1=Button(bg_img,command=self.student_details,text="Students Detail",cursor='hand2',font=('times new roman',15,'bold'),bg='white',fg='blue')
        b1.place(x=150,y=210,width=180,height=25)

        # Face Recognition Button
        img5=Image.open(r"D:\Projects\Attendence_system\images\img1.jpg")
        img5=img5.resize((180,160),Image.ANTIALIAS)
        self.Photoimg5=ImageTk.PhotoImage(img5)
        stud_img1=Button(bg_img,image=self.Photoimg5,cursor='hand2',command=self.face_r_window)
        stud_img1.place(x=445,y=50,width=180,height=160)

        # button 
        b2=Button(bg_img,text="Face Recognition",cursor='hand2',command=self.face_r_window,font=('times new roman',15,'bold'),bg='white',fg='blue')
        b2.place(x=445,y=210,width=180,height=25)


        # Attendence Button
       
        img6=Image.open(r"D:\Projects\Attendence_system\images\images.jpg")
        img6=img6.resize((180,160),Image.ANTIALIAS)
        self.Photoimg6=ImageTk.PhotoImage(img6)
        stud_img2=Button(bg_img,image=self.Photoimg6,cursor='hand2',command=self.attendence_data)
        stud_img2.place(x=740,y=50,width=180,height=160)

        # button 
        b3=Button(bg_img,text="Attendence",cursor='hand2',command=self.attendence_data,font=('times new roman',15,'bold'),bg='white',fg='blue')
        b3.place(x=740,y=210,width=180,height=25)
        

        #chatbot button

        img7=Image.open(r"D:\Projects\Attendence_system\images\images (9).jpg")
        img7=img7.resize((180,160),Image.ANTIALIAS)
        self.Photoimg7=ImageTk.PhotoImage(img7)
        stud_img3=Button(bg_img,image=self.Photoimg7,cursor='hand2',command=self.help_window)
        stud_img3.place(x=1035,y=50,width=180,height=160)

        # button 
        b4=Button(bg_img,text="Chat Bot",cursor='hand2',command=self.help_window,font=('times new roman',15,'bold'),bg='white',fg='blue')
        b4.place(x=1035,y=210,width=180,height=25)


     # train data Button

        img8=Image.open(r"D:\Projects\Attendence_system\images\images (1).jpg")
        img8=img8.resize((180,160),Image.ANTIALIAS)
        self.Photoimg8=ImageTk.PhotoImage(img8)
        stud_img4=Button(bg_img,image=self.Photoimg8,cursor='hand2',command=self.train_data)
        stud_img4.place(x=150,y=285,width=180,height=160)

        # button 
        b5=Button(bg_img,text="Train Data",command=self.train_data,cursor='hand2',font=('times new roman',15,'bold'),bg='white',fg='blue')
        b5.place(x=150,y=445,width=180,height=25)

    # photos
        img9=Image.open(r"D:\Projects\Attendence_system\images\images (12).jpg")
        img9=img9.resize((180,160),Image.ANTIALIAS)
        self.Photoimg9=ImageTk.PhotoImage(img9)
        stud_img5=Button(bg_img,image=self.Photoimg9,cursor='hand2',command=self.open_images)
        stud_img5.place(x=445,y=285,width=180,height=160)

        # button 
        b6=Button(bg_img,text="Photos",command=self.open_images,cursor='hand2',font=('times new roman',15,'bold'),bg='white',fg='blue')
        b6.place(x=445,y=445,width=180,height=25)

    # Developer
        img10=Image.open(r"D:\Projects\Attendence_system\images\images (11).jpg")
        img10=img10.resize((180,160),Image.ANTIALIAS)
        self.Photoimg10=ImageTk.PhotoImage(img10)
        stud_img6=Button(bg_img,image=self.Photoimg10,cursor='hand2',command=self.developer_data)
        stud_img6.place(x=740,y=285,width=180,height=160)

        # button 
        b7=Button(bg_img,text="Developer",cursor='hand2',command=self.developer_data,font=('times new roman',15,'bold'),bg='white',fg='blue')
        b7.place(x=740,y=445,width=180,height=25)

    # Exit Button

        img11=Image.open(r"D:\Projects\Attendence_system\images\images (4).jpg")
        img11=img11.resize((180,160),Image.ANTIALIAS)
        self.Photoimg11=ImageTk.PhotoImage(img11)
        stud_img7=Button(bg_img,image=self.Photoimg11,command=self.iexit,cursor='hand2')
        stud_img7.place(x=1035,y=285,width=180,height=160)

        # button
        b8=Button(bg_img,text="Exit",cursor='hand2',command=self.iexit,font=('times new roman',15,'bold'),bg='white',fg='blue')
        b8.place(x=1035,y=445,width=180,height=25)


    def iexit(self):
        iexit=messagebox.askyesno("Face recognition","Are you Sure Want to Exit ?")
        if iexit>0:
            self.root.destroy()
        else:
             return 
    #  ======function_buttons=========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_r_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_r(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    


    #  Open images
    def open_images(self):
        os.startfile('Training_images')
        










if __name__== "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()

