from cryptography.fernet import Fernet


message = "hello geeks"

def encrypt():

    key = Fernet.generate_key()
    global fernet 
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage

def decrypt(encrypted):
    decMessage = fernet.decrypt(encrypted).decode()
    return decMessage



