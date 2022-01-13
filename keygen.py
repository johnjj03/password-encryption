from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
#creates passwords.csv if not already created
with open('passwords.csv','w') as p:
    pass
