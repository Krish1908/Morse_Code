# IMPORT NECESSARY LIBRARIES

import sqlite3
import os
from dotenv import load_dotenv
from typing import Final 
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# CONSTANS
load_dotenv()
TOKEN: Final = os.getenv('api_key')
BOT_USERNAME: Final = '@morse_krish_bot'

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

# INITIALIZE SQLITE DATABASE
conn = sqlite3.connect("morse_bot.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    username TEXT,
    conversion_type TEXT,
    input_text TEXT,
    output_text TEXT,
    timestamp TEXT
)
''')
conn.commit()

# LOG CONVERSION TO DATABASE
def log_conversion(user_id, username, conversion_type, input_text, output_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO conversions (user_id, username, conversion_type, input_text, output_text, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, username, conversion_type, input_text, output_text, timestamp))
    conn.commit()

# COMMAND HANDLERS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Morse Code Converter Bot! Type '/help' to see available commands.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''
Available Commands:
/e2m <text> - Convert English to Morse Code.
/m2e <morse code> - Convert Morse Code to English.
/history - View your conversion history.
''')

async def e2m(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = ' '.join(context.args).upper()
        if any(char not in morse_dict for char in text):
            await update.message.reply_text("Error: Please enter valid English text.")
        else:
            morse_message = ' '.join(morse_dict[c] for c in text)
            log_conversion(update.effective_user.id, update.effective_user.username, "e2m", text, morse_message)
            await update.message.reply_text(f"Morse Code: {morse_message}")
    else:
        await update.message.reply_text("Usage: /e2m <text>")

async def m2e(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        morse_code = ' '.join(context.args)
        if any(code not in reverse_dict for code in morse_code.split()):
            await update.message.reply_text("Error: Please enter valid Morse Code.")
        else:
            english_message = ''.join(reverse_dict[code] for code in morse_code.split())
            log_conversion(update.effective_user.id, update.effective_user.username, "m2e", morse_code, english_message)
            await update.message.reply_text(f"English Text: {english_message}")
    else:
        await update.message.reply_text("Usage: /m2e <morse code>")

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cursor.execute("SELECT conversion_type, input_text, output_text, timestamp FROM conversions WHERE user_id = ?", (user_id,))
    records = cursor.fetchall()
    if records:
        history = "\n".join([f"{r[3]} | {r[0]}: {r[1]} -> {r[2]}" for r in records])
        await update.message.reply_text(f"Your Conversion History:\n{history}")
    else:
        await update.message.reply_text("No history found.")

# MESSAGE HANDLERS
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I didn't understand that. Type '/help' to see available commands.")

# MAIN FUNCTION
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("e2m", e2m))
    app.add_handler(CommandHandler("m2e", m2e))
    app.add_handler(CommandHandler("history", history))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot is running...")
    app.run_polling()
