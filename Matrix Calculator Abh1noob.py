#Matrix Addition with tkinter

#importing Libraries
import tkinter as tk
from tkinter import *



#Functions
def addition():
    tk.Label(root,text=(int(a11.get()))+(int(b11.get())), bg="white", width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,text=(int(a12.get()))+(int(b12.get())), bg="white", width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,text=(int(a21.get()))+(int(b21.get())), bg="white", width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,text=(int(a22.get()))+(int(b22.get())), bg="white", width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,text= "+").place(y='24',x='108')   

def subtraction():
    tk.Label(root,text=(int(a11.get()))-(int(b11.get())), bg = "white", width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,text=(int(a12.get()))-(int(b12.get())), bg = "white", width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,text=(int(a21.get()))-(int(b21.get())), bg = "white", width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,text=(int(a22.get()))-(int(b22.get())), bg = "white", width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,text= "-").place(y='24',x='108')

def multiplication():
    pass

#Initialising tkinter
root = tk.Tk()
root.geometry("350x100")
root.title("Matrix Calculator")

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
a11 = tk.Entry(root, text = 'a11',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
a12 = tk.Entry(root, text = 'a12',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
a21 = tk.Entry(root, text = 'a21',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
a22 = tk.Entry(root, text = 'a22',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
b11 = tk.Entry(root, text = 'b11',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
b12 = tk.Entry(root, text = 'b12',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
b21 = tk.Entry(root, text = 'b21',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")
b22 = tk.Entry(root, text = 'b22',font=('calibre',10,'normal'),width=5,borderwidth=2, relief="groove")

#Placing of Components in x-y plane
a11.place(x=10, y = 10)
a12.place(x=60, y = 10)
a21.place(x=10, y = 40)
a22.place(x=60, y = 40)

b11.place(x=130, y = 10)
b12.place(x=180, y = 10)
b21.place(x=130, y = 40)
b22.place(x=180, y = 40)

tk.Label(root,text="=").place(y='24',x = '230')

#Operation Buttons
add=tk.Button(root,text='Addition',command=addition,width = 10).place(y='70',x='10')
sub=tk.Button(root,text='Subtraction',command=subtraction,width = 10).place(y='70',x='95')

root.mainloop()
