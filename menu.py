from messages import MENU_MESSAGE, OPTION_RESPONSES

# Dicionário com palavras-chave para cada opção do menu
KEYWORDS = {
    "1": ["1", "comprar", "compras", "compra", "🛒", "comprar 🛒", "Comprar 🛒"],
    "2": ["2", "referencia", "referências", "referência", "📑", "Referência 📑"],
    "3": ["3", "como funciona", "funcionamento", "como", "funciona", "🛠️", "Como Funciona 🛠️"],
    "4": ["4", "diferenças", "diferença", "diferencas", "cc", "ccs", "diferenças de ccs", "🩸", "Diferenças de CCs 🩸"],
    "5": ["5", "tipos", "material", "tipos de material", "📦", "Tipos de Material 📦"],
    "6": ["6", "dicas", "dica", "💡", "Dicas 💡"],
    "7": ["7", "garantias", "garantia", "seguro", "segurança", "🔒", "Garantias 🔒"],
    "8": ["8", "seguro", "segurança", "é seguro?", "é seguro", "🔐", "É Seguro? 🔐"],
    "9": ["9", "falar com suporte", "suporte", "atendimento", "📞", "Falar com Suporte 📞"]
}

async def show_menu(event):
    await event.respond(MENU_MESSAGE)

async def handle_menu_option(event):
    message_text = event.message.message.strip().lower()

    # Verificar todas as palavras-chave
    for option, keywords in KEYWORDS.items():
        if any(keyword.lower() in message_text for keyword in keywords):
            response = OPTION_RESPONSES.get(option)
            if response:
                await event.respond(response)
                return

    await event.respond("Opção inválida. Por favor, escolha um número do menu.")
