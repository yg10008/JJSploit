import numpy as np
import time

print("🎩 Welcome to the Mystery Card Game!")

choose = int(input("Guess any number between 0-9: "))

cards = np.random.permutation(np.arange(0, 10))

position = int(input("🎴 Pick a card position from 1 to 10: "))

print("\nShuffling the cards...")
time.sleep(1)
print("Reading your fate...")
time.sleep(2)

picked_value = cards[position - 1]

if choose == picked_value:
    print("You have won the game! What a lucky guess!")
else:
    print(f"Oops! You lost. The card had number {picked_value}. Better luck next time!")

print("\nThanks for playing!")
