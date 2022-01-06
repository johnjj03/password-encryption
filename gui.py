from tkinter import *
import pickle
from main import *

window = Tk()

window.title("Password Encryption")


def entry():
    global title
    title=Label(window,text="Enter a hint for the password")
    btn_sub = Button(window,text="Submit", command=submit)
    btn_quit = Button(window,text="Quit",command=window.destroy)
    inp=Entry(window)
    inp.focus()

    btn_sub.grid(row=2, column=0, sticky="ew", padx=5,pady=5)
    btn_quit.grid(row=3,column=0,sticky="ew",padx=5)
    inp.grid(row=1,column=0,sticky="ew",padx=5)
    title.grid(row=0,column=0,sticky="ew",padx=5)

    global password_hint
    password_hint=inp.get()

def submit():
    enc=encrypt(password_hint)
    with open('Password.bin','ab') as f:
        pickle.dump(enc,f)
    title.config(text="Successfully Encrypted")
    

entry()
window.mainloop()
