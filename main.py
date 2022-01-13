from cryptography.fernet import Fernet
from tkinter import *
from random import choice 
from csv import writer
    

def encrypting():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('passwords.csv', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('passwords.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def generate():
    with open ('sample_sentences.txt','r') as f:
        l = f.read().split('.')
        word_list=[]
        s=inp.get()
        for i in l:
            for w in i.split():
                if w.lower()==s.lower():
                    word_list.append(i)
        out=choice(word_list)
        words=out.split(' ')
        for i in range(len(words)):
            if words[i].lower()==s.lower():
                if i==0:
                    out=s.lower()+words[i+1].lower()+words[i+2].lower()+words[i+3].lower()
                elif i==(len(words)-1):
                    out=words[i-3].lower()+words[i-2].lower()+words[i-1].lower()+s.lower()
                elif i==(len(words)-2):
                    out=words[i-2].lower()+words[i-1].lower()+s.lower()+words[i+1].lower()
                else:
                    out=words[i-1].lower()+s.lower()+words[i+1].lower()+words[i+2].lower()
        final=''
        for i in out:
            if i in [',',':','?',';',"'",'"']:
                pass
            else:
                final+=i
        return final

def submitted():
    popup = Tk()
    popup.title("Password Encryption")
    global title
    title=Label(popup,text=("Password is "+pw))
    btn_quit = Button(popup,text="Quit",command=end)
    title.grid(row=0,column=0,sticky="ew",padx=5)
    btn_quit.grid(row=1,column=0,sticky="ew",padx=5)
    popup.mainloop()

def submit():
    with open('passwords.csv','w') as p:
        w=writer(p)
        global pw
        pw=generate()
        w.writerow(pw)
    submitted()
    encrypting()

def end():
    window.destroy()


window = Tk()
window.title("Password Encryption")

title=Label(window,text="Enter a hint for the password")
btn_sub = Button(window,text="Submit", command=submit)
btn_quit = Button(window,text="Quit",command=window.destroy)
inp=Entry(window)
inp.focus()
subtext=Label(window,text="Works best with nouns")

title.grid(row=0,column=0,sticky="ew",padx=5)
subtext.grid(row=1, column=0, sticky="ew", padx=5)
inp.grid(row=2,column=0,sticky="ew",padx=5)
btn_sub.grid(row=3,column=0,sticky="ew",padx=5,pady=5)
btn_quit.grid(row=4,column=0,sticky="ew",padx=5)

window.mainloop()





    

   







    

