from tkinter import *
from tkinter import filedialog, messagebox

# Create the main window
root = Tk()
root.title("Notepad")
root.geometry("800x600")

# Create a Text widget for the notepad
text_area = Text(root, font=("Helvetica", 14), undo=True)
text_area.pack(expand=True, fill='both')

# Functions for File Operations
def new_file():
    text_area.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"),
                                                      ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, END)
            text_area.insert(END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))

def exit_app():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        root.destroy()

# Functions for Edit Menu
def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

# Function for Help Menu
def about():
    messagebox.showinfo("About", "Simple Notepad using Tkinter\nVersion 1.0")

# Creating the Menu Bar
menu_bar = Menu(root)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help Menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Attach the menu to the window
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
