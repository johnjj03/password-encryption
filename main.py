from cryptography.fernet import Fernet
from pickle import *

key = Fernet.generate_key()
fernet = Fernet(key)
with open('Password.bin','rb') as f:
    password=load(f)
    e=fernet.encrypt(password.encode())
    print('Encrypted password is ',e)
    print('Decrypted password is ',fernet.decrypt(e).decode())

    

   







    

