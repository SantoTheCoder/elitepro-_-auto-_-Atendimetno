# main.py
from telethon import TelegramClient, events
from config import API_ID, API_HASH, PHONE_NUMBER
from handlers import register_handlers

# Cria o cliente do Telegram
client = TelegramClient('anon', API_ID, API_HASH)

async def main():
    await client.start(phone=PHONE_NUMBER)
    register_handlers(client)
 
