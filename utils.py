#utils.py
from datetime import datetime, timedelta
import logging
from config import SUPPORT_IDS
from telethon.tl.types import User, PeerUser, PeerChat, PeerChannel

# Dicionário para armazenar a última interação com o menu para cada usuário
user_last_interaction = {}
user_last_message_id = {}  # Armazena o ID da última mensagem enviada pelo bot
user_fixed_menu_id = {}  # Dicionário para armazenar o ID do menu fixo
user_last_option_message_id = {}  # Dicionário para armazenar o ID da última mensagem de opção do menu
user_message_timestamps = {}  # Dicionário para armazenar os timestamps das mensagens dos usuários
spam_blocked_users = {}  # Dicionário para armazenar usuários bloqueados temporariamente por spam

# Configurações do reset
RESET_INTERVAL = timedelta(hours=24)
SPAM_INTERVAL = timedelta(minutes=1)  # Intervalo para considerar o spam (1 minuto)
SPAM_THRESHOLD = 10  # Número de mensagens permitido dentro do intervalo
SPAM_BLOCK_TIME = timedelta(minutes=1)  # Tempo de bloqueio por spam (5 minutos)

def check_reset(user_id):
    now = datetime.now()
    if user_id not in user_last_interaction or now - user_last_interaction[user_id] > RESET_INTERVAL:
        user_last_interaction[user_id] = now
        return True
    return False

def is_message_from_support(event):
    """
    Função para verificar se a mensagem foi enviada pelo suporte, com base na lista configurável de IDs.
    """
    return event.sender_id in SUPPORT_IDS

async def is_personal_contact(client, user_id):
    """
    Verifica se o usuário é um contato pessoal do bot.
    Utiliza o método `get_entity` como alternativa ao `get_contacts`.
    """
    try:
        # Usa `get_entity` para obter informações sobre o usuário
        entity = await client.get_entity(user_id)
        
        # Verifica se a entidade é um usuário e não um bot
        return isinstance(entity, User) and not entity.bot
    except Exception as e:
        logging.error(f"Erro ao verificar se o usuário é um contato pessoal: {e}")
        return False


def track_last_message(user_id, message_id):
    """
    Armazena o ID da última mensagem enviada pelo bot para o usuário.
    """
    user_last_message_id[user_id] = message_id

def get_last_message_id(user_id):
    """
    Retorna o ID da última mensagem enviada pelo bot para o usuário.
    """
    return user_last_message_id.get(user_id)

def track_last_option_message(user_id, message_id):
    """
    Armazena o ID da última mensagem de resposta associada a uma opção do menu.
    """
    user_last_option_message_id[user_id] = message_id

def get_last_option_message_id(user_id):
    """
    Retorna o ID da última mensagem de resposta associada a uma opção do menu.
    """
    return user_last_option_message_id.get(user_id)

async def delete_last_message(client, user_id):
    """
    Exclui a última mensagem enviada pelo bot para o usuário, exceto a mensagem do menu fixo.
    """
    last_message_id = get_last_message_id(user_id)
    last_option_message_id = get_last_option_message_id(user_id)
    fixed_menu_id = user_fixed_menu_id.get(user_id)

    # Exclui a última mensagem de opção, se existir, e se não for a mensagem do menu fixo
    if last_option_message_id and last_option_message_id != fixed_menu_id:
        try:
            await client.delete_messages(user_id, last_option_message_id)
        except Exception as e:
            logging.error(f"Erro ao excluir a última mensagem de opção: {e}")

    # Exclui a última mensagem enviada pelo bot, se não for a mensagem do menu fixo
    if last_message_id and last_message_id != fixed_menu_id:
        try:
            await client.delete_messages(user_id, last_message_id)
        except Exception as e:
            logging.error(f"Erro ao excluir a última mensagem: {e}")

def track_fixed_menu(user_id, message_id):
    """
    Armazena o ID da mensagem do menu fixo.
    """
    user_fixed_menu_id[user_id] = message_id

def get_fixed_menu_id(user_id):
    """
    Retorna o ID da mensagem do menu fixo.
    """
    return user_fixed_menu_id.get(user_id)

def is_spam(user_id):
    """
    Verifica se o usuário enviou mensagens em excesso em um curto período de tempo (filtro de spam).
    """
    now = datetime.now()

    # Limpa as entradas antigas do dicionário de bloqueio por spam
    if user_id in spam_blocked_users:
        block_time = spam_blocked_users[user_id]
        if now - block_time > SPAM_BLOCK_TIME:
            del spam_blocked_users[user_id]  # Remove bloqueio se o tempo expirou

    # Se o usuário está atualmente bloqueado por spam, retorna True
    if user_id in spam_blocked_users:
        return True

    # Adiciona o timestamp da mensagem ao histórico do usuário
    if user_id not in user_message_timestamps:
        user_message_timestamps[user_id] = []
    user_message_timestamps[user_id].append(now)

    # Remove timestamps antigos (fora do intervalo de 1 minuto)
    user_message_timestamps[user_id] = [timestamp for timestamp in user_message_timestamps[user_id] if now - timestamp <= SPAM_INTERVAL]

    # Verifica se o usuário excedeu o limite de mensagens permitidas
    if len(user_message_timestamps[user_id]) > SPAM_THRESHOLD:
        spam_blocked_users[user_id] = now  # Bloqueia o usuário temporariamente
        return True

    return False

def is_private_chat(event):
    """
    Verifica se a mensagem foi enviada em um chat privado (PeerUser).
    """
    return isinstance(event.message.peer_id, PeerUser)
