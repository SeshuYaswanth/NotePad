from tkinter import *
import os
from tkinter.messagebox import *
from tkinter import filedialog
global open_status_name
open_status_name = False
global selected
selected = False
root = Tk()
root.title("Notepad")
root.geometry("1900x990+3+3")


def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="C:/texts/", title="Select a file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
    name = text_file
    status_bar.config(text=f'{name}        ')
    name.replace("C:/texts/", "")
    root.title(f'{name} - Notepad')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()


def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Notepad")
    status_bar.config(text="New File        ")


def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/texts/", title="Save File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'{name}      ')
        name = name.replace("C:/texts/", "")
        root.title(f'{name} - Notepad')

        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))

        text_file.close()


def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))

        text_file.close()

        status_bar.config(text=f'Saved: {open_status_name}      ')
    else:
        save_as()


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


def view_help():
    root1 = Tk()
    root1.title("Help desk")
    root1.geometry("600x100+1300+58")
    Label(root1, text="Contact me@ seshuyaswanth2409@gmail.com",  font=("Courier", 15, "bold")).pack()
    root1.mainloop()


def about():
    root2 = Tk()
    root2.title("About Notepad")
    root2.geometry("600x100+1300+58")
    Label(root2, text="This is my mini-project.....", font=("Courier", 20, "bold")).pack()
    root2.mainloop()


my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(my_frame, width=245, height=60)
my_text.pack()

text_scroll.config(command=my_text.yview)

my_menu = Menu(root)


root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New           Ctrl+N", command=new_file)
file_menu.add_command(label="Open          Ctrl+O", command=open_file)
file_menu.add_command(label="Save          Ctrl+S", command=save_file)
file_menu.add_command(label="Save As       Ctrl+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo           Ctrl+Z", command=open_file)
edit_menu.add_command(label="Cut            Ctrl+X", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy           Ctrl+C", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste          Ctrl+P", command=lambda: paste_text(False))
edit_menu.add_command(label="Delete         del")

help_review = Menu(root)
my_menu.add_cascade(label="Help", menu=help_review)
help_review.add_command(label="View Help", command=view_help)
help_review.add_command(label="Send Feedback", command=view_help)
help_review.add_command(label="About Notepad", command=about)

status_bar = Label(root, text="Ready    ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)
root.mainloop()
