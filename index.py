import random
import string
# import math

def main():
    print("Welcome to the random password generator") 
    getPasswordInformation()

def getPasswordInformation():
    print("What are you using this password for?")
    whats_password_for = input();
    print("Lets now create your password for: " + whats_password_for)

    while(True):
        print("How long do you want you password to be(Min length is 8): ")
        password_length = int(input())

        if(password_length >= 8):
            createPassword(password_length, whats_password_for)
            break
        else: 
            print("Password has to be at least 8 long")
            continue


def createPassword(password_length, whats_password_for):
    # uppercase_letters = 

def savePassword():
    print("Hello")

def savePassword():
    print("Hello")


main()
# getPasswordInformation()