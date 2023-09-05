from tkinter import * 
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd 
from openpyxl import Workbook
import pathlib

DEFAULT_FONT_STYLE = ("Segoe", 14)
LARGE_FONT_STYLE = ("Segoe", 20, "bold")
background = "#5d2aff"
framebg = "#EDEDED"
framefg = "#5d2aff"

root=Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

file=pathlib.Path('Student_data.xlsx')
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"     
    sheet['D1']="Gender"
    sheet['E1']="DOB"
    sheet['F1']="Date of Registration"
    sheet['G1']="Religion"
    sheet['H1']="Skill"
    sheet['I1']="Father Name"
    sheet['J1']="Mother Name"
    sheet['K1']="Father's Occupation"
    sheet['L1']="Mother's Occupation"
    
    file.save(r'C:\Users\User\Desktop\test\Student_data.xlsx')

#Function of selection
def selection():
    value=radio.get()
    if value == 1:
        gender="Male"
        print(gender)
    elif value == 2:
        gender="Female"
        print(gender)
        

#HEADER / TOP FRAMES
Label(root,text="Email: qbdatiamzon@tip.edu.ph", width=10,height=3,bg="#ffc82a",anchor='e').pack(side=TOP,fill=X)
Label(root,text="STUDENT REGISTRATION", width=10,height=2,bg="#ffbd00",anchor='center',font=DEFAULT_FONT_STYLE, justify='center').pack(side=TOP,fill=X)

#SEARCH BOX
Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=2,font="arial 14").place(x=820,y=70)
imageicon3=PhotoImage(file=r'C:\Users\User\Desktop\test\glasskoto.png')
Srch=Button(root,text="Search",compound=LEFT, image=imageicon3, width=20, height=20, bg='#000000',font="arial 13 bold")
Srch.place(x=1060,y=66)

imageicon4=PhotoImage(file=r'')
update_button=Button(root,image=imageicon4,bg='#FFFFFF')
update_button.place(x=110,y=64)

#Registration and Date 
Label(root,text="Registration No:", font="arial 13", fg=framebg, bg=background).place(x=30,y=150)
Label(root,text="Date: ", font="arial 13", fg=framebg, bg=background).place(x=500,y=150)

Registration = StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font="arial 10")
reg_entry.place(x=160,y=150)

#registrationno
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial 10")
date_entry.place(x=550,y=150)

Date.set(d1)

#Student Details
obj=LabelFrame(root,text="Student's Details",font=20,bd=2,width=900,bg=framebg,fg=framefg, height=250,relief=GROOVE)
obj.place(x=30,y=200)

Label(obj,text="Full Name:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=50)
Label(obj,text="Date of Birth:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=100)
Label(obj,text="Gender:",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=150)

Label(obj,text="Class:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=50)
Label(obj,text="Religion:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=100)
Label(obj,text="Skills:",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=150)

Name = StringVar()
name_entry = Entry(obj, textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y=50)

radio = IntVar()
R1 = Radiobutton(obj,text="Male", variable=radio, value=1, bg=framebg,fg=framefg,command=selection)
R1.place(x=150,y=150)

R1 = Radiobutton(obj,text="Female", variable=radio, value=2, bg=framebg,fg=framefg,command=selection)
R1.place(x=200,y=150)

#Parents Details
obj=LabelFrame(root,text="Parent's Details",font=20,bd=2,width=900,bg=framebg,fg=framefg, height=220, relief=GROOVE)
obj.place(x=30,y=470)



root.mainloop()

