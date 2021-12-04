from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql
import mysql.connector
from main import Face_recognition_system

from login import login_window


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration")
        self.root.geometry('1366x768+0+0')

        # Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_confirm_pass=StringVar()
        self.var_Security=StringVar()
        self.var_Security_entry=StringVar()
        self.var_check=IntVar()
        

         # background images
        img=Image.open(r"D:\Projects\Attendence_system\images\keyboard.jpg")
        img=img.resize((1366,768),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.Photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #leftimage
        img1=Image.open(r"D:\Projects\Attendence_system\images\quotes1.jpg")
        img1=img1.resize((500,470),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.Photoimg1)
        bg_img1.place(x=60,y=100,width=500,height=500)

        frame=Frame(self.root,bg='white')
        frame.place(x=560,y=100,width=750,height=500)

        #get_str=Label(frame,text="Register Here",font=("times new roman",20,'bold '),fg='green',bg='white')
        #get_str.place(x=9,y=5)

        Class_student_frame=LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text='Register Here',font=("times new roman",15,"bold italic"))
        Class_student_frame.place(x=0,y=10,width=747,height=599)

        # First_name
        student_id=Label(Class_student_frame,text="First Name-",font=("times new roman",12,"bold italic"),bg='white')
        student_id.grid(row=0,column=0,padx=5,pady=20)

        student_id_entry=ttk.Entry(Class_student_frame,textvariable=self.var_fname,font=("times new roman",12,"bold italic"))
        student_id_entry.grid(row=0,column=1,padx=5,pady=20)

        # Student name
        student_name=Label(Class_student_frame,text="Last Name-",font=("times new roman",12,"bold italic"),bg='white')
        student_name.grid(row=0,column=3,padx=5,pady=20)

        student_name_entry=ttk.Entry(Class_student_frame,textvariable=self.var_lname,font=("times new roman",12,"bold italic"))
        student_name_entry.grid(row=0,column=4,padx=5,pady=20)


         # Student Roll no
        student_roll_no=Label(Class_student_frame,text="Contact No-",font=("times new roman",12,"bold italic"),bg='white')
        student_roll_no.grid(row=1,column=0,padx=5,pady=20)

        student_roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_contact,font=("times new roman",12,"bold italic"))
        student_roll_no_entry.grid(row=1,column=1,padx=5,pady=20)\


        student_roll_no=Label(Class_student_frame,text="Email-",font=("times new roman",12,"bold italic"),bg='white')
        student_roll_no.grid(row=1,column=3,padx=5,pady=20)

        student_roll_no_entry=ttk.Entry(Class_student_frame,textvariable=self.var_email,font=("times new roman",12,"bold italic"))
        student_roll_no_entry.grid(row=1,column=4,padx=5,pady=20)


        gender=Label(Class_student_frame,text="Security Question-",font=("times new roman",12,"bold italic"),bg='white')
        gender.grid(row=2,column=0,padx=5,pady=20)

        gender_combo=ttk.Combobox(Class_student_frame,textvariable=self.var_Security,font=("times new roman",12,"italic"),state='readonly')
        gender_combo['values']=('Select Security Question','Birth Place','Pet Name')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=3,pady=20)

        security_ans=Label(Class_student_frame,text="Security Answer",font=("times new roman",12,"bold italic"),bg='white')
        security_ans.grid(row=2,column=3,padx=5,pady=20)

        security_ans_entry=ttk.Entry(Class_student_frame,textvariable=self.var_Security_entry,font=("times new roman",12,"bold italic"))
        security_ans_entry.grid(row=2,column=4,padx=5,pady=20)

        password=Label(Class_student_frame,text="Password-",font=("times new roman",12,"bold italic"),bg='white')
        password.grid(row=3,column=0,padx=5,pady=20)

        password_entry=ttk.Entry(Class_student_frame,textvariable=self.var_pass,font=("times new roman",12,"bold italic"))
        password_entry.grid(row=3,column=1,padx=5,pady=20)

        c_password=Label(Class_student_frame,text="Conform Password-",font=("times new roman",12,"bold italic"),bg='white')
        c_password.grid(row=3,column=3,padx=5,pady=20)

        c_password_entry=ttk.Entry(Class_student_frame,textvariable=self.var_confirm_pass,font=("times new roman",12,"bold italic"))
        c_password_entry.grid(row=3,column=4,padx=5,pady=20)


        # check button

        check_button=Checkbutton(frame,text="I agree the terms and Conditions ",variable=self.var_check,font=("times new roman",12,"italic"),bg='white')

        check_button.place(x=50,y=310)

        register_button=Button(frame,text='Register Now',command=self.register,width=16,font=("times new roman",12,"bold italic"),bg='red',fg='black',bd=3,activebackground='red')
        register_button.place(x=50,y=400,height=50)

        # Login button
        login_button=Button(frame,text='Login',width=16,font=("times new roman",12,"bold italic"),bg='green',fg='white',bd=3,activebackground='red')
        login_button.place(x=500,y=400,height=50)



    def register(self):
        if self.var_fname.get()=="" or self.var_email.get()=='' or self.var_Security.get()=='Select Security Question':
            messagebox.showerror('Error', 'All fields are required')
        elif self.var_pass.get()!=self.var_confirm_pass.get():
            messagebox.showerror('Error', 'password and Confirm Password must be same')
        elif self.var_check.get()==0:
            messagebox.showerror('Error', 'Please Agree with Our Terms and Condition')
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='zafeer@786',database='attendence_system')
            my_cursor=conn.cursor()
            query=("select * from login_data where userid=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,Please try with another mail")
            else:
                my_cursor.execute("insert into login_data values (%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_check.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        
                                                                                        
                                                                                        self.var_Security.get(),
                                                                                        self.var_Security_entry.get(),
                                                                                        self.var_pass.get()
                                                                                        ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")
            

        









   











if __name__=="__main__":
    root=Tk()
    app=register_window(root)
    root.mainloop()

        