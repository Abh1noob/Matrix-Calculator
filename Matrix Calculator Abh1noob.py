#Matrix Addition with tkinter

#importing Libraries
import tkinter as tk
from tkinter import *

#Standard Settings
bg_color="#00ABB3"
fg_color="#3C4048"
accent_color="3C4048"
my_font = ('calibre',10,'bold')

#Functions
def addition():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))+(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))+(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))+(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))+(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "+").place(y='24',x='108')   

def subtraction():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))-(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))-(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))-(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))-(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "-").place(y='24',x='108')

def multiplication():
    tk.Label(root,fg = fg_color,bg = bg_color, text=(((int(a11.get()))*(int(b11.get())))+((int(a12.get()))*(int(b21.get())))),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color, text=(((int(a11.get()))*(int(b12.get())))+((int(a12.get()))*(int(b22.get())))),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color, text=(((int(a21.get()))*(int(b11.get())))+((int(a22.get()))*(int(b21.get())))),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color, text=(((int(a21.get()))*(int(b12.get())))+((int(a22.get()))*(int(b22.get())))),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color, text= "x").place(y='24',x='108')

#Initialising tkinter
root = tk.Tk()
root.geometry("350x100")
root.title("Matrix Calculator")
root['bg']=bg_color

#Declaring entries to be variable
a11 = tk.Variable
a12 = tk.Variable
a21 = tk.Variable
a22 = tk.Variable

b11 = tk.Variable
b12 = tk.Variable
b21 = tk.Variable
b22 = tk.Variable

#Taking Entries through tkinter
a11 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a11',font=my_font,width=5,borderwidth=2, relief="groove")
a12 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a12',font=my_font,width=5,borderwidth=2, relief="groove")
a21 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a21',font=my_font,width=5,borderwidth=2, relief="groove")
a22 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a22',font=my_font,width=5,borderwidth=2, relief="groove")
b11 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b11',font=my_font,width=5,borderwidth=2, relief="groove")
b12 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b12',font=my_font,width=5,borderwidth=2, relief="groove")
b21 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b21',font=my_font,width=5,borderwidth=2, relief="groove")
b22 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b22',font=my_font,width=5,borderwidth=2, relief="groove")

#Placing of Components in x-y plane
a11.place(x=10, y = 10)
a12.place(x=60, y = 10)
a21.place(x=10, y = 40)
a22.place(x=60, y = 40)

b11.place(x=130, y = 10)
b12.place(x=180, y = 10)
b21.place(x=130, y = 40)
b22.place(x=180, y = 40)

tk.Label(root,fg = fg_color, bg = bg_color,text="=").place(y='24',x = '230')

#Operation Buttons
add=tk.Button(root,bg = "#3C4048", fg = "#B2B2B2", text='Addition',command=addition,width = 10).place(y='70',x='10')
sub=tk.Button(root,bg = "#3C4048", fg = "#B2B2B2", text='Subtraction',command=subtraction,width = 10).place(y='70',x='95')
mul=tk.Button(root,bg = "#3C4048", fg = "#B2B2B2", text='Multiplication',command=multiplication,width = 10).place(y='70',x='185')

root.mainloop()
