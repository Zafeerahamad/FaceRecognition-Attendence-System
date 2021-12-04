import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_detail import Student
from train import Train
from recognition import Face_r
import os
import csv
from time import strftime
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog

class Help:
    def __init__(self,root) :
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Help Window")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="HELP",font=('times new roman',25,'bold'),bg='white',fg='green')
        title_lbl.place(x=0,y=0,width=1366,height=40)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='white',fg='blue')
        lbl.place(x=5,y=0,width=110,height=40)
        time()

        img=Image.open(r"D:\Projects\Attendence_system\images\keyboard.jpg")
        img=img.resize((1366,670),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        f_label=Label(self.root,image=self.Photoimg)
        f_label.place(x=0,y=41,width=1366,height=670)


        main_frame=Frame(f_label,bd=2,bg="black")
        main_frame.place(x=700,y=40,width=500,height=150)
        email=Label(main_frame,text="E-Mail :- zafeer20898@gmail.com",font=('times new roman',15,'bold'),bg='black',fg='white')
        email.grid(row=1,column=0,padx=5,pady=10)




if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()