from tkinter import *

window = Tk()

window.title("Password Encryption")

def clicked():
    pass

lbl = Label(window, text="Enter a word for the password")
lbl.grid(column=0, row=0)

btn1 = Button(window, text="Enter", command=clicked)
btn1.grid(column=1, row=0)

txt = Entry(window,width=10)
txt.grid(column=2,row=0)

txt.focus()

password_hint=txt.get()


window.geometry('350x200')
window.mainloop()
