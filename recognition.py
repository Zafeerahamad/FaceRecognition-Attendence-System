import numpy as np
import cv2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
#from tensorflow.core.framework.types_pb2 import DataType
from student_detail import Student
import mysql.connector
from time import strftime
from datetime import datetime
import os
class Face_r:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Face Recognition",font=('times new roman',25,'bold'),bg='white',fg='green')
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

        '''img1=Image.open(r"D:\Projects\Attendence_system\images\images (14).jpg")
        img1=img1.resize((365,627),Image.ANTIALIAS)
        self.Photoimg1=ImageTk.PhotoImage(img1)
        f_label1=Label(self.root,image=self.Photoimg1)
        f_label1.place(x=900,y=41,width=465,height=720)'''

         #Button
        b1=Button(f_label,text="Click here to recognize your face",command=self.face_rec,cursor='hand2',font=('times new roman',20,'bold'),fg='white',bg='green')
        b1.place(x=0,y=620,height=50,width=1366)

        # face recognition algorithm
            ## ========Attendence ===============
    def mark_attendence(self,i,d,r,n):
        with open ("Attendence_Report/attendence_report.csv",'r+',newline='\n') as f:
            mydatalist=f.readlines()
            id_list=[]
            name_list=[]
            
            #print(DataType(i),d,r,n)
            for line in mydatalist:
                #print(line)
                entry=line.split((','))
                #print(entry)
                id_list.append(entry[0])
                #name_list.append(entry[2])

                #print(name_list)
            if ((str(i) not in id_list) and (n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{r},{n},{d},{dtstring},{d1},Present\n")
    def face_rec(self):
        def draw_boundry(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scalefactor,minNeighbors)

            cord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                #print(predict)
                #print(id)
                confidence= int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username='root',password='zafeer@786',database='attendence_system')
                my_cursor=conn.cursor()
                '''my_cursor.execute("select Name from student_details where StudentId="+str(id))
                n=my_cursor.fetchone()
                print(n)
                n="+".join(n)

                my_cursor.execute("select RollNo from student_details where StudentId="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student_details where StudentId="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                my_cursor.execute("select StudentId from student_details where StudentId="+str(id))
                i=my_cursor.fetchone()'''
                #print(i)

                if predict<55:
                    query1=f"select Name from student_details where StudentId={id}"
                    value=(id,)
                    my_cursor.execute(query1)
                    n=my_cursor.fetchone()
                    #print(n,value)
                    n="+".join(n)

                    query2=f"select RollNo from student_details where StudentId={id}"
                    value=(str(id),)
                    my_cursor.execute(query2)
                    r=my_cursor.fetchone()
                    r="+".join(r)

                    query3=f"select Dep from student_details where StudentId={id}"
                    value=(str(id),)
                    my_cursor.execute(query3)
                    d=my_cursor.fetchone()
                    d="+".join(d)
                    query4=f"select StudentId from student_details where StudentId={id}"
                    value=(str(id),)
                    my_cursor.execute(query4)
                    id=my_cursor.fetchone()
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                    cv2.putText(img,f"Confidence:{predict}",(x,y+h+5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),4)
                    self.mark_attendence(id,d,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),4)
                    cv2.putText(img,f"Confidence:{predict}",(x,y+h+5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),4)
                cord=[x,y,w,h]

            return cord




        def recognize(img,clf,faceCascade):
            cord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        #clf=cv2.face.createLBPHFaceRecognizer()
        clf.read("classifier.xml")
        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognizer",img)
            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
        video_cap.release()
        cv2.destroyAllWindows()








if __name__== "__main__":
    root=Tk()
    obj=Face_r(root)
    root.mainloop()