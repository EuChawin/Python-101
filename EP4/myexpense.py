from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

###################################################################

# Function to write expenses data to CSV file
def writecsv(data):
    with open('expense.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(data)

# Function to read expenses data from CSV file
def readcsv():
    with open('expense.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data

# Function to display expenses data in Listbox
def display():
    expenses = readcsv()
    listbox.delete(0, END)
    for expense in expenses:
        listbox.insert(END, expense)

# Function to handle button click event
def addexpense():
    # Get user input
    item = item_var.get()
    cost = cost_var.get()

    # Check if it's valid
    if not item or not cost:
        messagebox.showerror('Error','Please enter both item and cost')
        return
    
    try:
        cost = float(cost)
    except ValueError:
        messagebox.showerror('Error','Invalid cost')
        return
    
    # Write data to CSV
    t = datetime.now().strftime('%y/%m/%d %H:%M:%S')
    data = [t,item,cost]
    writecsv(data)

    item_var.set('')
    cost_var.set('')

    # Show success message popup
    messagebox.showinfo('Success','Expense added successfully')

    display()

###################################################################

window = Tk()
window.title('Expense Recording Program')
window.geometry('800x800')

L1 = Label(window,text='My Expense',font=('Fira Code',50),fg='black')
L1.pack(pady=30)

###################################################################

LF1 = ttk.LabelFrame(window,text='Please enter both item and cost')
LF1.pack()

item_var = StringVar() # Special function used with messages in gui
cost_var = StringVar()

item_entry = ttk.Entry(LF1,textvariable=item_var,font=('Fira Code',20))
item_entry.pack(pady=10)

cost_entry = ttk.Entry(LF1,textvariable=cost_var,font=('Fira Code',20))
cost_entry.pack(pady=20)

button = ttk.Button(window,text='Save',command=addexpense)
button.pack()

###################################################################

listbox = Listbox(window,font=('Fira Code',16))
listbox.pack(ipadx=250,ipady=150)

expenses = readcsv()
for expense in expenses:
    listbox.insert(END, expense)

window.mainloop()
