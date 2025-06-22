from art import logo, vs
import random
from game_data import data
import os

print(logo)
score = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    data_1 = random.choice(data)
    data_2 = random.choice(data)
    compareA = print(f"Compare A: {data_1['name']}, a {data_1["description"]}, from {data_1["country"]}")
    
    print(vs)
    compareB = print(f"Compare A: {data_2['name']}, a {data_2["description"]}, from {data_2["country"]}")
    
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if data_1["follower_count"] > data_2["follower_count"] and answer == 'A':
        score += 1
        clear()
        print(f"You 're right! Current score: {score}")
    elif data_1["follower_count"] < data_2["follower_count"] and answer == 'B':
        score += 1
        clear()
        print(f"You 're right! Current score: {score}")
    else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        break