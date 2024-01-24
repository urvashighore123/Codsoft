#password generator
import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5']
symbols = ['!','@','#','$','%','&','*']

print("Welcome to password generator!")
num_letters=int(input("How many letters do you want in your password?\n"))
num_numbers=int(input("How many numbers do you want in your password?\n"))
num_symbols=int(input("How many symbols do you want in your password?\n"))

password_list=[]
for char in range(1,num_letters+1):
    random_choice1= rd.choice(letters)
    password_list += random_choice1
for num in range(1,num_numbers+1):
    random_choice2= rd.choice(numbers)
    password_list += random_choice2
for sym in range(1,num_symbols+1):
    random_choice3= rd.choice(symbols)
    password_list += random_choice3

rd.shuffle(password_list)

password=""
for char in password_list:
    password+=char

print("your password is :",password)
    
    
