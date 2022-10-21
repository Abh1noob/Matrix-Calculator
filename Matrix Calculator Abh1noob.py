#Matrix Addition with tkinter

#importing Libraries
from sunau import AUDIO_FILE_ENCODING_ADPCM_G723_3
import tkinter as tk
from tkinter import *

#Standard Settings
bg_color="#00ABB3"
fg_color="#3C4048"
accent_color="3C4048"
my_font = ('calibre',10,'bold')

#Functions
def addition_2_2():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))+(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))+(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))+(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))+(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "+").place(y='24',x='108')

#placement to be done for addition_3_3
def addition_3_3():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))+(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))+(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a13.get()))+(int(b13.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))+(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))+(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a23.get()))+(int(b23.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a31.get()))+(int(b31.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a32.get()))+(int(b32.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a33.get()))+(int(b33.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "+").place(y='24',x='108')


def subtraction_2_2():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))-(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))-(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))-(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))-(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "-").place(y='24',x='108')

#placement to be done for subtraction_3_3
def subtraction_3_3():
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a11.get()))-(int(b11.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a12.get()))-(int(b12.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a13.get()))-(int(a13.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a21.get()))-(int(b21.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='250')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a22.get()))-(int(b22.get())),width = '5',borderwidth=2, relief="groove").place(y='40',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a23.get()))-(int(b23.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a31.get()))-(int(b31.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a32.get()))-(int(b32.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color,bg = bg_color,text=(int(a33.get()))-(int(b33.get())),width = '5',borderwidth=2, relief="groove").place(y='10',x='300')
    tk.Label(root,fg = fg_color, bg = bg_color,text= "-").place(y='24',x='108')

def multiplication_2_2():
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
a13 = tk.Variable
a21 = tk.Variable
a22 = tk.Variable
a23 = tk.Variable
a31 = tk.Variable
a32 = tk.Variable
a33 = tk.Variable

b11 = tk.Variable
b12 = tk.Variable
b13 = tk.Variable
b21 = tk.Variable
b22 = tk.Variable
b23 = tk.Variable
b31 = tk.Variable
b32 = tk.Variable
b33 = tk.Variable

#Taking Entries through tkinter, placement for new stuff to be done
a11 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a11',font=my_font,width=5,borderwidth=2, relief="groove")
a12 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a12',font=my_font,width=5,borderwidth=2, relief="groove")
a13 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a13',font=my_font,width=5,borderwidth=2, relief="groove")
a21 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a21',font=my_font,width=5,borderwidth=2, relief="groove")
a22 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a22',font=my_font,width=5,borderwidth=2, relief="groove")
a23 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a23',font=my_font,width=5,borderwidth=2, relief="groove")
a31 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a31',font=my_font,width=5,borderwidth=2, relief="groove")
a32 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a32',font=my_font,width=5,borderwidth=2, relief="groove") 
a33 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'a33',font=my_font,width=5,borderwidth=2, relief="groove") 

b11 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b11',font=my_font,width=5,borderwidth=2, relief="groove")
b12 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b12',font=my_font,width=5,borderwidth=2, relief="groove")
b13 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b13',font=my_font,width=5,borderwidth=2, relief="groove")
b21 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b21',font=my_font,width=5,borderwidth=2, relief="groove")
b22 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b22',font=my_font,width=5,borderwidth=2, relief="groove")
b23 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b23',font=my_font,width=5,borderwidth=2, relief="groove")
b31 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b31',font=my_font,width=5,borderwidth=2, relief="groove")
b32 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b32',font=my_font,width=5,borderwidth=2, relief="groove") 
b33 = tk.Entry(root,justify=CENTER,fg = fg_color, bg = bg_color, text = 'b33',font=my_font,width=5,borderwidth=2, relief="groove") 


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
