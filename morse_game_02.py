# IMPORT NECESSARY LIBRARIES

import streamlit as st
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

# GENERATE RANDOM WORD WITH A GIVEN LENGTH
def generate_random_word(word_length):
    filtered_words = []
    for word in english_words:
        if len(word) == word_length:
            filtered_words.append(word.upper())
    if not filtered_words:
        return None
    return random.choice(filtered_words)

# MAIN LAYOUT
st.title("Morse Code Game")

# INITIALIZE SESSION STATE VARIABLES
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'random_word' not in st.session_state:
    st.session_state.random_word = None
if 'display_text' not in st.session_state:
    st.session_state.display_text = ""
if 'display_morse' not in st.session_state:
    st.session_state.display_morse = ""
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# GAME OPTIONS
col1, col2 = st.columns([2, 1])
with col1:
    choice = st.radio("Choose an option:", ["Display English Word", "Display Morse Code"])

    word_length = st.number_input("Enter the word length:", min_value=1, max_value=15, value=5)

    # USER INPUT FIELD
    user_input = st.text_input("Enter the Answer:", value=st.session_state.user_input).strip()

with col2:
    st.write(f"**Your current score: {st.session_state.score}**")

# BUTTON TO GENERATE THE WORD, DEPENDING ON THE SELECTED OPTION
if st.button('Generate Word'):
    if choice == "Display English Word":
        st.session_state.random_word = generate_random_word(word_length)
        if st.session_state.random_word is None:
            st.session_state.display_text = f"No words found with length {word_length}."
            st.session_state.display_morse = ""
        else:
            st.session_state.display_text = f"Generated English word: {st.session_state.random_word}"
            st.session_state.display_morse = ""
    elif choice == "Display Morse Code":
        st.session_state.random_word = generate_random_word(word_length)
        if st.session_state.random_word is None:
            st.session_state.display_text = f"No words found with length {word_length}."
            st.session_state.display_morse = ""
        else:
            morse_message = " ".join(morse_dict[c] for c in st.session_state.random_word)
            st.session_state.display_text = f"Generated Morse code: {morse_message}"
            st.session_state.display_morse = morse_message

# DISPLAY THE GENERATED WORD OR MORSE CODE
if st.session_state.display_text:
    st.write(st.session_state.display_text)

# BUTTON TO SHOW THE HINT
if st.button("Hint"):
    if st.session_state.score > 0:  # DETECT POINTS ONLY IF THE SCORE IS > 0
        st.session_state.score -= 1
        st.image("Morse Code 02.jpg", caption="Morse Code Chart", use_column_width=True)
        st.warning("Hint used! -1 point.")
    else:
        st.image("Morse Code 02.jpg", caption="Morse Code Chart", use_column_width=True)
        st.info("Hint used! Score cannot go below zero.")

# BUTTON TO CHECK THE ANSWER
if st.button('Check Answer'):
    random_word = st.session_state.random_word
    if random_word is None:
        st.error("Please generate a word first!")
    else:
        if choice == "Display English Word":
            # CONVERT WORD TO MORSE CODE
            morse_message = " ".join(morse_dict[c] for c in random_word)
            # CHECK FOR CORRECT ANSWER
            if user_input.replace(" ", "") == morse_message.replace(" ", ""):
                st.success("Correct answer!")
                st.write(f"Corresponding Morse Code is: {morse_message}")
                st.session_state.score += 1
            else:
                st.error(f"Wrong answer! The correct Morse code is: {morse_message}")
        
        elif choice == "Display Morse Code":
            # CHECK FOR CORRECT ANSWER
            if user_input.upper().replace(" ", "") == random_word:
                st.success("Correct answer!")
                st.write(f"Corresponding English word is: {random_word}")
                st.session_state.score += 1
            else:
                st.error(f"Wrong answer! The correct English word is: {random_word}")
        
        # DISPLAY CURRENT SCORE
        st.write(f"**Your current score: {st.session_state.score}**")
