import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"


headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def perguntar_ai(texto):
    payload = {
        "inputs": f"Responda de forma amigável: {texto}"
    }

    

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)

        if response.status_code != 200:
            return "A IA tá dormindo agora 😴 tenta daqui a pouco"

        resultado = response.json()

        print(response.text)

        if isinstance(resultado, list) and 'generated_text' in resultado[0]:
            return resultado[0]['generated_text']

        return "Não entendi direito 😅 tenta falar diferente"

    except Exception as e:
        print("ERRO:", e)
        return "Deu uma travada aqui 😅 tenta de novo"
        

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    resposta = perguntar_ai(texto)

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()


