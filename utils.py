from datetime import datetime, timedelta
from config import SUPPORT_IDS

# Dicionário para armazenar a última interação com o menu para cada usuário
user_last_interaction = {}
user_last_message_id = {}  # Novo dicionário para armazenar o ID da última mensagem enviada pelo bot

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

async def delete_last_message(client, user_id):
    """
    Exclui a última mensagem enviada pelo bot para o usuário.
    """
    last_message_id = get_last_message_id(user_id)
    if last_message_id:
        try:
            await client.delete_messages(user_id, last_message_id)
        except Exception as e:
            logging.error(f"Erro ao excluir a última mensagem: {e}")
