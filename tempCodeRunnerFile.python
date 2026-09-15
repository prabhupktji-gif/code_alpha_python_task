import random

# Some words for the game
words = ["python", "computer", "elephant", "program", "internet"]

# Pick one word randomly
word = random.choice(words)

# Show blanks instead of the actual word
display = ["_"] * len(word)

# Store the letters the player has already entered
guessed = []

wrong = 0
chances = 6

print(" HANGMAN GAME ")
print("Try to guess the word!")
print("You have", chances, "wrong guesses available.")

while wrong < chances and "_" in display:

    print("\nWord:", " ".join(display))
    print("Letters guessed:", " ".join(guessed))
    print("Chances left:", chances - wrong)

    letter = input("Enter a letter: ").lower()

    # Check if the input is valid
    if len(letter) != 1 or not letter.isalpha():
        print("Enter only one letter.")
        continue

    # Check if the letter was already entered
    if letter in guessed:
        print("You already entered this letter.")
        continue

    guessed.append(letter)

    # Check whether the letter is in the word
    if letter in word:
        print("Good guess!")

        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter

    else:
        wrong += 1
        print("Oops! Wrong letter.")

# Check the result
if "_" not in display:
    print("\nYou won!!!!")
    print("The word was:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)