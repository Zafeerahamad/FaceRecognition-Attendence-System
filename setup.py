import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win64':
    base = "Win64GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\zafeer ahmad\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\zafeer ahmad\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Face_recognition",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'images','Training_images','database','Attendence_Report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By ZafeerAhamad",
    executables = executables
    )
