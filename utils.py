#utils.py
from datetime import datetime, timedelta
from config import SUPPORT_IDS

# Dicionário para armazenar a última interação com o menu para cada usuário
user_last_interaction = {}

# Configurações do reset
RESET_INTERVAL = timedelta(hours=24)

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
