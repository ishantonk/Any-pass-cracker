from random import *

user_pass = input("Enter Your Password : ")

# arroy of possible char...
upperCass = ['A', 'B', 'C', 'D', 'E', 'F'  'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

lowerCass = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' 'w', 'x', 'y', 'z',]

char = upperCass + lowerCass
guess = ""

# generate passwords untill we find the matched password.
while (guess != user_pass):
    guess = ""
    # generating random passwords...
    for letter in range(len(user_pass)):
        guess_letter = char[randint(0, 49)]
        guess = str(guess_letter) + str(guess)
    # print guessed passwords...
    print(guess)

# printing correct password
print("Your password is ", guess)