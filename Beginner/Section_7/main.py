import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
lives = 6
display = ["_" for i in range(len(chosen_word))]

print(chosen_word)

while ("_" in display):
    guess_word = input("Guess a word: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess_word:
            display[i] = guess_word
            
    if guess_word not in chosen_word:
        lives -= 1
    
    print(hangman_art.stages[lives])
    print(display)
            
    if lives == 0:
        print("You Lose")
        break
    
    if "_" not in display:
        print("You Win")
        break