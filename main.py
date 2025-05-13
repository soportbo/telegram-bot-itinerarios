import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("7479654011:AAGz1neoiROjk603ig_lIv1iBDN5pTAr3Xc")  # Render cargará esto como variable de entorno

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu bot de itinerarios y estoy funcionando 24/7 en Render.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot iniciado.")
    app.run_polling()
