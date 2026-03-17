import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI

TOKEN = os.getenv("8712222565:AAH9ajBX11Ky_-H5L6w1ZCQSa65NUbR2-cc")
client = OpenAI(api_key=os.getenv("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"))

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    resposta_ai = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Você é uma amiga virtual simpática e inteligente."},
            {"role": "user", "content": texto}
        ]
    )

    resposta = resposta_ai.choices[0].message.content

    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, responder))
app.run_polling()
