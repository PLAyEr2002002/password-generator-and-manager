from cryptography.fernet import Fernet
import random 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


# def load_key():
#     file = open("key.key", "rb")
#     key = file.read()
#     file.close()
#     return key


# key = load_key()
# fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:" , passw)
            #,
                #   fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        # f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        f.write(name + "|" +pwd + "\n")
        

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        
def create_random():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}") 
    confirmed= input("Would you like to save this? (yes/no)").lower()
    if confirmed =="yes":
        name1 = input('Account Name: ')
        
        with open('passwords.txt', 'a') as f:
        # f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
            f.write(name1 + "|" +password + "\n")
    else:
        print("ok no worries")
####################################
while True:
    mode = input(
        "Would you like to add a new password or view existing ones or create a new random password (view, add, create), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode== "create":
        create_random()
    else:
        print("Invalid mode.")
        continue