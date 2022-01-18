# Password Generator and Encryptor

Passwords are an integral part in the world of Computer Science.  
This project aims to generate and encrypt passwords for the user using Python.

## Getting Started

### Prerequisites

- The program will run without any issues on any computer, but for a good experience, it is recommended to use a system with atleast 4 GB memory, and atleast 2 CPU cores.
- You can use git to clone the repository, or you can download the zip file.

### Basic Setup

- First, install the packages required by running

```
pip install -r requirements.txt
```

- Generate the key and create phone number csv file running

```
python3 keygen.py
```

- Create a free Twilio account and get your phone number ,Account SID and Authentication Token from Twilio

- Create a .env file and add your information following this naming scheme:

```
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
tno='+12345678901'
```

- If you don't want to use the sms feature, just leave the phone number field blank while entering the password hint.

- Start the app with the following command :

```
python3 main.py
```

- Decrypt and view the password by running :

```
python3 show_password.py
```

### Technologies Used

- All the visuals were built solely using ![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) 
- [**Tkinter**](https://docs.python.org/3/library/tkinter.html),[**Cryptography**](https://pypi.org/project/cryptography/) and [**Twilio**](https://pypi.org/project/twilio/) were the libraries used to create the project.

### Main Contributors

 - [John J J](https://github.com/jxhn_jj/)
