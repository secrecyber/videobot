from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7252155462:AAGkF0objeszRAG_IHSPi6ltsC-Rtx8EKHg"

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.video:
        await update.message.reply_text(f"File ID: {update.message.video.file_id}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, get_file_id))
print("✅ File ID bot ishga tushdi...")
app.run_polling()
