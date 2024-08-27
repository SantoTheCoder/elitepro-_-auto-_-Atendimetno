# messages.py
WELCOME_MESSAGE = """
Bom dia, {}! 🦾

Seja bem-vindo à **ELITEPRO**! Aqui, seu dinheiro vale mais! 💵💎

Você está falando comigo porque quer fazer umas compras, certo? 🛒😎

Abaixo, você encontrará as perguntas mais frequentes. Basta seguir o menu. Se precisar de ajuda, envie "Falar com atendente" que logo vou estar aqui para te ajudar. 🚀

Mas antes disso, descubra mais sobre nossos produtos e vantagens! Explore tudo abaixo! 👇🦾

---

🚀 **Aqui está o nosso **Menu Principal** para você navegar e encontrar tudo o que precisa. Basta selecionar a opção desejada e seguir as instruções! 👇**
"""

MENU_MESSAGE = """
1. **Comprar** 🛒
2. **Referência** 📑
3. **Como Funciona** 🛠️
4. **Diferenças de CCs** 🩸
5. **Tipos de Material** 📦
6. **Dicas** 💡
7. **Garantias** 🔒
8. **É Seguro?** 🛡️
9. **Falar com Suporte** 📞

**Escolha a opção correspondente digitando o número e enviarei mais informações detalhadas!**

Se precisar de assistência em qualquer momento, basta digitar "Falar com atendente" e um de nossos especialistas estará aqui para te ajudar! 🚀
"""

