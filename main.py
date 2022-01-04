from cryptography.fernet import Fernet
from pickle import *



def encrypt(password):

    key = Fernet.generate_key()
    global fernet 
    fernet = Fernet(key)
    encMessage = fernet.encrypt(password.encode())
    return encMessage

def decrypt(encrypted):
    decMessage = fernet.decrypt(encrypted).decode()
    return decMessage

with open('Password.bin','rb') as f:
    p=load(f)
    print('Encrypted password ',p)
    dec=decrypt(p)
    print('Decrypted password ',dec)
    

