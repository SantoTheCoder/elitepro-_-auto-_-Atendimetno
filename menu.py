#menu.py
import logging
from messages import MENU_MESSAGE, OPTION_RESPONSES

# Dicionário com palavras-chave para cada opção do menu
KEYWORDS = {
    "1": ["1", "comprar", "compras", "compra", "🛒", "comprar 🛒", "Comprar 🛒"],
    "2": ["2", "troca", "trocar", "material", "📦", "Troca de Material 📦"],
    "3": ["3", "referencia", "referências", "referência", "📑", "Referência 📑"],
    "4": ["4", "como funciona", "funcionamento", "como", "funciona", "🛠️", "Como Funciona 🛠️"],
    "5": ["5", "dicas", "dica", "💡", "Dicas 💡"],
    "6": ["6", "seguro", "segurança", "é seguro?", "é seguro", "🔐", "É Seguro? 🔐"],
    "7": ["7", "falar com suporte", "suporte", "atendimento", "📞", "Falar com Suporte 📞"]
}

async def show_menu(event):
    await event.respond(MENU_MESSAGE)

async def handle_menu_option(event):
    message_text = event.message.message.strip().lower()
    logging.info(f"Processando a mensagem do menu: {message_text}")

    # Verificar todas as palavras-chave, priorizando combinações mais longas e específicas
    for option, keywords in KEYWORDS.items():
        if any(keyword in message_text for keyword in keywords):
            logging.info(f"Palavra-chave encontrada: {keywords} para a opção {option}")
            response = OPTION_RESPONSES.get(option)
            if response:
                await event.respond(response)
                logging.info(f"Resposta enviada para a opção {option}")
                return

    logging.info("Nenhuma palavra-chave correspondente encontrada. Nenhuma ação tomada.")
