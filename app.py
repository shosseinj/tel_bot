from flask import Flask
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import g4f
import asyncio
import os
import threading
import nest_asyncio

# Apply nest_asyncio to allow reuse of the event loop in environments like Jupyter
nest_asyncio.apply()

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running and alive!"

# Telegram Bot logic
async def gpt_handler(message: Message):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        content = response if isinstance(response, str) else "Unexpected response format."
        await message.answer(content)
    except Exception as e:
        await message.answer(f"Error occurred: {str(e)}")

async def start_bot():
    bot_token = os.getenv('TELEGRAM_API_TOKEN')
    if not bot_token:
        raise ValueError("TELEGRAM_API_TOKEN environment variable is not set.")

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    dp.message.register(gpt_handler, F.text)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Polling error: {e}")

def run_flask():
    # Run Flask in a separate thread
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5001)))

if __name__ == '__main__':
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start Telegram bot in the main thread using an existing loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
