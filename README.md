# Morse Code Converter And Game
## Overview
This is an interactive application built for seamless text-to-Morse code, Morse-to-text conversions and to test the knowledge on both. Available as a GUI (Tkinter), Web App (Streamlit), and a Telegram Bot, this project combines simplicity with versatility.

Experience real-time conversions, audio playback, and a history feature that makes it easy to track past conversions. Whether you're exploring Morse code or building similar apps, this project offers a strong foundation!

## Features:
- **English to Morse Code Conversion:** Convert standard English text into Morse Code.

- **Morse Code to English Conversion:** Decode Morse Code into readable English text.

- **Responsive Interface:** Clean and minimalistic UI with support for larger fonts for better readability.

- **Multi-Platform Support:** Access via terminal, GUI (Tkinter), Web App (Streamlit), or Telegram Bot.

- **Audio Playback:** Plays audio for the selected conversion output.

- **Telegram Bot Integration:** A bot offering real-time conversions with easy-to-use commands.

- **History Tracking:** Maintains a history of the conversions made.

- **Interactive Knowledge Chech:** Allows users to check their knowledge on encoding and decoding the content via a interative game.

## Technologies Used:
- **Tkinter:** A GUI for Basic Python applications.

- **Streamlit:** A powerful Python framework used to build interactive web applications and to deploy in Streamlit Community Cloud.

- **Python:** Core programming language for the application logic.

- **SQLite:** To store the conversion history in database.

- **Python Anywhere:** To host the telegram bot script.

- **Nltk:** Used for generating the Logical English words.

## Dependencies:
Install the required dependencies using the provided `requirements.txt` file.

`pip install -r requirements.txt`

This will install all the necessary libraries, including:
```
playsound
pyttsx3
streamlit
python-telegram-bot
nltk
```

## Available Scripts:
**Morse_Code_01.py:** This is a python script which is used for conversion and deployed for the Terminal.

**Morse_Code_02.py:** This is a python script which is used for conversion and deployed using Tkinter.

**Morse_Code_03.py:** This is a python script which is used for conversion and deployed using Streamlit.

**Morse_Code_04.py:** This is a python script which is used for conversion and deployed for Telegram Bot.

**Morse_Game_01.py:** This is a python script which is used for knowledge chech (interactive game) and deployed for the Terminal.

**Morse_Game_02.py:** This is a python script which is used for knowledge chech (interactive game) and deployed using Streamlit.


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

   To run Morse Code 04 (Telegram Bot), create a file named `.env` in the same directory. The format of the file should be like this:

   ```
     [groq]
     api_key = "your-api-key-here"
   ```
   Replace `your-groq-api-key-here` with your actual GROQ CLOUD API key.

   Then use the below line in your terminal.

   `py morse_code_04.py`

6. Enter your text in the Input Text area.

7. Select the conversion type:

   English to Morse Code or Morse Code to English

8. Click the Convert button to see the results in the Output area.

9. Click the play button to hear the output as audio.

10. To clear all fields, click the Clear button.

11. To use the telegram bot, open your telegram application and search for `morse_krish_bot`

12. Go through the `/help` command and use the bot.

13. To test your knowledge on conversion, try out   `morse_game_02.py` or click [here.](https://krish-mini-projects-morse-game.streamlit.app)
