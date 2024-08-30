import logging
from messages import MENU_MESSAGE, OPTION_RESPONSES
from utils import delete_last_message, track_last_message, track_last_option_message

# Dicionário com palavras-chave para cada opção do menu
KEYWORDS = {
    "1": ["1", "comprar", "compras", "compra", "🛒", "comprar 🛒", "Comprar 🛒"],
    "2": ["2", "troca", "trocar", "material", "📦", "Troca de Material 📦"],
    "3": ["3", "referencia", "referências", "referência", "📑", "Referência 📑"],
    "4": ["4", "como funciona", "funcionamento", "como", "funciona", "🛠️", "Como Funciona 🛠️"],
    "5": ["5", "grupo de doações", "doações", "grupo", "💳", "Grupo de Doações 💳"],
    "6": ["6", "dicas", "dica", "💡", "Dicas 💡"],
    "7": ["7", "seguro", "segurança", "é seguro?", "é seguro", "🔐", "É Seguro? 🔐"],
    "8": ["8", "falar com suporte", "suporte", "atendimento", "📞", "Falar com Suporte 📞"]
}

async def show_menu(event):
    menu_message = await event.respond(MENU_MESSAGE, reply_to=event.message.id)
    return menu_message  # Retorna a mensagem para rastrear o ID

async def handle_menu_option(event):
    user_id = event.sender_id
    message_text = event.message.message.strip().lower()
    logging.info(f"Processando a mensagem do menu: {message_text}")

    # Exclui a última mensagem antes de responder a nova opção
    await delete_last_message(event.client, user_id)

    # Verificar todas as palavras-chave, priorizando combinações mais longas e específicas
    for option, keywords in KEYWORDS.items():
        if any(keyword in message_text for keyword in keywords):
            logging.info(f"Palavra-chave encontrada: {keywords} para a opção {option}")
            response = OPTION_RESPONSES.get(option)
            if response:
                option_message = await event.respond(response, reply_to=event.message.id)
                logging.info(f"Resposta enviada para a opção {option}")
                
                # Rastreia a mensagem do número selecionado e a resposta associada
                track_last_message(user_id, event.message.id)  # Rastreia o número da seleção
                track_last_option_message(user_id, option_message.id)  # Rastreia a mensagem de resposta
                
                return option_message  # Retorna a mensagem para rastrear o ID

    logging.info("Nenhuma palavra-chave correspondente encontrada. Nenhuma ação tomada.")
    return None  # Retorna None se nenhuma mensagem foi enviada
