# Morse Code Converter
## Overview
The **Morse Code Converter** is an interactive application built for seamless text-to-Morse code and Morse-to-text conversions. Available as a GUI (Tkinter), Web App (Streamlit), and a Telegram Bot, this project combines simplicity with versatility.

Experience real-time conversions, audio playback, and a history feature that makes it easy to track past conversions. Whether you're exploring Morse code or building similar apps, this project offers a strong foundation!

## Features:
- **English to Morse Code Conversion:** Convert standard English text into Morse Code.

- **Morse Code to English Conversion:** Decode Morse Code into readable English text.

- **Responsive Interface:** Clean and minimalistic UI with support for larger fonts for better readability.

- **Multi-Platform Support:** Access via terminal, GUI (Tkinter), Web App (Streamlit), or Telegram Bot.

- **Audio Playback:** Plays audio for the selected conversion output.

- **Telegram Bot Integration:** A bot offering real-time conversions with easy-to-use commands.

- **History Tracking:** Maintains a history of the conversions made.

## Technologies Used:
- **Tkinter:** A GUI for Basic Python applications.

- **Streamlit:** A powerful Python framework for building interactive web applications.

- **Python:** Core programming language for the application logic.

- **SQLite:** To store the conversion history in database.

- **Python Anywhere:** To host the telegram bot script.

## Dependencies:
Install all the required dependencies from the `requirements.txt` file. Open your terminal and run the following command:

`pip install -r requirements.txt`

## Available Scripts:
**Morse_Code_01.py:** This is a python script which is deployed for the Terminal.

**Morse_Code_02.py:** This is a python script which is deployed using Tkinter.

**Morse_Code_03.py:** This is a python script which is deployed using Streamlit.

**Morse_Code_04.py:** This is a python script which is deployed for Telegram Bot.


## Steps:

1. Clone or download this repository.

2. Open the code in your editor.

3. Install the dependencies using `requirements.txt`

4. To run Morse Code 01 (terminal code), use the below line in your terminal.
   
   `py morse_code_01.py`

   To run Morse Code 02 (tkinter), use the below line in your terminal.

   `py morse_code_02.py`

   To run Morse Code 03 (streamlit), use the below line in your terminal.

   `streamlit run morse_code_03.py`

5. Enter your text in the Input Text area.

6. Select the conversion type:

   English to Morse Code or Morse Code to English

7. Click the Convert button to see the results in the Output area.

8. Click the play button to hear the output as audio.

9. To clear all fields, click the Clear button.

10. To use the telegram bot, open your telegram application and search for `morse_krish_bot`

11. Go through the `/help` command and use the bot.
