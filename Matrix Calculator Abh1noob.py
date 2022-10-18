#Matrix Addition wit(int(h t.get()))kr rot

import tkinter as tk
from tkinter import *

def calculate():
    tk.Label(root,text=(int(a11.get()))+(int(b11.get()))).place(y='5',x='235')
    tk.Label(root,text=(int(a12.get()))+(int(b12.get()))).place(y='5',x='275')
    tk.Label(root,text=(int(a21.get()))+(int(b21.get()))).place(y='30',x='235')
    tk.Label(root,text=(int(a22.get()))+(int(b22.get()))).place(y='30',x='275')

root = tk.Tk()
root.geometry("400x100")
root.title("Matrix Calculator")

a11 = tk.Variable
a12 = tk.Variable
a21 = tk.Variable
a22 = tk.Variable

b11 = tk.Variable
b12 = tk.Variable
b21 = tk.Variable
b22 = tk.Variable

a11 = tk.Entry(root, text = 'a11',font=('calibre',10,'normal'),width=5)
a12 = tk.Entry(root, text = 'a12',font=('calibre',10,'normal'),width=5)
a21 = tk.Entry(root, text = 'a21',font=('calibre',10,'normal'),width=5)
a22 = tk.Entry(root, text = 'a22',font=('calibre',10,'normal'),width=5)
b11 = tk.Entry(root, text = 'b11',font=('calibre',10,'normal'),width=5)
b12 = tk.Entry(root, text = 'b12',font=('calibre',10,'normal'),width=5)
b21 = tk.Entry(root, text = 'b21',font=('calibre',10,'normal'),width=5)
b22 = tk.Entry(root, text = 'b22',font=('calibre',10,'normal'),width=5)

a11.place(x=5, y = 5)
a12.place(x=50, y = 5)
a21.place(x=5, y = 30)
a22.place(x=50, y = 30)

b11.place(x=120, y = 5)
b12.place(x=165, y = 5)
b21.place(x=120, y = 30)
b22.place(x=165, y = 30)

tk.Label(root,text="+").place(y='13',x='98')

tk.Label(root,text ="=").place(y='13',x = '213')

cal=tk.Button(root,text='Calculate',command=calculate).place(y='60',x='150')

root.mainloop()
