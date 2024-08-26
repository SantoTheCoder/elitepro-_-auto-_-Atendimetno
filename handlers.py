#handlers.py
from telethon import events
from messages import WELCOME_MESSAGE
from menu import show_menu, handle_menu_option
from utils import check_reset, is_message_from_support

def register_handlers(client):

    @client.on(events.NewMessage)
    async def handle_message(event):
        # Ignora mensagens enviadas pelo suporte
        if is_message_from_support(event):
            return
        
        user_id = event.sender_id

        # Verifica se o usuário deve receber a mensagem de boas-vindas
        if check_reset(user_id):
            await event.respond(WELCOME_MESSAGE.format(event.sender.first_name))
            await show_menu(event)
        else:
            if event.message.message.lower() == 'menu':
                await show_menu(event)
            elif event.message.message.isdigit():
                await handle_menu_option(event)
