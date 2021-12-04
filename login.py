from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql
import mysql.connector
from main import Face_recognition_system


def main_fun():
    win=Tk()
    app=login_window(win)
    win.mainloop()

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry('1366x768+0+0')
        

        # background images
        img=Image.open(r"D:\Projects\Attendence_system\images\keyboard.jpg")
        img=img.resize((1366,768),Image.ANTIALIAS)
        self.Photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.Photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)


        # Login Frame
        frame=Frame(self.root,bg='black')
        frame.place(x=500,y=150,width=366,height=518)

        img1=Image.open(r"D:\Projects\Attendence_system\images\user.png")
        img1.resize((125,125),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(image=self.Photoimg1,bg='black',borderwidth=0)
        lblimg.place(x=605,y=150,width=125,height=125)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,'bold'),fg='white',bg='black')
        get_str.place(x=95,y=125)

        #label
        username=Label(frame,text="User Name",font=("times new roman",15,'bold'),fg='white',bg='black')
        username.place(x=70,y=195)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,'bold'))
        self.textuser.place(x=30,y=230,width=300)


        password=Label(frame,text="Password",font=("times new roman",15,'bold'),fg='white',bg='black')
        password.place(x=70,y=295)

        self.textpass=ttk.Entry(frame,font=("times new roman",15,'bold'))
        self.textpass.place(x=30,y=330,width=300)


        #=======icon images===========
        img2=Image.open(r"D:\Projects\Attendence_system\images\username.png")
        img2.resize((35,35),Image.ANTIALIAS)
        self.Photoimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(frame,image=self.Photoimg2,bg='black',borderwidth=0)
        lblimg1.place(x=30,y=190,width=35,height=35)

        img3=Image.open(r"D:\Projects\Attendence_system\images\icon1.png")
        img3.resize((35,35),Image.ANTIALIAS)
        self.Photoimg4=ImageTk.PhotoImage(img3)
        lblimg2=Label(frame,image=self.Photoimg4,bg='black',borderwidth=0)
        lblimg2.place(x=30,y=290,width=35,height=35)


        # Login button
        login_button=Button(frame,text='Login',command=self.login,width=16,cursor='hand2',font=("times new roman",12,"bold italic"),bg='red',fg='white',bd=3,activebackground='red')
        login_button.place(x=100,y=400,height=50)


        # regitration button
        reg_button=Button(frame,text='Register New User',command=self.register,cursor='hand2',font=("times new roman",12,"bold italic"),bg='black',fg='white',bd=0,activebackground='black')
        reg_button.place(x=30,y=465)

        # Forgot Password button
        for_button=Button(frame,text='Forgot Password',command=self.forgot_pass_window,cursor='hand2',font=("times new roman",12,"bold italic"),bg='black',fg='white',bd=0,activebackground='black')
        for_button.place(x=200,y=465)

    
    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=register_window(self.new_window)



    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","Both Fields are mandatory")

        #elif self.textuser.get()=="sg" or self.textpass.get()=="sdf":
        #    messagebox.showinfo("Success",'Welcome')

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='zafeer@786',database='attendence_system',auth_plugin='mysql_native_password')
            my_cursor=conn.cursor()
            query=("select * from login_data where userid=%s and password=%s",(self.textuser.get(),
                                                                                self.textpass.get()))
            #value=(self.var_email.get(),)
            my_cursor.execute("select * from login_data where userid=%s and password=%s",(self.textuser.get(),
                                                                                self.textpass.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid User name or password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recognition_system(self.new_window)
                else:
                    if not open_main:
                        return 

            conn.commit()
            conn.close()
    
    #===============reset password=================
    def reset_pass(self):
        if self.gender_combo.get()=='Select Security Question':
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.security_ans_entry.get()=='':
            messagebox.showerror("Error","Please Enter the answer",parent=self.root2)
        elif self.password_entry.get()=="":
            messagebox.showerror("Error","Please Enter Some Valid Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='zafeer@786',database='attendence_system')
            my_cursor=conn.cursor()
            my_cursor.execute("select * from login_data where userid=%s and SecurityAns=%s",(self.textuser.get(),
                                                                                self.security_ans_entry.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Security Ans",parent=self.root2)
            else:
                query=("update login_data set password=%s where userid=%s")
                value=(self.password_entry.get(),self.textuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been reset,Please Login for next page",parent=self.root2)
                self.root2.destroy()
            







    #=============forgot password===================
    def forgot_pass_window(self):
        if self.textuser.get()=='':
            messagebox.showerror("Error","Please Enter the Email Address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password='zafeer@786',database='attendence_system')
            my_cursor=conn.cursor()
           
    
            #value=(self.var_email.get(),)
            my_cursor.execute("select * from login_data where userid=%s",(self.textuser.get(),
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry('500x550+510+170')
                forgot_str=Label(self.root2,text="Reset Password",font=("times new roman",20,'bold'),fg='red',bg='white')

                forgot_str.place(x=0,y=10,width=550)

                C_frame=LabelFrame(self.root2,bd=2,bg="white",relief=RIDGE,font=("times new roman",15,"bold italic"))
                C_frame.place(x=0,y=50,width=550,height=500)

                gender=Label(C_frame,text="Security Question-",font=("times new roman",12,"bold italic"),bg='white')
                gender.grid(row=0,column=0,padx=5,pady=20)

                self.gender_combo=ttk.Combobox(C_frame,font=("times new roman",12,"italic"),state='readonly')
                self.gender_combo['values']=('Select Security Question','Birth Place','Pet Name')
                self.gender_combo.current(0)
                self.gender_combo.grid(row=0,column=1,padx=3,pady=20)

                security_ans=Label(C_frame,text="Security Answer-",font=("times new roman",12,"bold italic"),bg='white')
                security_ans.grid(row=1,column=0,padx=5,pady=20)

                self.security_ans_entry=ttk.Entry(C_frame,font=("times new roman",12,"bold italic"))
                self.security_ans_entry.grid(row=1,column=1,padx=5,pady=20)

                password=Label(C_frame,text="New Password-",font=("times new roman",12,"bold italic"),bg='white')
                password.grid(row=2,column=0,padx=5,pady=20)

                self.password_entry=ttk.Entry(C_frame,font=("times new roman",12,"bold italic"))
                self.password_entry.grid(row=2,column=1,padx=5,pady=20)

                c_password=Label(C_frame,text="Conform New Password-",font=("times new roman",12,"bold italic"),bg='white')
                c_password.grid(row=3,column=0,padx=5,pady=20)

                self.c_password_entry=ttk.Entry(C_frame,font=("times new roman",12,"bold italic"))
                self.c_password_entry.grid(row=3,column=1,padx=5,pady=20)
                # Reset button
                reset_button=Button(C_frame,text='Reset Password',command=self.reset_pass,width=16,font=("times new roman",12,"bold italic"),bg='brown',fg='white',bd=3,activebackground='red')
                reset_button.place(x=80,y=300,height=50)




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
        login_button=Button(frame,text='Login',command=self.return_login,width=16,font=("times new roman",12,"bold italic"),bg='green',fg='white',bd=3,activebackground='red')
        login_button.place(x=500,y=400,height=50)

    def return_login(self):
        self.root.destroy()

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
    main_fun()
