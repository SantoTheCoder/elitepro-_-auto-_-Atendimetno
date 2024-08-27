import logging
from telethon import events
from messages import WELCOME_MESSAGE
from menu import show_menu, handle_menu_option
from utils import check_reset, is_message_from_support, track_last_message, delete_last_message

def register_handlers(client):
    @client.on(events.NewMessage)
    async def handle_message(event):
        logging.info(f"Nova mensagem recebida de {event.sender_id}: {event.message.message}")

        # Ignora mensagens enviadas pelo suporte
        if is_message_from_support(event):
            logging.info("Mensagem do suporte ignorada.")
            return

        user_id = event.sender_id

        # Excluir a última mensagem do bot, se existir
        await delete_last_message(client, user_id)  # A função delete_last_message agora é assíncrona

        # Verifica se o usuário deve receber a mensagem de boas-vindas
        if check_reset(user_id):
            sender = await event.get_sender()
            first_name = sender.first_name if sender.first_name else "Usuário"
            welcome_message = await event.respond(WELCOME_MESSAGE.format(first_name))
            logging.info("Mensagem de boas-vindas enviada.")
            track_last_message(user_id, welcome_message.id)  # Rastreia a última mensagem
            menu_message = await show_menu(event)
            logging.info("Menu exibido.")
            track_last_message(user_id, menu_message.id)  # Rastreia a última mensagem
        else:
            if event.message.message.lower() == 'menu':
                menu_message = await show_menu(event)
                logging.info("Menu exibido.")
                track_last_message(user_id, menu_message.id)  # Rastreia a última mensagem
            else:
                option_message = await handle_menu_option(event)
                logging.info("Opção de menu tratada.")
                if option_message:  # Verifica se houve uma resposta
                    track_last_message(user_id, option_message.id)  # Rastreia a última mensagem
