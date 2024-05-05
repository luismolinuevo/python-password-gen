import random
import string
# import math

def main():
    print("Welcome to the random password generator") ;
    getPasswordInformation();

def getPasswordInformation():
    print("What are you using this password for?");
    whats_password_for = input();
    print("Lets now create your password for: " + whats_password_for);

    while(True):
        print("How long do you want you password to be(Min length is 8): ");
        password_length = int(input());

        if(password_length >= 8):
            createPassword(password_length, whats_password_for);
            break;
        else: 
            print("Password has to be at least 8 long");
            continue;


def createPassword(password_length, whats_password_for):
    password = "";
    what_to_add = password_length - 8;

    # All the chars needed to create a random password
    uppercase_letters = string.ascii_uppercase;
    lowercase_letters = string.ascii_lowercase;
    numbers = string.digits;
    symbols = string.punctuation;

    all_chars = uppercase_letters + lowercase_letters + numbers + symbols;
    print(all_chars)

    # Create the basic 8 long password(2 lowercase and uppercase letters, 2 numbers, 2 symbols)
    for i in range(2):
        password = password + random.choice(uppercase_letters);
        password = password + random.choice(lowercase_letters);
        password = password + random.choice(numbers);
        password = password + random.choice(symbols);
    print(password)

    # Create the rest of the password(8 + n)
    for i in range(what_to_add):
        password = password + random.choice(all_chars)
    
    savePassword(password, whats_password_for)



def savePassword(password, whats_password_for):
    print("Hello");

def savePassword():
    print("Hello");


main()
# getPasswordInformation()