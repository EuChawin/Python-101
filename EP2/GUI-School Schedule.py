from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title("School Schedule")
GUI.geometry("500x500")

#####################################

L = Label(GUI, text="School Schedule",font=("Fira Code",30),fg="#892C18")
L.place(x=60,y=50)

#####################################

def mon():
    text = "Monday Schedule:\n\nMath - 9:00 AM\nHistory - 11:00 AM\nChemistry - 1:00 PM"
    messagebox.showinfo("Monday",text)
    
def tue():
    text = "Tuesday Schedule:\n\nBiology - 9:00 AM\nGeometry - 11:00 AM\nPE - 1:00 PM"
    messagebox.showinfo("Tuesday",text)

def wed():
    text = "Wednesday Schedule:\n\nArt - 9:00 AM\nEconomics - 11:00 AM\nMusic - 1:00 PM"
    messagebox.showinfo("Wednesday",text)

def thu():
    text = "Thursday Schedule:\n\nAlgebra - 9:00 AM\nPhysics - 11:00 AM\nStatistics - 1:00 PM"
    messagebox.showinfo("Thursday",text)

def fri():
    text = "Friday Schedule:\n\nGeography - 9:00 AM\nCalculus - 11:00 AM\nComputer - 1:00 PM"
    messagebox.showinfo("Friday",text)

#####################################

F1 = Frame(GUI)
F1.place(x=190,y=150)
B1 = ttk.Button(F1,text="Monday",command=mon)
B1.pack(ipadx=20,ipady=10)

F2 = Frame(GUI)
F2.place(x=190,y=200)
B2 = ttk.Button(F2,text="Tuesday",command=tue)
B2.pack(ipadx=20,ipady=10)

F3 = Frame(GUI)
F3.place(x=190,y=250)
B3 = ttk.Button(F3,text="Wednesday",command=wed)
B3.pack(ipadx=20,ipady=10)

F4 = Frame(GUI)
F4.place(x=190,y=300)
B4 = ttk.Button(F4,text="Thursday",command=thu)
B4.pack(ipadx=20,ipady=10)

F5 = Frame(GUI)
F5.place(x=190,y=350)
B5 = ttk.Button(F5,text="Friday",command=fri)
B5.pack(ipadx=20,ipady=10)

GUI.mainloop()
