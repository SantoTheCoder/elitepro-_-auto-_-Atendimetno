#handlers.py
import logging
from telethon import events
from telethon.tl.types import User
from messages import MENU_MESSAGE, WELCOME_MESSAGE
from menu import show_menu, handle_menu_option
from utils import (
    check_reset,
    is_message_from_support,
    track_last_message,
    delete_last_message,
    track_fixed_menu,
    get_fixed_menu_id,
    track_last_option_message
)

def register_handlers(client):
    @client.on(events.NewMessage)
    async def handle_message(event):
        logging.info(f"Nova mensagem recebida de {event.sender_id}: {event.message.message}")

        # Ignora mensagens enviadas pelo suporte ou que não são de usuários
        if is_message_from_support(event) or not await is_user_message(event):
            logging.info("Mensagem de bot, canal, ou grupo ignorada.")
            return

        user_id = event.sender_id

        # Excluir a última mensagem do bot, se existir (exceto o menu fixo)
        await delete_last_message(client, user_id)

        # Verifica se o usuário deve receber a mensagem de boas-vindas e exibir o menu fixo
        if check_reset(user_id):
            sender = await event.get_sender()
            first_name = sender.first_name if sender.first_name else "Usuário"
            welcome_message = await event.respond(WELCOME_MESSAGE.format(first_name), reply_to=event.message.id)
            logging.info("Mensagem de boas-vindas enviada.")
            track_last_message(user_id, welcome_message.id)  # Rastreia a última mensagem

            # Exibe e fixa o menu fixo apenas uma vez
            fixed_menu_id = get_fixed_menu_id(user_id)
            if not fixed_menu_id:
                menu_message_user = await show_and_pin_menu(event, client)
                logging.info("Menu fixo exibido e fixado no chat do usuário.")
                track_fixed_menu(user_id, menu_message_user.id)  # Rastreia o ID do menu fixo no chat do usuário
        else:
            if event.message.message.lower() == 'menu':
                menu_message = await show_menu(event)
                logging.info("Menu exibido.")
                track_last_message(user_id, menu_message.id)  # Rastreia a última mensagem
            else:
                option_message = await handle_menu_option(event)
                logging.info("Opção de menu tratada.")
                if option_message:  # Verifica se houve uma resposta
                    track_last_message(user_id, event.message.id)  # Rastreia o número da seleção do usuário
                    track_last_option_message(user_id, option_message.id)  # Rastreia a mensagem de resposta do menu

async def show_and_pin_menu(event, client):
    """
    Exibe e fixa o menu no chat do usuário.
    """
    menu_message = await event.respond(MENU_MESSAGE, reply_to=event.message.id)
    await client.pin_message(event.chat_id, menu_message.id, notify=False)  # Fixa a mensagem no chat do usuário
    return menu_message

async def is_user_message(event):
    """
    Verifica se a mensagem é de um usuário (não bot, não canal, não grupo).
    """
    try:
        sender = await event.get_sender()

        # Verifica se é um usuário real
        if isinstance(sender, User):
            return not sender.bot  # Retorna True se não for um bot

        return False
    except Exception as e:
        logging.error(f"Erro ao verificar tipo de entidade: {e}")
        return False
