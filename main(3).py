from tkinter import *

from tkmacosx import Button

from tkinter.messagebox import showerror, showinfo, showwarning

table1=0

table2=0

table3=0

table4=0

table5=0

table6=0

def analysis():

    win1=Toplevel()

    win1.geometry("1920x1080")

    win1.config(bg="#d43131")

    label1=Label(win1, font=("Impact", 70), text="Analysis", bg="#d43131", fg="#31c71a")

    label1.place(relx=0.4, rely=0.01)

    label2=Label(win1, font=("Impact", 120), text=''