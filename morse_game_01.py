# IMPORT NECESSARY LIBRARIES

import nltk
from nltk.corpus import words
import random

# WORD LIST
nltk.download('words')
english_words = words.words()

# MORSE CODE DICTIONARY
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', 
    " ": "/"
}

# REVERSE DICTIONARY
reverse_dict = {v: k for k, v in morse_dict.items()}

# GENERATE RANDOM WORD WITH A GIVEN LENGTH
def generate_random_word(word_length):
    filtered_words = []
    for word in english_words:
        if len(word) == word_length:
            filtered_words.append(word.upper())
    if not filtered_words:
        return None
    return random.choice(filtered_words)

# MAIN GAME LOOP
score = 0  # SCORE COUNTER

while True:
    print("\n--- Morse Code Game ---")
    print(f"Your current score: {score}")
    print("1. Display English Word")
    print("2. Display Morse Code")
    print("3. Quit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        try:
            word_length = int(input("Enter the word length: "))
        except ValueError:
            print("Please enter a valid number for word length.")
            continue

        random_word = generate_random_word(word_length) # FUCTION CALL TO GENERATE RANDOM WORDS
        if random_word is None:
            print(f"No words found with length {word_length}.")
            continue

        print(f"\nEnglish Word: {random_word}")
        user_input = input("Enter the corresponding Morse code: ").strip()

        morse_message = " ".join(morse_dict[c] for c in random_word)

        # CHECKS FOR CORRECT ANSWER - IF USER INPUT AND MORSE CODE ARE SAME
        if user_input.replace(" ", "") == morse_message.replace(" ", ""):
            print("Correct answer!")
            print(f"Corresponding Morse Code is: {morse_message}")
            score += 1
        else:
            print(f"Wrong answer! The correct Morse code is: {morse_message}")

    elif choice == "2":
        try:
            word_length = int(input("Enter the word length: "))
        except ValueError:
            print("Please enter a valid number for word length.")
            continue

        random_word = generate_random_word(word_length) # FUCTION CALL TO GENERATE RANDOM WORDS
        if random_word is None:
            print(f"No words found with length {word_length}.")
            continue

        morse_message = " ".join(morse_dict[c] for c in random_word)

        print(f"\nMorse Code: {morse_message}")
        
        user_input = input("Enter the corresponding English text: ").replace(" ", "").upper()

        # CHECKS FOR CORRECT ANSWER - IF USER INPUT AND ENGLISH WORD ARE SAME
        if user_input == random_word:
            print("Correct answer!")
            print(f"Corresponding English word is: {random_word}")
            score += 1
        else:
            print(f"Wrong answer! The correct English word is: {random_word}")

    elif choice == "3":
        print(f"\nYour final score: {score}")
        print("Thank you for playing the Morse Code Game!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
