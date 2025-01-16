# IMPORT THE NECESSARY LIBRARIES

import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import pyttsx3
from playsound import playsound
import time

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

# INITIALIZE TEXT-TO-SPEECH ENGINE
text_speech = pyttsx3.init()

# CONVERT ENGLISH TO MORSE
def english_to_morse():
    input_text = input_box.get("1.0", tk.END).strip().upper()
    try:
        global current_mode
        current_mode = "ENG_TO_MORSE"
        global morse_code
        morse_code = ' '.join(morse_dict[c] for c in input_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, morse_code)
    except KeyError:
        messagebox.showerror("Error", "Invalid character found in input. Only letters, numbers, and spaces are allowed.")

# CONVERT MORSE TO ENGLISH
def morse_to_english():
    input_text = input_box.get("1.0", tk.END).strip()
    try:
        global current_mode
        current_mode = "MORSE_TO_ENG"
        global english_text
        english_text = ''.join(reverse_dict[c] for c in input_text.split(' '))
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, english_text)
    except KeyError:
        messagebox.showerror("Error", "Invalid Morse code found in input.")

# CLEAR FIELDS
def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

# PLAY SOUND BASED ON CONVERSION
def play_output():
    if not output_box.get("1.0", tk.END).strip():
        messagebox.showinfo("Alert", "Convert something first to play!")
        return

    if current_mode == "ENG_TO_MORSE":
        morse_output = output_box.get("1.0", tk.END).strip()
        
        for char in morse_output:
            if char == '.':
                playsound("short.wav")
                time.sleep(0.1)
            elif char == '-':
                playsound("long.wav")
                time.sleep(0.1)
            elif char == '/':
                time.sleep(0.5)
            else:
                time.sleep(0.5)
        
    elif current_mode == "MORSE_TO_ENG":
        english_output = output_box.get("1.0", tk.END).strip()
        text_speech.say(english_output)
        text_speech.runAndWait()


# MAIN WINDOW
root = tk.Tk()
root.title("Morse Code Converter")
root.resizable(False, False)

# UI - FONTS
title_font = Font(family="Helvetica", size=16, weight="bold")
label_font = Font(family="Helvetica", size=12)
button_font = Font(family="Helvetica", size=10, weight="bold")
text_font = Font(family="Courier", size=12)

# UI - COLORS
bg_color = "#f0f8ff"  
button_color = "#4682b4"
button_text_color = "white"
text_bg_color = "white"
text_fg_color = "black"

# UI - BG COLOR
root.configure(bg=bg_color)

# TITLE
title_label = tk.Label(root, text="Morse Code Converter", font=title_font, bg=bg_color)
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# INPUT AREA
input_label = tk.Label(root, text="Input:", font=label_font, bg=bg_color)
input_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_box = tk.Text(root, height=5, width=50, font=text_font, bg=text_bg_color, fg=text_fg_color)
input_box.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# OUTPUT AREA
output_label = tk.Label(root, text="Output:", font=label_font, bg=bg_color)
output_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
output_box = tk.Text(root, height=5, width=50, font=text_font, bg=text_bg_color, fg=text_fg_color)
output_box.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# CONVERSION BUTTONS
to_morse_button = tk.Button(root, text="Convert to Morse Code", font=button_font, bg=button_color, fg=button_text_color, command=english_to_morse)
to_morse_button.grid(row=5, column=0, padx=10, pady=10)

to_english_button = tk.Button(root, text="Convert to English", font=button_font, bg=button_color, fg=button_text_color, command=morse_to_english)
to_english_button.grid(row=5, column=1, padx=10, pady=10)

clear_button = tk.Button(root, text="Clear", font=button_font, bg=button_color, fg=button_text_color, command=clear_text)
clear_button.grid(row=5, column=2, padx=10, pady=10)

# PLAY BUTTON
play_button = tk.Button(root, text="Play Output", font=button_font, bg=button_color, fg=button_text_color, command=play_output)
play_button.grid(row=6, column=1, padx=10, pady=10)

# RUN THE CODE
current_mode = None  # Track the current mode (ENG_TO_MORSE or MORSE_TO_ENG)
root.mainloop()
