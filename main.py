from cryptography.fernet import Fernet

password=input("Enter your password ")

def encrypt(password):

    key = Fernet.generate_key()
    global fernet 
    fernet = Fernet(key)
    encMessage = fernet.encrypt(password.encode())
    return encMessage

def decrypt(encrypted):
    decMessage = fernet.decrypt(encrypted).decode()
    return decMessage



