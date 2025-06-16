#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_easy = ""
for _ in range(nr_letters):
    password_easy += letters[random.randrange(len(letters))]
    
for _ in range(nr_symbols):
    password_easy += symbols[random.randrange(len(symbols))]
    
for _ in range(nr_numbers):
    password_easy += numbers[random.randrange(len(numbers))]
    
print(password_easy)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_hard = []
password = ""

for _ in range(nr_letters):
    password_hard += letters[random.randrange(len(letters))]
    
for _ in range(nr_symbols):
    password_hard += symbols[random.randrange(len(symbols))]
    
for _ in range(nr_numbers):
    password_hard += numbers[random.randrange(len(numbers))]
    
print(password_hard)

random.shuffle(password_hard)

for word in (password_hard):
    password += word
    
print(password)