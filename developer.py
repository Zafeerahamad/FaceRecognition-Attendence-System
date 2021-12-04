import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_detail import Student
from train import Train
from recognition import Face_r
from time import strftime
from datetime import datetime
import os
import csv
from tkinter import messagebox
from tkinter import filedialog

class Developer:
    def __init__(self,root) :
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Developer System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="DEVELOPER",font=('times new roman',25,'bold'),bg='white',fg='green')
        title_lbl.place(x=0,y=0,width=1366,height=40)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='white',fg='blue')
        lbl.place(x=5,y=0,width=110,height=40)
        time()

        img=Image.open(r"D:\Projects\Attendence_system\images\new_img.jpg")
        img=img.resize((1366,670),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        f_label=Label(self.root,image=self.Photoimg)
        f_label.place(x=0,y=41,width=1366,height=670)

        # Main Frame
        main_frame=Frame(f_label,bd=2,bg="sky blue")
        main_frame.place(x=866,y=0,width=500,height=670)

        img1=Image.open(r"D:\Projects\Attendence_system\images\my_first.jpg")
        img1=img1.resize((200,228),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        f_label=Label(main_frame,image=self.Photoimg1)
        f_label.place(x=300,y=0,width=200,height=228)

        # Developer Info

        dev_label=Label(main_frame,text="Hello, my name is Zafeer Ahamad, and \n I am a Machine Learning Engineer.",font=('times new roman',18,'bold'),bg='sky blue',fg='black')
        dev_label.place(x=0,y=230)

        contact_frame=LabelFrame(main_frame,bd=2,bg="sky blue")
        contact_frame.place(x=0,y=340,width=500,height=330)

        email=Label(contact_frame,text="E-Mail :- zafeer20898khan@gmail.com",font=('times new roman',15,'bold'),bg='sky blue',fg='black')
        email.grid(row=0,column=0,padx=5,pady=10)

        Github=Label(contact_frame,text="Github link :- https://github.com/Zafeerahamad",font=('times new roman',15,'bold'),bg='sky blue',fg='black')
        Github.grid(row=1,column=0,padx=5,pady=10)











if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()