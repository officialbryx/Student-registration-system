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


#HEADER / TOP FRAMES
Label(root,text="Email: qbdatiamzon@tip.edu.ph", width=10,height=3,bg="#ffc82a",anchor='e').pack(side=TOP,fill=X)
Label(root,text="STUDENT REGISTRATION", width=10,height=2,bg="#ffbd00",anchor='center',font=DEFAULT_FONT_STYLE, justify='center').pack(side=TOP,fill=X)

#SEARCH BOX
Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=2,font="arial 14").place(x=820,y=70)
imageicon3=PhotoImage(file=r'C:\Users\User\Desktop\test\glasskoto.png')
Srch=Button(root,text="Search",compound=LEFT, image=imageicon3, width=20, height=20, bg='#000000',font="arial 13 bold")
Srch.place(x=1060,y=66)







root.mainloop()

