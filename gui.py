from tkinter import *
from pickle import *

window = Tk()

window.title("Password Encryption")


def entry():
    global title
    title=Label(window,text="Enter a hint for the password")
    global btn_sub
    btn_sub = Button(window,text="Submit", command=submit)
    btn_quit = Button(window,text="Quit",command=window.destroy)
    global inp
    inp=Entry(window)
    inp.focus()

    btn_sub.grid(row=2, column=0, sticky="ew", padx=5,pady=5)
    btn_quit.grid(row=3,column=0,sticky="ew",padx=5)
    inp.grid(row=1,column=0,sticky="ew",padx=5)
    title.grid(row=0,column=0,sticky="ew",padx=5)

    

def submit():
    password_hint=inp.get()
    with open('Password.bin','wb') as f:
        dump(password_hint,f)
    title.config(text="Successfully Encrypted")
    btn_sub['state']='disabled'
    

entry()
window.mainloop()
