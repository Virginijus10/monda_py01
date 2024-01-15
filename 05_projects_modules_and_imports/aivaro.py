
#passwords maneger su encryptinimu. Jei kam bus idomu
#ir su visais paaiskinimais
from cryptography.fernet import Fernet # pip install cryptography

'''#create a key to encrypt the passwords
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file: #wb means write binary 
        key_file.write(key)

write_key()'''  #this is for testing purposes, to create a key file and then use it to encrypt passwords

def load_key(): #this is to load the key from the key file
    file = open('key.key', 'rb') #rb means read binary
    key = file.read() #read the key file
    file.close() #close the file
    return key #return the key


master_pwd = input("Whats is the master password? ") #this is to get the master password
key = load_key() + master_pwd.encode() #this is to get the key from the key file and then add the master password to it
fer = Fernet(key)#this is to create the fernet object

def view():
    with open('passwords.txt', 'r') as f: # r means read
        for line in f.readlines(): #read the file line by line
            data = line.rstrip() 
            user, passw = data.split(":")
            '''print("User: ", user, "| Password: ", fer.decrypt(passw.encode()))''' #this is to view decrypted passwords
            print(f"User: {user}: Encrypted password: {passw}") #this is to view encrypted passwords

def add():
    name = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f: # a means append, w means write, r means read
        f.write(name + ":" + fer.encrypt(pwd.encode()).decode() + "\n") #this is to add the encrypted password to the file


while True:

    mode = input("Would you like to add a new password or view your existing passwords ( view / add ), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()    
    else:
        print("Invalid input")
        continue
