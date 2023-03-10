from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Get even numbers from input list
def get_even_numbers():
    input_str = input_entry.get()   # Get user input from the entry widget    
    input_list = list(map(int, input_str.split()))  # Convert the user input(string) into a list of integers

    # Check the input list and add even numbers to output list
    output_list = []
    for num in input_list:
        if num % 2 == 0:
            output_list.append(num)

    # Error Message     
    if len(input_list) == 0:    # Check if the input list is empty
        messagebox.showerror("Error", "Input list is empty!")

    elif len(input_list) == 1:    # Check if the input list has only 1 value
        messagebox.showerror("Error", "Input list must have at least two values!")

    elif len(output_list) == 0:   # Check if the input list has no even numbers
        messagebox.showwarning("Even numbers", "There are no even numbers in the input list!")

    else: # Show output using meesagebox
        messagebox.showinfo("Even numbers",output_list)
    
# Main window, its title and size
root = Tk()
root.title("Even number finder")
root.geometry("500x300")
label = Label(root, text="Find your even numbers!", font =("Fira Code", 20), fg = "black")
label.pack(pady = 20)

# Frame that holds the input label and entry widget
frame = Frame(root)
input_label = Label(frame, text="Enter a list of integers separated by spaces:", font=20)
input_entry = ttk.Entry(frame, font=15)
frame.pack(pady=20)
input_label.pack()
input_entry.pack(ipadx=20, pady=20)

# Button that uses "get_even_numbers" function
button = ttk.Button(frame, text="Get even numbers", command=get_even_numbers)
button.pack(ipadx=20, ipady=20)

root.mainloop()