# Respostas para cada opção, com instruções para retornar ao menu principal
OPTION_RESPONSES = {
    "1": """
**❓ Como Comprar? 🛒**

É muito simples! Somos os maiores e melhores vendedores de CCs do Brasil, com mais de 100.000 unidades vendidas! 🇧🇷✨

Você pode adquirir seu material com garantia de qualidade absoluta através do nosso bot @ElitePRO_Store_Bot. Para começar, escreva **/start** no bot e, para adicionar saldo, digite: **/recarga "valor"**. Exemplo: **/recarga 50** para uma recarga de R$50. 📱💳

Se tiver dúvidas sobre como funciona, nossas referências, dicas de uso e muito mais, basta escrever **Menu** e selecionar a opção desejada. ✅

---

Escreva "Menu" para retornar ao menu principal.
""",
    "2": """
**📑 Referências**

Confira nosso canal com as referências do nosso material: @ElitePRO_Store. Pode observar que todo dia temos muitas referências de nosso material. Venha comprovar e fazer a compra que tanto deseja. Também temos vários grupos no Telegram, totalizando mais de 100.000 pessoas! 🎉

---

Escreva "Menu" para retornar ao menu principal.
""",
    "3": """
**🔧 Como Funciona?**

CCs são cartões clonados que você pode usar na hora de fazer a compra, utilizando a modalidade de pagamento de cartão de crédito, principalmente em compras online, mas podendo ser usadas pessoalmente também, desde que permitam inserir os dados do cartão. 

Trabalhamos com diferentes categorias de cartões:

1. **Promoção**: Cartões promocionais prontos para uso.
2. **Garantia de Débito**: Cartões com valor debitado antes da entrega.
3. **FULL DADOS**: Cartões com dados reais do dono.
4. **Garantia de Saldo**: Cartões com saldo mínimo garantido.

Nosso bot automático está sempre funcionando, então você pode realizar suas compras a qualquer hora. Vá diretamente no bot @ElitePRO_Store_Bot para começar. 🕒

---

Escreva "Menu" para retornar ao menu principal.
""",
    "4": """
**💳 Diferenças de CCs** 🩸

Níveis e limites dos cartões:

- 🏛 **Classic**: Limite máximo de R$150 a R$180.
- ♨️ **Standard**: Limite máximo de R$200 a R$250.
- 👑 **Gold**: Limite máximo de R$400 a R$470.
- 🪙 **Platinum**: Limite máximo de R$600 a R$700.
- 🪢 **Elo**: Limite máximo de R$800 a R$850.
- 💎 **Business**: Limite máximo de R$1000.
- ♾ **Black/Infinite**: Limite inicial de R$1000 (sem limite máximo).

🩸 Pode haver variações de saldo nos infocc/cc. 

---

Escreva "Menu" para retornar ao menu principal.
""",
    "5": """
**Tipos de Material** 📦

Trabalhamos com os seguintes tipos de material:

1. **PROMO**: Cartões promocionais verificados na entrega. Tempo para troca: 20 minutos (troca direto pelo bot).
2. **GARANTIA DE DÉBITO**: Cartões debitados antes da entrega para garantir que estão prontos para uso. Tempo para troca: 20 minutos (envie um vídeo realizando a compra e encaminhe para troca).
3. **FULL DADOS**: Cartões com dados reais do dono, recomendados para aprovações em sites maiores e valores altos.
4. **Garantia de Saldo**: Cartões vendidos com garantia de saldo mínimo. Tempo para troca: 25 minutos (envie um vídeo comprando um curso na Hotmart e encaminhe o material recebido).

---

Escreva "Menu" para retornar ao menu principal.
""",
    "6": """
**💡 Dicas**

Temos um canal de dicas personalizadas: [ElitePROCC_Dicas](https://t.me/ElitePROCC_Dicas). Saiba todas as informações sobre CCs, segurança, dicas para aprovação e muito mais! 🌟

---

Escreva "Menu" para retornar ao menu principal.
""",
    "7": """
**🔒 Garantias**

Nós garantimos todo nosso material, entregando LIVE e com garantia de funcionamento. Conheça os tipos de material:

- **PROMO**: Cartões promocionais verificados na entrega. Tempo para troca: 20 minutos (troca direto pelo bot).
- **GARANTIA DE DÉBITO**: Cartões debitados antes da entrega para garantir que estão prontos para uso. Tempo para troca: 20 minutos (envie um vídeo realizando a compra e encaminhe para troca).
- **FULL DADOS**: Cartões com dados reais do dono, recomendados para aprovações em sites maiores e valores altos.
- **Garantia de Saldo**: Cartões vendidos com garantia de saldo mínimo. Tempo para troca: 25 minutos (envie um vídeo comprando um curso na Hotmart e encaminhe o material recebido).

---

Escreva "Menu" para retornar ao menu principal.
""",
    "8": """
**🔐 Segurança ao Usar CCs**

Uma pergunta frequente é: **É perigoso fazer aprovação?**

A resposta é: **DEPENDE**. 🚀 Se o titular contestar a compra, o banco pode investigar e pode ser ressarcido. O banco vai cruzar informações diversas como:

- ⚠ Titular não costuma fazer compras naquele site.
- ⚠ Titular não costuma fazer compras daquele valor.
- ⚠ Titular não costuma fazer compras online.
- ⚠ Titular não costuma fazer compras internacionais.
- ⚠ Titular não costuma fazer compras naquele horário.
- ⚠ Titular nunca utiliza mais de 80% do limite do cartão de crédito.

O banco geralmente pede investigação junto à polícia quando a fraude é grande, ou seja, estamos falando de aprovações diversas de valores altos acima dos 20 mil reais. 

Ainda assim, pode haver problemas com valores baixos? SIM. Um exemplo é você fazer várias compras no iFood sempre no mesmo restaurante, com cartões diversos. O restaurante saberá dos estornos. Isso não será bom para você. Evite comprar sempre no mesmo lugar e com muita frequência. Isso se chama DROP QUEIMADO.

---

Escreva "Menu" para retornar ao menu principal.
""",
    "9": """
**Falar com Suporte** 📞

Um atendente humano estará disponível em breve para te ajudar. 🚀

---

Escreva "Menu" para retornar ao menu principal.
"""
}
