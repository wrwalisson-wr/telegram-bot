import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def perguntar_ai(texto):
    payload = {
        "inputs": texto
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        resultado = response.json()

        if isinstance(resultado, list):
            return resultado[0].get('generated_text', 'Sem resposta 😅')

        return "Pensando... tenta de novo 😄"

    except Exception as e:
        print(e)
        return "Deu uma travada aqui 😅 tenta de novo"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    resposta = perguntar_ai(texto)

    await update.message.reply_text(resposta)

print(response.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()
