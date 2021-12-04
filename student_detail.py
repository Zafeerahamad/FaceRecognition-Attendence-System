from tkinter import * 
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
from time import strftime
from datetime import datetime
from cv2 import VideoCapture
import mysql.connector
import matplotlib.pyplot as plt
import time
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768")
        self.root.title("Student Detail") 
        self.root.wm_iconbitmap("face.ico")  # used for face icon used in exe fil
        


        # ================== Variable ===============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_Phone=StringVar()
        self.var_dob=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_search_entry=StringVar()
        self.var_search=StringVar()






        img=Image.open(r"D:\Projects\Attendence_system\images\images.jpg")
        img=img.resize((455,150),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        f_label=Label(self.root,image=self.Photoimg)
        f_label.place(x=2,y=0,width=455,height=150)

        img1=Image.open(r"D:\Projects\Attendence_system\images\images (3).jpg")
        img1=img1.resize((455,150),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        f_label1=Label(self.root,image=self.Photoimg1)
        f_label1.place(x=457,y=0,width=455,height=150)

        img2=Image.open(r"D:\Projects\Attendence_system\images\images.jpg")
        img2=img2.resize((455,150),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)
        f_label2=Label(self.root,image=self.Photoimg2)
        f_label2.place(x=912,y=0,width=455,height=150)

        # Background Images
        img3=Image.open(r"D:\Projects\Attendence_system\images\download (2).jpg")
        img3=img3.resize((1366,568),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0,y=150,width=1366,height=568)

        #Title Label

        title_lbl=Label(bg_img,text="Student Management System",font=('times new roman',30,'bold'),bg='white',fg='dark blue')
        title_lbl.place(x=0,y=0,width=1366,height=45)
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),bg='white',fg='blue')
        lbl.place(x=5,y=0,width=110,height=50)
        time()

        # Main Frame
        main_frame=Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=0,y=45,width=1366,height=528)

        # Left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text='Students Detail',font=("times new roman",15,"bold italic"))
        left_frame.place(x=0,y=0,width=643,height=528)


        # right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text='Students Detail',font=("times new roman",15,"bold italic"))
        right_frame.place(x=733,y=0,width=633,height=528)

        # current Course Details Frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text='Current Course Details',font=("times new roman",15,"bold italic"))
        current_course_frame.place(x=0,y=10,width=633,height=120)

        #course label
        dep_label=Label(current_course_frame,text='Course -',font=("times new roman",12,"bold italic"),bg='white')
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"italic"),state='readonly')
        dep_combo["values"]=('Select Course','B.Tech','B.SC','BE','Diploma')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10)



        #Department label
        dep_label=Label(current_course_frame,text='Department -',font=("times new roman",12,"bold italic"),bg='white')
        dep_label.grid(row=0,column=2)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"italic"),state='readonly')
        dep_combo["values"]=('Select Your Department','CSE','IT','ME','EE','ECE','BT','ChE')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=3,pady=10)


        # Year Label
        yr_label=Label(current_course_frame,text='Year -',font=("times new roman",12,"bold italic"),bg='white')
        yr_label.grid(row=1,column=0,padx=3,pady=10)

        yr_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"italic"),state='readonly')
        yr_combo["values"]=('Select Your Year','1st-year','2nd-year','3rd-year','4th-year')
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1,padx=3,pady=10)

        # semester Label
        sm_label=Label(current_course_frame,text='Semester -',font=("times new roman",12,"bold italic"),bg='white')
        sm_label.grid(row=1,column=2,padx=3,pady=10)

        sm_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"italic"),state='readonly')
        sm_combo["values"]=('Select Semester','First Semester','Second Semester')
        sm_combo.current(0)
        sm_combo.grid(row=1,column=3,padx=3,pady=10)

        # Class student Information Frame

        Class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text='Class Students Details',font=("times new roman",15,"bold italic"))
        Class_student_frame.place(x=0,y=135,width=633,height=393)

        # Student id
        student_id=Label(Class_student_frame,text="Student ID -",font=("times new roman",12,"bold italic"),bg='white')
        student_id.grid(row=0,column=0,padx=3,pady=10)

        student_id_entry=ttk.Entry(Class_student_frame,textvariable=self.var_std_id,font=("times new roman",12,"bold italic"))
        student_id_entry.grid(row=0,column=1,padx=3,pady=10)

        # Student name
        student_name=Label(Class_student_frame,text="Student Name -",font=("times new roman",12,"bold italic"),bg='white')
        student_name.grid(row=0,column=2,padx=3,pady=10)

        student_name_entry=ttk.Entry(Class_student_frame,textvariable=self.var_name,font=("times new roman",12,"bold italic"))
        student_name_entry.grid(row=0,column=3,padx=3,pady=10)


         # Student Roll no
        student_roll_no=Label(Class_student_frame,text="Roll No -",font=("times new roman",12,"bold italic"),bg='white')
        student_roll_no.grid(row=1,column=0,padx=3,pady=10)

        student_roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_roll,font=("times new roman",12,"bold italic"))
        student_roll_no_entry.grid(row=1,column=1,padx=3,pady=10)

        # Gender
        gender=Label(Class_student_frame,text="Gender -",font=("times new roman",12,"bold italic"),bg='white')
        gender.grid(row=1,column=2,padx=3,pady=10)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"italic"),state='readonly')
        gender_combo['values']=('Select Gender','Male','Female','Others')
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=3,pady=10)

        # DOB

        dob=Label(Class_student_frame,text="Date Of Birth -",font=("times new roman",12,"bold italic"),bg='white')
        dob.grid(row=2,column=0,padx=3,pady=10)

        dob_entry=ttk.Entry(Class_student_frame,textvariable=self.var_dob,text=" DD-MM-YYYY",font=("times new roman",12,"bold italic"))
        dob_entry.grid(row=2,column=1,padx=3,pady=10)

        # Email

        email=Label(Class_student_frame,text="Email ID -",font=("times new roman",12,"bold italic"),bg='white')
        email.grid(row=2,column=2,padx=3,pady=10)

        email_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,font=("times new roman",12,"bold italic"))
        email_entry.grid(row=2,column=3,padx=3,pady=10)


        # Phone number
        phoneno=Label(Class_student_frame,text="Phone No -",font=("times new roman",12,"bold italic"),bg='white')
        phoneno.grid(row=3,column=0,padx=3,pady=10)

        phoneno_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Phone,font=("times new roman",12,"bold italic"))
        phoneno_entry.grid(row=3,column=1,padx=3,pady=10)

        # Radio Button
        self.var_radio1=StringVar()
        radio_btn=Radiobutton(Class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value='Yes',font=("times new roman",12,"bold italic"),bg='white')
        radio_btn.grid(row=4,column=0,padx=3,pady=10)

        radio_btn2=Radiobutton(Class_student_frame,text="No Photo Sample",variable=self.var_radio1,value='No',font=("times new roman",12,"bold italic"),bg='white')
        radio_btn2.grid(row=4,column=1,padx=3,pady=10)

        #button frame

        btn_frame=LabelFrame(Class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=220,width=633,height=140)

        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=16,font=("times new roman",12,"bold italic"),bg='green')
        save_btn.grid(row=0,column=0,padx=3,pady=10)

        Update_btn=Button(btn_frame,text='Update',command=self.update_data,width=16,font=("times new roman",12,"bold italic"),bg='grey')
        Update_btn.grid(row=0,column=1,padx=3,pady=10)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=16,font=("times new roman",12,"bold italic"),bg='light blue')
        reset_btn.grid(row=0,column=2,padx=3,pady=10)

        delete_btn=Button(btn_frame,text='Delete',command=self.delete_data,width=16,font=("times new roman",12,"bold italic"),bg='red')
        delete_btn.grid(row=0,column=3,padx=4,pady=10)

        take_photo_btn=Button(btn_frame,text='Take Photo Sample',command=self.take_photo,width=16,font=("times new roman",12,"bold italic"),bg='green')
        take_photo_btn.grid(row=1,column=0,padx=4,pady=10)

        update_photo_btn=Button(btn_frame,text='Update Photo Sample',width=16,font=("times new roman",12,"bold italic"),bg='grey')
        update_photo_btn.grid(row=1,column=3,padx=4,pady=10)


        # ---- search system ------
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg='white')
        search_frame.place(x=0,y=10,width=623,height=100)

        search_label=Label(search_frame,text="SearchBy: -",font=("times new roman",12,"bold italic"),fg='blue',bg='white')
        search_label.grid(row=0,column=0,padx=3,pady=10)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",12,"italic"),state='readonly')
        search_combo['values']=('Select','Roll No','Phone No','Department')
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10)
        
        # search entry
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search_entry,font=("times new roman",12,"bold italic"))
        search_entry.grid(row=0,column=2,padx=2,pady=10)

        # search Button
        search_btn=Button(search_frame,text='Search',width=16,command=self.search_fun,font=("times new roman",12,"bold italic"),bg='light blue')
        search_btn.grid(row=1,column=2,padx=3,pady=10)

        #show all buttun
        showall_btn=Button(search_frame,text='Showall',command=self.showall,width=16,font=("times new roman",12,"bold italic"),bg='black',fg='white')
        showall_btn.grid(row=1,column=3,padx=3,pady=10)
         
         # Table Frame

        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=0,y=112,width=623,height=350)

        # setting the scroll bar
        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('ID','Name','Roll_No','Gender','Course','Dep','Year','Semester','DOB','E_Mail','Phone_No','Photo_Sample'))

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_x.config(command=self.student_table.xview)
        scrol_y.config(command=self.student_table.yview)

        self.student_table.heading('ID',text='ID')
        self.student_table.heading('Name',text='Name')
        self.student_table.heading('Roll_No',text='Roll_number')
        self.student_table.heading('Gender',text='Gender')
        self.student_table.heading('Course',text='Course')
        self.student_table.heading('Dep',text='Department')
        self.student_table.heading('Year',text='Year')
        self.student_table.heading('Semester',text='Semester')
        self.student_table.heading('DOB',text='DOB')
        self.student_table.heading('E_Mail',text='Email')
        self.student_table.heading('Phone_No',text='Phone_number')
        self.student_table.heading('Photo_Sample',text='Photo Sample')
        self.student_table["show"]='headings'

        self.student_table.column('ID',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Roll_No',width=100)
        self.student_table.column('Gender',width=100)
        self.student_table.column('Course',width=100)
        self.student_table.column('Dep',width=100) 
        self.student_table.column('Year',width=100)
        self.student_table.column('Semester',width=100)
        self.student_table.column('DOB',width=100)
        self.student_table.column('E_Mail',width=100)
        self.student_table.column('Phone_No',width=100)
        self.student_table.column('Photo_Sample',width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



# ================ search data function ====================
    def search_fun(self):
        if self.var_search=='Select':
            messagebox.showinfo("Advice","First Select SearchBy then search will complete")
        elif self.var_search.get()=='Roll No':
            try:
                #messagebox.showinfo("Advice","before conn")
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
               
                query="Select * from student_details where RollNo=%s"
                #messagebox.showinfo("Advice","after query")
                val=(self.var_search_entry.get(),)
                #messagebox.showinfo("Advice","after val")

                my_cursor.execute(query,val)
                #messagebox.showinfo("Advice","after execute")
                data=my_cursor.fetchone()
                #print(data,val)
                #messagebox.showinfo("Advice","after fetchone")
                self.student_table.delete(*self.student_table.get_children())
                self.student_table.insert("",END,values=data)
                conn.commit()
                conn.close()
                #messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)
        elif self.var_search.get()=='Phone No':
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query="select * from student_details where PhoneNo=%s"
                value=(self.var_search_entry.get(),)
                my_cursor.execute(query,value)
                data=my_cursor.fetchone()
                self.student_table.delete(*self.student_table.get_children())
                self.student_table.insert("",END,values=data)
                conn.commit()
                #my_cursor.fetchone()
                conn.close()
                #messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)
        elif self.var_search.get()=='Department':
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                query="select * from student_details where Dep=%s"
                value=(self.var_search_entry.get(),)
                my_cursor.execute(query,value)
                data=my_cursor.fetchall()

                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
                #messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)

    # ================== Showall Function ===================
    def showall(self):
        self.fetch_data()



    # ============ functio declearation ===============
    
    def add_data(self) :

        if self.var_dep.get()=='Select Your Department' or self.var_std_id.get()=="" or self.var_name.get()=="" or self.var_course.get()=='Select Your Course' :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_std_id.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_roll.get(),
                                                                                        
                                                                                        self.var_gender.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_dep.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_semester.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_Phone.get(),
                                                                                        self.var_radio1.get()
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student detail has been added successfully",parent=self.root)


            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)


    # ======Fetch Data ==========
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_details")
                data= my_cursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()


    # =============get cursor===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        

        [self.var_std_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_roll.set(data[2]),
        self.var_gender.set(data[3]),
        self.var_course.set(data[4]),
        self.var_dep.set(data[5]),
        self.var_year.set(data[6]),
        self.var_semester.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_Phone.set(data[10]),
        self.var_radio1.set(data[11])]


    # ==========Update Function ================
    def update_data(self):
        if self.var_dep.get()=='Select Your Department' or self.var_std_id.get()=="" or self.var_name.get()=="" or self.var_course.get()=='Select Your Course' :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update the student detail",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student_details set Name=%s,RollNo=%s,Gender=%s,Course=%s,Dep=%s,Year=%s,Semester=%s,DOB=%s,EMail=%s,PhoneNo=%s,PhotoStatus=%s where StudentId=%s",(
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_std_id.get()))

                    
                else :
                    return
                conn.commit()
                messagebox.showinfo("Success","Student detail has been Updated successfully",parent=self.root)
                
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)

    # ==========delete Button ===============
    def delete_data(self):
        if self.var_std_id.get()=="" :
            messagebox.showerror("Error"," Student id is mandatory",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("delete","Do you want to delete the student detail",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system')
                    my_cursor=conn.cursor()
                    query="delete from student_details where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(query,val)
                else:
                    return

                conn.commit()
                messagebox.showinfo("Success","Student detail has been deleted successfully",parent=self.root)
                
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)


    # ========== reset_data ===============
    def reset_data(self):
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_course.set("Select Course")            
        self.var_dep.set("select Department")
        self.var_year.set("select Year")
        self.var_semester.set("select semester")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_Phone.set("")
        self.var_radio1.set("No")



    # =========Taking the Photo sample ====================
    def take_photo(self):
        if self.var_dep.get()=='Select Your Department' or self.var_std_id.get()=="" or self.var_name.get()=="" or self.var_course.get()=='Select Your Course' :
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_details")
                myres=my_cursor.fetchall()
                id=0
                for x in myres:
                    id+=1
                my_cursor.execute("update student_details set Name=%s,RollNo=%s,Gender=%s,Course=%s,Dep=%s,Year=%s,Semester=%s,DOB=%s,EMail=%s,PhoneNo=%s,PhotoStatus=%s where StudentId=%s",(
                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_std_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                name=self.var_name.get()
                std_id=self.var_std_id.get()
                photostatus=self.var_radio1.get()
                self.reset_data()
                conn.close()

                # load predefine data
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                def face_Cropped(img):
                    #face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    # minimum neighbours=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                if photostatus=='No' or photostatus=="":
                    messagebox.showinfo('Advice',"First select the Radio Button on (Take Photo Sample)")
                else:

                    cap=VideoCapture(0, cv2.CAP_DSHOW)
                    loop=True
                    img_id=0
                    while loop:
                        ret,myframe=cap.read()
                        if face_Cropped(myframe) is not None:
                            img_id+=1
                        else:
                            messagebox.showinfo('Note','Your face is not in the frame come in the frame')
                            continue
                        face=cv2.resize(face_Cropped(myframe),(550,550))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        file=r"D:\Projects\Attendence_system\Training_images\ "+str(name) +"."+str(std_id)+'.'+str(img_id)+".jpg"
                        cv2.imwrite(file,face)
                        #cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Cropped Face', face)
                        if (cv2.waitKey(1) & 0xFF == ord('q')) or (img_id==400) :

                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo('Result',"Generating dataset completed!!!")
            except Exception as e:
                messagebox.showerror("Error",f"Due To: {str(e)}",parent=self.root)

 


                





    








            
if __name__== "__main__":

    root=Tk()
    obj=Student(root)
    root.mainloop()