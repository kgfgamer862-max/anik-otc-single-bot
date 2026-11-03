
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❤️ Welcome to ANIK OTC SINGLE BOT!\n"
        "OTC Demo Signal Bot is online.\n\n"
        "Use /signal to request analysis."
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 OTC Analysis\n\n"
        "Live OTC data is not connected yet.\n"
        "No verified BUY/SELL signal available.\n"
        "Please use Demo only."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start Bot\n"
        "/signal - Request Analysis\n"
        "/help - Help"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN missing!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
