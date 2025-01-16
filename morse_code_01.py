# IMPORT THE NECESSARY LIBRARIES
 
from playsound import playsound
import time
import pyttsx3

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

# TEXT-TO-SPEECH INITIALIZATION
text_speech = pyttsx3.init()

def play_sound(message):
    for c in message:
        if c == '.':
            playsound('short.wav')
            time.sleep(0.1)
        elif c == '-':
            playsound('long.wav')
            time.sleep(0.3)
        elif c == '/' or c == ' ':
            time.sleep(0.5)

# MAIN LOOP
while True:
    print("\n1. English to Morse Code")
    print("2. Morse Code to English")
    print("3. Exit")
    choice = input("Enter your option here: ")
    
    # CONVERT ENGLISH TO MORSE
    if choice == '1':
        message = input('Enter your text message here: ')
        try:
            morse_message = ' '.join(morse_dict[c] for c in message.upper())
            print(f"Morse Code: {morse_message}")
            play_sound(morse_message)
        except KeyError:
            print("Invalid input! Please use only letters, numbers, and spaces.")

    # CONVERT MORSE TO ENGLISH
    elif choice == '2':
        message = input("Enter Morse Code here: ")
        try:
            english_message = ''.join(reverse_dict[c] for c in message.split(' '))
            print(f"English Text: {english_message}")
            text_speech.say(english_message)
            text_speech.runAndWait()
        except KeyError:
            print("Invalid Morse code input! Please check your Morse code and try again.")
    
    #EXIT
    elif choice == '3':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid option! Please select 1, 2, or 3.")
