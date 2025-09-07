#WORKING WITH TKINTER
from tkinter import *

window = Tk()

window.title("Hello World")

window.geometry("750x500")
#entry widget

def submit():
    user_input = entry.get()
    print(f"{user_input}")
    entry.config(state=DISABLED )

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get()) - 1, END)

entry = Entry(window,
              font=("arial", 10, "bold"),
              relief=RAISED,
              bd=5,
              bg="blue",
              show="*"
              )
entry.insert(0, "")
entry.pack(side="left")

submit_button = Button(window, text="Submit",
                font=("arial", 20),
                fg="skyblue",
                command=submit)
submit_button.pack(side="right")

delete_button = Button(window, text="clear all",
                font=("arial", 20),
                fg="skyblue",
                command=delete)
delete_button.pack(side="right")

backspace_button = Button(window, text="backspace",
                font=("arial", 20),
                fg="skyblue",
                command=backspace)
backspace_button.pack(side="right")

window.mainloop()