import os
import time
import getpass

from pip._vendor.distlib.compat import raw_input
import sys

service = ""
email = ""
password = ""
p = -1
g = -1


def set_email(f):
    email1 = raw_input("Please enter your E-mail ID: ")

    time.sleep(1)

    email_confirm = raw_input('Please confirm your E-mail ID: ')

    if (email1 == email_confirm):

        print("\n**** E-mail ID Confirmed ****\n")
        time.sleep(2)
        f.write(email1 + " ")
        return 1

    else:

        print("\n!!!! E-mail did not match. Please try again !!!!\n")
        return 0


def set_password(f):
    password1 = getpass.getpass(
        'Please enter your Password (Nothing will appear on-screen when you type, for privacy reasons) : ')

    time.sleep(1)

    password_confirm = getpass.getpass('Please confirm your Password: ')

    if (password1 == password_confirm):

        print("\n**** Password Confirmed ****\n")
        time.sleep(2)
        f.write(password1 + "\n")
        return 1

    else:

        print("\n!!!! Password did not match. Please try again !!!!\n")
        return 0


def add():
    print("\n**** Add your credentials ****")
    f = open("credentials.txt", "a+")
    time.sleep(2)
    email_service()
    return_code = set_email(f)
    while (return_code != 1):
        return_code = set_email(f)

    return_code1 = set_password(f)
    while (return_code1 != 1):
        return_code1 = set_password(f)
    f.close()
    print("\n**** Credentials added successfully !! ****")
    time.sleep(2)


def update():
    global g
    input1 = raw_input("\n**** type in the service you want to update the credentials for ****\n")
    time.sleep(1)
    if os.path.isfile("credentials.txt"):
        f = open("credentials.txt", "r+")
        time.sleep(1)
        response = input1
        Lines = f.readlines()
        for line in Lines:
            g = line.strip().find(response)
            if g != -1:
                print("\n**** Updating the service credentials ****\n")
                del line
                add()
        if g == -1:
            print("\n**** no credentials exist ****\n")
            add()
            login()
    else:
        print("\n**** no credentials exist ****\n")
        add()
        login()


def email_service():
    print("**** Please write the service ****\n")
    response = raw_input("Enter Response : ")
    print("\n**** You have selected " + str(response) + "!! ****\n")
    f = open("credentials.txt", "w+")
    f.write(str(response) + " ")
    f.close()


def login():
    global service
    global email
    global password
    global p
    if os.path.isfile("credentials.txt"):
        f = open("credentials.txt", "r+")
        response = sys.argv[1]
        Lines = f.readlines()
        for line in Lines:
            p = line.strip().find(response)
            if p != -1:
                print("\n**** Welcome to Auto-Login! Your credentials are already set ****\n")
                service = line.split()[0]
                email = line.split()[1]
                password = line.split()[2].strip()
        if p == -1:
            add()
            login()
    else:
        add()
        login()

    run_string = "python3.8 " + str(service) + ".py " + service + " " + email + " " + "'" + password + "'"
    os.system(run_string)


def main():
    if sys.argv[1] == "update":
        update()
    else:
        login()


main()
