# Morse Code Converter And Game
## Overview
This interactive application allows for seamless text-to-Morse code and Morse-to-text conversions, as well as a fun way to test your knowledge of both. Available as a GUI (Tkinter), Web App (Streamlit), and Telegram Bot, this project combines simplicity with versatility.

Experience real-time conversions, audio playback, and a history feature that tracks past conversions. Whether you're learning Morse code or building similar apps, this project offers a solid foundation!

## Features:
- **English to Morse Code Conversion:** Convert standard English text into Morse Code.

- **Morse Code to English Conversion:** Decode Morse Code into readable English text.

- **Responsive Interface:** Clean and minimalistic UI with support for larger fonts for better readability.

- **Multi-Platform Support:** Access via terminal, GUI (Tkinter), Web App (Streamlit), or Telegram Bot.

- **Audio Playback:** Plays audio for the selected conversion output.

- **Telegram Bot Integration:** A bot offering real-time conversions with easy-to-use commands.

- **History Tracking:** Maintains a history of the conversions made.

- **Interactive Knowledge Chech:** Test your Morse code encoding/decoding skills with an interactive game.

## Technologies Used:
- **Tkinter:** A GUI for Basic Python applications.

- **Streamlit:** A powerful Python framework for building and deploying interactive web applications.
  
- **Python:** Core programming language for the application logic.

- **SQLite:** To store the conversion history in database.

- **Python Anywhere:** To host the telegram bot script.

- **Nltk:** Used to generate logical English words for the game.

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
**Morse_Code_01.py:** Conversion logic for the terminal.

**Morse_Code_02.py:** Conversion logic using Tkinter for GUI.

**Morse_Code_03.py:** Conversion logic with Streamlit (Web app)

**Morse_Code_04.py:** Conversion logic for Telegram Bot.

**Morse_Game_01.py:** Interactive game for testing knowledge (Terminal).

**Morse_Game_02.py:** Interactive game for testing knowledge (Streamlit).

## Steps:

1. Clone or download this repository.

2. Open the code in your editor.

3. Install the dependencies using `requirements.txt`

4. Create a bot using BotFather and customize your bot in telegram.

5. To run Morse Code 01 (terminal code):
   
   `py morse_code_01.py`

   To run Morse Code 02 (tkinter):

   `py morse_code_02.py`

   To run Morse Code 03 (streamlit):

   `streamlit run morse_code_03.py`

   To run Morse Code 04 (Telegram Bot), create a file named `.env` in the same directory with the following format:

   ```
     api_key = "your-api-key-here"
   ```
   Replace `your-api-key-here` with your actual BotFather API key, then run:

   `py morse_code_04.py`

6. Using the Application:
   - Enter text in the input area.
   - Select the conversion type (English to Morse or Morse to English)
   - Click the "Convert" button to view the result in the output area.
   - Press the "Play" button to hear the conversion as audio.
   - Click "Clear" to reset the fields.

7. Using the Telegram Bot:
   - Open your Telegram app and search for `morse_krish_bot`.
   - Use the `/help` command to get started.
  
8. Testing Knowledge (Interactive Game):
   - Run `Morse_Game_02.py` to play the interactive game or access it via [this link.](https://krish-mini-projects-morse-game.streamlit.app)
