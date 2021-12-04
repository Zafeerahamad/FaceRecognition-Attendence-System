import numpy as np
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student_detail import Student
from train import Train
from recognition import Face_r
import os
from time import strftime
from datetime import datetime
import csv
from tkinter import messagebox
from tkinter import filedialog

my_data=[]
class Attendence:
    def __init__(self,root) :
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")
        # ================== Variable ===============
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_std_id=StringVar()
        self.var_roll=StringVar()

        self.var_Attendence_status=StringVar()

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
        img3=Image.open(r"D:\Projects\Attendence_system\images\new_img.jpg")
        img3=img3.resize((1366,568),Image.ANTIALIAS)
        self.Photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0,y=200,width=1366,height=568)

        # title label
        title_lbl=Label(bg_img,text="Attendence Management System",font=('times new roman',30,'bold'),bg='white',fg='blue')
        title_lbl.place(x=0,y=0,width=1366,height=45)



        # Main Frame
        main_frame=Frame(bg_img,bd=2,bg="sky blue")
        main_frame.place(x=0,y=45,width=1366,height=528)

        # Left Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="beige",relief=RIDGE,text='Students Attendence Detail',font=("times new roman",15,"bold italic"))
        left_frame.place(x=0,y=0,width=643,height=528)


        # right Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="beige",relief=RIDGE,text='Students Attendence Detail',font=("times new roman",15,"bold italic"))
        right_frame.place(x=733,y=0,width=633,height=528)

        #left_inside_frame=LabelFrame(left_frame,bd=2,bg="light orange",relief=RIDGE,text='Students Attendence Detail',font=("times new roman",15,"bold italic"))
        #left_inside_frame.place(x=0,y=0,width=643,height=528)

        # Student id
        student_id=Label(left_frame,text="Student ID -",font=("times new roman",12,"bold italic"),bg='beige')
        student_id.grid(row=0,column=0,padx=5,pady=20)

        student_id_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,font=("times new roman",12,"bold italic"))
        student_id_entry.grid(row=0,column=1,padx=5,pady=20)

        # Student Roll no
        student_roll_no=Label(left_frame,text="Roll No -",font=("times new roman",12,"bold italic"),bg='beige')
        student_roll_no.grid(row=0,column=2,padx=5,pady=20)

        student_roll_no_entry=ttk.Entry(left_frame,textvariable=self.var_roll,font=("times new roman",12,"bold italic"))
        student_roll_no_entry.grid(row=0,column=3,padx=5,pady=20)

        # Student name
        student_name=Label(left_frame,text="Student Name -",font=("times new roman",12,"bold italic"),bg='beige')
        student_name.grid(row=1,column=0,padx=5,pady=10)

        student_name_entry=ttk.Entry(left_frame,textvariable=self.var_name,font=("times new roman",12,"bold italic"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=10)

        #Department label
        dep_label=Label(left_frame,text='Department -',font=("times new roman",12,"bold italic"),bg='beige')
        dep_label.grid(row=1,column=2,padx=5,pady=10)

        dep_combo=ttk.Combobox(left_frame,textvariable=self.var_dep,font=("times new roman",12,"italic"),state='readonly')
        dep_combo["values"]=('Select Your Department','CSE','IT','ME','EE','ECE','BT','ChE')
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=5,pady=10)

        # Time
        time=Label(left_frame,text="Time -",font=("times new roman",12,"bold italic"),bg='beige')
        time.grid(row=2,column=0,padx=5,pady=10)

        time_entry=ttk.Entry(left_frame,textvariable=self.var_time,font=("times new roman",12,"bold italic"))
        time_entry.grid(row=2,column=1,padx=5,pady=10)

        # Date
        date=Label(left_frame,text="Date -",font=("times new roman",12,"bold italic"),bg='beige')
        date.grid(row=2,column=2,padx=5,pady=10)

        date_entry=ttk.Entry(left_frame,textvariable=self.var_date,font=("times new roman",12,"bold italic"))
        date_entry.grid(row=2,column=3,padx=5,pady=10)

        # Attendence Status
        Attend_status_label=Label(left_frame,text='Attendence_Status -',font=("times new roman",12,"bold italic"),bg='beige')
        Attend_status_label.grid(row=3,column=0,padx=5,pady=10)

        Attend_status_combo=ttk.Combobox(left_frame,textvariable=self.var_Attendence_status,font=("times new roman",12,"italic"),state='readonly')
        Attend_status_combo["values"]=('Status','Present','Absent')
        Attend_status_combo.current(0)
        Attend_status_combo.grid(row=3,column=1,padx=5,pady=10)

        
        #Button Frame
        btn_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=220,width=633,height=140)

        save_btn=Button(btn_frame,text='Import CSV',command=self.import_csv,width=16,font=("times new roman",12,"bold italic"),bg='green')
        save_btn.grid(row=0,column=0,padx=3,pady=10)

        export_btn=Button(btn_frame,text='Export CSV',command=self.export_csv,width=16,font=("times new roman",12,"bold italic"),bg='grey')
        export_btn.grid(row=0,column=1,padx=3,pady=10)

        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=16,font=("times new roman",12,"bold italic"),bg='light blue')
        reset_btn.grid(row=0,column=2,padx=3,pady=10)

        update_btn=Button(btn_frame,text='Update',width=16,font=("times new roman",12,"bold italic"),bg='red')
        update_btn.grid(row=0,column=3,padx=4,pady=10)

        # table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=0,y=0,width=623,height=350)

        # setting the scroll bar
        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('ID','Roll_No','Name','Dep','Time','Date','Attendence_Status'))

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_x.config(command=self.student_table.xview)
        scrol_y.config(command=self.student_table.yview)
        self.student_table.heading('ID',text='ID')
        
        self.student_table.heading('Roll_No',text='Roll_number')
        self.student_table.heading('Name',text='Name')
        #self.student_table.heading('Gender',text='Gender')
        #self.student_table.heading('Course',text='Course')
        self.student_table.heading('Dep',text='Department')
        self.student_table.heading("Time",text='Time')
        self.student_table.heading('Date',text='Date')
        #self.student_table.heading('DOB',text='DOB')
        self.student_table.heading('Attendence_Status',text='Attendence_Status')
        #self.student_table.heading('Phone_No',text='Phone_number')
        #self.student_table.heading('Photo_Sample',text='Photo Sample')
        self.student_table["show"]='headings'

        self.student_table.column('ID',width=100)
        
        self.student_table.column('Roll_No',width=100)
        self.student_table.column('Name',width=100)
        #self.student_table.column('Gender',width=100)
        #self.student_table.column('Course',width=100)
        self.student_table.column('Dep',width=100) 
        self.student_table.column('Time',width=100)
        self.student_table.column('Date',width=100)
        self.student_table.column('Attendence_Status',width=100)
        #self.student_table.column('E_Mail',width=100)
        #self.student_table.column('Phone_No',width=100)
        #self.student_table.column('Photo_Sample',width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        #self.fetch_data()


    # ============= Fetch Data ==================
    def fetch_data(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)


    #  import csv
    def import_csv(self):
        global my_data
        my_data.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",'*.csv'),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csv_read=csv.reader(myfile, delimiter=",")
            for i in csv_read:
                my_data.append(i)
            self.fetch_data(my_data)


    # Export csv

    def export_csv(self):
        try:
            if len(my_data)<1:
                messagebox.showerror("NO DATA","No Data Found To Export",parent=self.root)
                return False

            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File",'*.csv'),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in my_data:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Yor data  Exported to " +os.path.basename(fln) +" Succsfully",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Due To {str(e)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        

        [self.var_std_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        
        self.var_Attendence_status.set(data[6])]
        #self.var_semester.set(data[7]),
        #self.var_dob.set(data[8]),
        #self.var_email.set(data[9]),
        #self.var_Phone.set(data[10]),
        #self.var_radio1.set(data[11])]

    # ========== reset_data ===============
    def reset_data(self):
        self.var_std_id.set("")
        
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")            
        
        self.var_Attendence_status.set("select")
            












if __name__== "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()