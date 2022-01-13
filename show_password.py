from cryptography.fernet import Fernet
from tkinter import *

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
    fernet = Fernet(key)
    with open('passwords.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted).decode()
out=''
for i in decrypted:
    if i in [',','\r','\n',' ']:
        pass
    else:
        out+=i
root=Tk()
root.title("Password Encryption")
global title
title=Label(root,text=("Password is: "+out))
btn_quit = Button(root,text="Quit",command=root.destroy)
title.grid(row=0,column=0,sticky="ew")
btn_quit.grid(row=1,column=0,sticky="ew")
root.mainloop()
