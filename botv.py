from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)

BOT_TOKEN = "7252155462:AAGkF0objeszRAG_IHSPi6ltsC-Rtx8EKHg"
KANALLAR = ["@azizbek_cyber"]
INSTAGRAM_LINK = "https://www.instagram.com/aziz_cyber"
VIDEO_IDS = {
    "1": "BAACAgIAAxkBAANnaEPsuHp3K8xSM0bdC9f6Vc2zcYgAArlIAAI5iYBJ4B7cK7Q7xEs2BA",  # kod: 1
    "2": "BAACAgIAAxkBAANpaEPs6zrY0RZbxERn40Kc-rv3oVYAAqdaAAIGzqlIjzP2CaeQ-Ig2BA",  # kod: 2
    "3": "BAACAgIAAxkBAANqaEPs65t5_ZohZr5-0ygeKKStPIgMAAoJyAAIq94hJRi2dPz8BcaM2BA",  # kod: 3
    "4": "BAACAgIAAxkBAANraEPs62uiWD1WQGdo3LgXrMZleMEAAv1qAAJfWSFI6v3M5_hUfYo2BA",  # kod: 4
    "5": "BAACAgIAAxkBAANsaEPs6yLxkUa-RwrV3RbMwXpuhjIAAo5zAAKOCwFJNxZiqUV4me42BA",  # kod: 5
    "6": "BAACAgIAAxkBAANtaEPs61s_l1jpIRJ-CHg1gRMPGGUAAp9SAAI7PeBJbq3Uvx1jFUg2BA",  # kod: 6
    "7": "BAACAgIAAxkBAANuaEPs66Hdc4MQ7y_7NI1QkbHD40EAAmRrAAImQrhImklLg8FfcBo2BA",  # kod: 7
    "8": "BAACAgIAAxkBAANvaEPs63Tar2vMxKN5UUCytPt2Z4sAAo50AAJ9CKlIJg9_OV0_0Ho2BA",  # kod: 8
    "9": "BAACAgIAAxkBAAODaEP-07n6KNosK3xhDraCC1cQ3voAAhRYAAJr3VBKtWrD-K_P5rU2BA",  # kod: 9
    "10": "BAACAgIAAxkBAAOFaEP-6A-n0fyRRwWl8UJyEmv3dQwAArVkAAJf_5lIugu3fjbYLZU2BA",  # kod: 10
    "11": "BAACAgIAAxkBAAOHaEP-_TONNPwyuOoQoEurp1tFYD8AArddAAKEC_BLeFteYqE6XJo2BA",  # kod: 11
    "12": "BAACAgIAAxkBAAOJaEP_KHLrSsPADSJmCqUYGBGCRz8AAplNAAKWtUBJTkPQuzZYxxw2BA",  # kod: 12
    "13": "BAACAgIAAxkBAAOLaEP_SWG9a3bY3kfhT95WebN9fDkAAkpFAAJifplKegWQu0ec6hs2BA",  # kod: 13
    "14": "BAACAgIAAxkBAAOMaEP_SSYogNrnQQnst2lWvKjGTqMAAthkAAJf_5lII05oeTYW0mw2BA",  # kod: 14
    "15": "BAACAgIAAxkBAAONaEP_SdIzgFhLM030zBSlmRx6Y14AAvFUAALM5zFKNCugcRq5dsc2BA",  # kod: 15
    "16": "BAACAgIAAxkBAAOOaEP_SXdKWqYkQ1ZW8bex8rtZp7AAApNmAAI-zzhKL4K5iwhfaCE2BA",  # kod: 16
    "17": "BAACAgIAAxkBAAOPaEP_SYQRXJGwQx_1iJkZW2xigiIAAh5_AAIfZsFIrD_WSDwRAAE8NgQ",  # kod: 17
    "18": "BAACAgIAAxkBAANraEPs62uiWD1WQGdo3LgXrMZleMEAAv1qAAJfWSFI6v3M5_hUfYo2BA",  # kod: 18
    "19": "BAACAgIAAxkBAAOVaEP_rmVt_TRgjLAniyG-zcQwlpAAAih_AAIfZsFIdrDHziGNmDI2BA",  # kod: 19
    "20": "BAACAgIAAxkBAAOWaEP_rv-Q7Zv4Ivhy15p5xN8-Rp4AAjN_AAIfZsFInn0uX9xmGMY2BA",  # kod: 20
    "21": "BAACAgIAAxkBAAOXaEP_rk8m82rGyRWkYA_q5b7gYHoAAkAtAAJHOahIzVR_-RDo0882BA",  # kod: 21
    "22": "BAACAgIAAxkBAAOYaEP_rlsX5LQnWY3X2vLxdo_Ug-sAAspPAAK4hAFJpMnCm2xeD_Q2BA",  # kod: 22
    "23": "BAACAgIAAxkBAAOZaEP_rlU8tqociU5ewrAaL0PD6lEAAnBAAAIy7fBLn88wjdSy7KI2BA",  # kod: 23
    "24": "BAACAgIAAxkBAAOfaEQAAR5XQHgG6xsJrxWAEmR_eS_bAAIxNwAC_h-ZSnOP34kR0fV-NgQ",  # kod: 24
    "25": "BAACAgIAAxkBAAOgaEQAAR6nAhN07RMg9YSLRJLapp1bAAIzcQACcs-QSGfVqSLB3mSdNgQ",  # kod: 25
    "26": "BAACAgIAAxkBAAOhaEQAAR4NcZLhqxHKWBjch7HUy5bwAAJ6XgACIA9hSPEYyf9nbYbxNgQ",  # kod: 26
    "27": "BAACAgIAAxkBAAOiaEQAAR6c263eBMaHgL-pj2NpAt7SAAIadQACcQtQSRBLlc4g-04rNgQ",  # kod: 27
    "28": "BAACAgIAAxkBAAOjaEQAAR5NrRmk1Z-vWaEM-u1LM9tUAAIodQACcQtQSRkUUb95kyvNNgQ",  # kod: 28
    "29": "BAACAgIAAxkBAAOkaEQAAR4-ColdViGd_lpZ_-ahFDXBAALeagACGZmpSejqA-FWjDZWNgQ",  # kod: 29
    "30": "BAACAgIAAxkBAAOlaEQAAR7O8dyRcuf1vvjAF91xhoE-AAKzGwACA9fRSqd-NIIY9t6sNgQ",  # kod: 30
    "31": "BAACAgQAAxkBAAOmaEQAAR5InDyHvj3RCgQ-i8bgzF04AAJgAgACPYjsUrWLRdY_LJioNgQ",  # kod: 31
    "32": "BAACAgIAAxkBAAOnaEQAAR539O1skT-lbQMVzuFKcsh-AAIYbwACSEeQSagN2HoxxZAyNgQ",  # kod: 32
    "33": "BAACAgIAAxkBAAOoaEQAAR5MCln5Vzr2UG7XKStu2_f2AALAawACZXbZSlLieZtl0DGPNgQ",  # kod: 33
    "34": "BAACAgIAAxkBAAOpaEQAAR7X-aK3-EwTHk3LmonKUQXoAAK5CQACAnIBSPf5XgPVN1ALNgQ",  # kod: 34
    "35": "BAACAgIAAxkBAAOqaEQAAR5BuDsctUaIxrg_o-w8F8IGAAIWZAACHI7hSj0JZNlqE5n5NgQ",  # kod: 35
    "36": "BAACAgIAAxkBAAOraEQAAR5Jb26EH0XMYHl0jPXu9Wb7AALwdQACQz2wSpbdD2t2vkGdNgQ",  # kod: 36
}
#/start komandas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1 - kanal", url=f"https://t.me/{KANALLAR[0][1:]}")],
        [InlineKeyboardButton("2 - Instagram", url=INSTAGRAM_LINK)],
        [InlineKeyboardButton("✅ Tasdiqlash", callback_data="tasdiqlash")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "❌ Botdan foydalanish uchun kanalga obuna bo‘ling:",
        reply_markup=reply_markup
    )

# Tasdiqlash
async def tasdiqlash(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    obuna = True
    for kanal in KANALLAR:
        try:
            member = await context.bot.get_chat_member(chat_id=kanal, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                obuna = False
                break
        except:
            obuna = False
            break

    if obuna:
        await query.edit_message_text("✅ Obuna tasdiqlandi! Video kodini yuboring .")
    else:
        await query.answer("❗ Iltimos, avval kanalga obuna bo‘ling.", show_alert=True)

# Kodni qabul qilish
async def handle_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = update.message.text.strip()
    file_id = VIDEO_IDS.get(code)

    if file_id:
        await update.message.reply_video(video=file_id)
    else:
        await update.message.reply_text("❌ Bunday kod mavjud emas.")

# Botni ishga tushirish
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tasdiqlash, pattern="tasdiqlash"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_code))

print("✅ Bot ishga tushdi...")
app.run_polling()
