# handlers.py
import logging
from telethon import events
from messages import WELCOME_MESSAGE
from menu import show_menu, handle_menu_option
from utils import check_reset, is_message_from_support

def register_handlers(client):
    @client.on(events.NewMessage)
    async def handle_message(event):
        logging.info(f"Nova mensagem recebida de {event.sender_id}: {event.message.message}")

        # Ignora mensagens enviadas pelo suporte
        if is_message_from_support(event):
            logging.info("Mensagem do suporte ignorada.")
            return

        user_id = event.sender_id

        # Verifica se o usuário deve receber a mensagem de boas-vindas
        if check_reset(user_id):
            sender = await event.get_sender()
            first_name = sender.first_name if sender.first_name else "Usuário"
            await event.respond(WELCOME_MESSAGE.format(first_name))
            logging.info("Mensagem de boas-vindas enviada.")
            await show_menu(event)
            logging.info("Menu exibido.")
        else:
            if event.message.message.lower() == 'menu':
                await show_menu(event)
                logging.info("Menu exibido.")
            else:
                await handle_menu_option(event)
                logging.info("Opção de menu tratada.")
