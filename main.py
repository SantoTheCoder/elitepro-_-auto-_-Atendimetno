#main.py
import logging
from telethon import TelegramClient
from config import API_ID, API_HASH, PHONE_NUMBER
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

# Cria o cliente do Telegram
client = TelegramClient('anon', API_ID, API_HASH)

async def main():
    await client.start(phone=PHONE_NUMBER)
    logging.info("Cliente Telegram iniciado e conectado.")
    register_handlers(client)
    logging.info("Handlers registrados com sucesso.")

client.loop.run_until_complete(main())
client.run_until_disconnected()
