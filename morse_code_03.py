import streamlit as st
import time
from playsound import playsound
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

# INITIALIZE SESSION STATE VARIABLES
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "output_text" not in st.session_state:
    st.session_state.output_text = ""
if "morse_code" not in st.session_state:
    st.session_state.morse_code = ""

# TITLE
st.title("Morse Code Converter")

# INPUT AREA
st.header("Input Text")
st.session_state.input_text = st.text_area(
    "Enter your text below:", 
    value=st.session_state.input_text, 
    height=100,
    key="input_area",
)

# CONVERSION TYPE AND CONVERSION BUTTON
st.header("Convert")
col1, col2 = st.columns([2, 3])

with col1:
    conversion_type = st.radio(
        "Select Conversion Type:",
        ["English to Morse Code", "Morse Code to English"],
        horizontal=True,
    )

with col2:
    if st.button("Convert"):
        if conversion_type == "English to Morse Code":
            try:
                # CONVERT ENGLISH TO MORSE
                st.session_state.output_text = ' '.join(
                    morse_dict[char] for char in st.session_state.input_text.upper().strip() if char in morse_dict
                )
                st.session_state.morse_code = st.session_state.output_text
            except KeyError:
                st.error("Invalid character found in input. Only letters, numbers, and spaces are allowed.")
        elif conversion_type == "Morse Code to English":
            try:
                # CONVERT MORSE TO ENGLISH
                st.session_state.output_text = ''.join(
                    reverse_dict[code] for code in st.session_state.input_text.strip().split(' ') if code in reverse_dict
                )
                st.session_state.morse_code = ""
            except KeyError:
                st.error("Invalid Morse code found in input.")

# OUTPUT AREA
st.header("Output")
st.text_area(
    "Converted Text:", 
    value=st.session_state.output_text, 
    height=100, 
    disabled=True,
    key="output_area",
)

# PLAY SOUND FOR ENGLISH-TO-MORSE
def play_morse(morse_code):
    for char in morse_code:
        if char == '.':
            playsound("short.wav")
            time.sleep(0.1)
        elif char == '-':
            playsound("long.wav")
            time.sleep(0.1)
        elif char == '/':
            time.sleep(0.5)
        else :
            time.sleep(0.5)

# PLAY SOUND FOR MORSE-TO-ENGLISH
def play_speech(english_text):
    engine = pyttsx3.init()
    engine.say(english_text)
    engine.runAndWait()

if st.button("Play"):
    if not st.session_state.morse_code and not st.session_state.output_text:
        st.warning("Please convert something first before playing.")
    elif st.session_state.morse_code:
        play_morse(st.session_state.morse_code)
    elif st.session_state.output_text:
        play_speech(st.session_state.output_text)

# CLEAR BUTTON
if st.button("Clear"):
    st.session_state.input_text = ""
    st.session_state.output_text = ""
    st.session_state.morse_code = ""

# STYLES
st.markdown(
    """
    <style>
    textarea {
        font-size: 20px !important;  /* Applies to both input and output textareas */
        font-family: Arial, sans-serif !important;
        color: #FFFFFF !important;
    }
    .stRadio label {
        font-size: 20px !important;
    }
    </style>
    """, 
    unsafe_allow_html=True,
)
