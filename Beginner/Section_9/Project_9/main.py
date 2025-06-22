import os
from art import logo

def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print("Welcome to the secret auction program.")

bids = []

while True:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    max = 0
    bids.append({
        "name": name,
        "bid": bid
    })
    
    if other_bidder == "yes":
        clear()
    else:
        for i in range(len(bids)):
            if max < bids[i]["bid"]:
                max = bids[i]["bid"]
        print(max)
        break