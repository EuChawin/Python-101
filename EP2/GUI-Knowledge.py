from tkinter import *
from tkinter import ttk #tk theme
from tkinter import messagebox

GUI = Tk()  
GUI.title('โปรแกรมบันทึกข้อมูล') #program title
GUI.geometry('500x500') #screen size


L1 = Label(GUI, text='โปรแกรมบันทึกความรู้', font=('Angsana New', 20), fg='blue')
L1.place(x=20, y=100)
b1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท?')
b1.pack(ipadx=20, ipady=20) #expand the size of the button

def Button2() : #button function
    text = 'ตอนนี้มีเงินในบัญชี 5 บาท'
    messagebox.showinfo('เงินในบัญชี', text)

fb1 = Frame(GUI)
fb1.place(x=100, y=200)
b2 = ttk.Button(fb1, text='เงินมีอยู่กี่บาท ?', command=Button2)
b2.pack(ipadx=20, ipady=20)


GUI.mainloop()
