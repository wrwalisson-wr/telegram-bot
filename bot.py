from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8712222565:AAH9ajBX11Ky_-H5L6w1ZCQSa65NUbR2-cc"

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    resposta = "Oi 😄 estou online 24h. Você disse: " + texto
    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, responder))

app.run_polling()
