from tkinter import *
from tkinter import ttk #tk theme
from tkinter import messagebox

GUI = Tk()  
GUI.title('โปรแกรมบันทึกข้อมูล') #program title
GUI.geometry('500x400') #screen size

L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 20), fg='blue')
L1.place(x=170, y=50)
##################################################
def Button1() : #button function
    text = 'ตอนนี้มีเงินในบัญชี 5 บาท'
    messagebox.showinfo('เงินในบัญชี',text)
fb1 = Frame(GUI)
fb1.place(x=200, y=150)
b1 = ttk.Button(fb1, text='เงินมีอยู่กี่บาท?', command=Button1)
b1.pack(ipadx=20, ipady=20)
##################################################
def Button2() : #button function
    text = 'เรียน Python 101'
    messagebox.showinfo('วิชาที่เรียน',text)
fb2 = Frame(GUI)
fb2.place(x=200, y=250)
b2 = ttk.Button(fb2, text='เรียนวิชาอะไร?', command=Button2)
b2.pack(ipadx=20, ipady=20)
##################################################

GUI.mainloop()
