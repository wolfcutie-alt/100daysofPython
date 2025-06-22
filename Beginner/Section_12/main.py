#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode)

from art import logo
import random

def get_number():
    return random.randint(0, 100)
print(logo)

play_mode = input("Select play mode: 'Easy' or 'Hard' ").lower()

if play_mode == "easy":
    turn = 10
elif play_mode == "hard":
    turn = 5
    
while turn > 0:
    guess_num = int(input("Enter your number: "))
    
    if guess_num > get_number():
        turn -= 1
        print(f"Too High. Remaining {turn} turns.")
        
    elif guess_num < get_number():
        turn -= 1
        print(f"Too Low. Remaining {turn} turns.")
        
    else:
        print("Correct answer. You Win!!!")
        break
        
if turn == 0:
    print("You Lose")