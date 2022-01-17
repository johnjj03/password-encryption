from cryptography.fernet import Fernet
from tkinter import *
from random import choice 
from csv import reader, writer
from os import getenv
from twilio.rest import Client
from dotenv import load_dotenv
    
load_dotenv()

def sendSMS(pwd,pno):
    print('SMS sent!!')
    account_sid = getenv('account_sid')
    auth_token = getenv('auth_token')
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=('Your password is '+pwd),from_=getenv('tno'),
    to=pno)

def encrypting():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('passwords.csv', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('passwords.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def submitted():
    global popup
    popup = Tk()
    popup.title("Password Encryption")
    global title
    title=Label(popup,text=("Password is "+pw))
    btn_quit = Button(popup,text="Quit",command=end)
    title.grid(row=0,column=0,sticky="ew",padx=5)
    btn_quit.grid(row=1,column=0,sticky="ew",padx=5)
    popup.mainloop()

def invinp():
    global popup
    popup = Tk()
    popup.title("Password Encryption")
    global title
    title=Label(popup,text=("Invalid Input"))
    btn_quit = Button(popup,text="Quit",command=end)
    title.grid(row=0,column=0,sticky="ew",padx=5)
    btn_quit.grid(row=1,column=0,sticky="ew",padx=5)
    popup.mainloop()

def nopwd():
    global popup
    popup = Tk()
    popup.title("Password Encryption")
    global title
    title=Label(popup,text=("Unable to generate password, try a different word"))
    btn_quit = Button(popup,text="Quit",command=end)
    title.grid(row=0,column=0,sticky="ew",padx=5)
    btn_quit.grid(row=1,column=0,sticky="ew",padx=5)
    popup.mainloop() 

def nomore():
    global popup
    popup = Tk()
    popup.title("Password Encryption")
    global title
    title=Label(popup,text=("Max passwords generated"))
    btn_quit = Button(popup,text="Quit",command=end)
    title.grid(row=0,column=0,sticky="ew",padx=5)
    btn_quit.grid(row=1,column=0,sticky="ew",padx=5)
    popup.mainloop() 

def generate():
    s=inp.get()
    if s.isnumeric() or not(s and s.strip()):
        return 'Invalid Input'
    else:
        with open ('sample_sentences.txt','r') as f:
            l = f.read().split('.')
            word_list=[]
            for i in l:
                for w in i.split():
                    if w.lower()==s.lower():
                        word_list.append(i)
            if len(word_list)==0:
                return 'No Password'
            else:
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
                    if i in [',',':','?',';',"'",'"','-']:
                        pass
                    else:
                        final+=i
                return final


def submit():
    pn=pno.get()
    global pw
    pw=generate()
    if pw=='Invalid Input':
        invinp()
    elif pw=='No Password':
        nopwd()
    else:
        with open('passwords.csv','w') as p:
            w=writer(p)
            w.writerow(pw)
        submitted()
        encrypting()
        if not(pn and pn.strip()):
            pass
        else:
            sendSMS(pw,pn)

def checkpno():
    submit()


def end():
    popup.destroy()
    window.destroy()


window = Tk()
window.title("Password Encryption")


title=Label(window,text="Enter a hint for the password")
subtext=Label(window,text="Enter phone number to send password to with +91")
smsinfo=Label(window,text="To not use sms, leave phone number blank")
btn_sub = Button(window,text="Submit", command=checkpno)
btn_quit = Button(window,text="Quit",command=window.destroy)
inp=Entry(window)
inp.focus()
pno=Entry(window)


title.grid(row=0,column=0,sticky="ew",padx=5)
inp.grid(row=1,column=0,sticky="ew",padx=5)
subtext.grid(row=2, column=0, sticky="ew",padx=5)
pno.grid(row=3,column=0,sticky='ew',padx=5)
btn_sub.grid(row=4,column=0,sticky="ew",padx=5,pady=5)
btn_quit.grid(row=5,column=0,sticky="ew",padx=5)
smsinfo.grid(row=6,column=0,sticky="ew",padx=5)

window.mainloop()