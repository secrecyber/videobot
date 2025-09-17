from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)

BOT_TOKEN = "7252155462:AAGkF0objeszRAG_IHSPi6ltsC-Rtx8EKHg"
KANALLAR = ["@cybersec_uzbek"]
INSTAGRAM_LINK = "https://www.instagram.com/aziz_cyber"
VIDEO_IDS = {
    "1": "BAACAgIAAxkBAANnaEPsuHp3K8xSM0bdC9f6Vc2zcYgAArlIAAI5iYBJ4B7cK7Q7xEs2BA",  # kod: 1
    "7": "BAACAgIAAxkBAANpaEPs6zrY0RZbxERn40Kc-rv3oVYAAqdaAAIGzqlIjzP2CaeQ-Ig2BA",  # kod: 2
    "9": "BAACAgIAAxkBAANqaEPs65t5_ZohZr5-0ygeKKStIgMAAoJyAAIq94hJRi2dPz8BcaM2BA",  # kod: 3
    "3": "BAACAgIAAxkBAANraEPs62uiWD1WQGdo3LgXrMZleMEAAv1qAAJfWSFI6v3M5_hUfYo2BA",  # kod: 4
    "10": "BAACAgIAAxkBAANsaEPs6yLxkUa-RwrV3RbMwXpuhjIAAo5zAAKOCwFJNxZiqUV4me42BA",  # kod: 5
    "34": "BAACAgIAAxkBAANtaEPs61s_l1jpIRJ-CHg1gRMPGGUAAp9SAAI7PeBJbq3Uvx1jFUg2BA",  # kod: 6
    "23": "BAACAgIAAxkBAANuaEPs66Hdc4MQ7y_7NI1QkbHD40EAAmRrAAImQrhImklLg8FfcBo2BA",  # kod: 7
    "65": "BAACAgIAAxkBAANvaEPs63Tar2vMxKN5UUCytPt2Z4sAAo50AAJ9CKlIJg9_OV0_0Ho2BA",  # kod: 8
    "13": "BAACAgIAAxkBAAODaEP-07n6KNosK3xhDraCC1cQ3voAAhRYAAJr3VBKtWrD-K_P5rU2BA",  # kod: 9
    "19": "BAACAgIAAxkBAAOFaEP-6A-n0fyRRwWl8UJyEmv3dQwAArVkAAJf_5lIugu3fjbYLZU2BA",  # kod: 10
    "15": "BAACAgIAAxkBAAOHaEP-_TONNPwyuOoQoEurp1tFYD8AArddAAKEC_BLeFteYqE6XJo2BA",  # kod: 11
    "20": "BAACAgIAAxkBAAOJaEP_KHLrSsPADSJmCqUYGBGCRz8AAplNAAKWtUBJTkPQuzZYxxw2BA",  # kod: 12
    "25": "BAACAgIAAxkBAAOLaEP_SWG9a3bY3kfhT95WebN9fDkAAkpFAAJifplKegWQu0ec6hs2BA",  # kod: 13
    "27": "BAACAgIAAxkBAAOMaEP_SSYogNrnQQnst2lWvKjGTqMAAthkAAJf_5lII05oeTYW0mw2BA",  # kod: 14
    "29": "BAACAgIAAxkBAAONaEP_SdIzgFhLM030zBSlmRx6Y14AAvFUAALM5zFKNCugcRq5dsc2BA",  # kod: 15
    "90": "BAACAgIAAxkBAAOOaEP_SXdKWqYkQ1ZW8bex8rtZp7AAApNmAAI-zzhKL4K5iwhfaCE2BA",  # kod: 16
    "93": "BAACAgIAAxkBAAOPaEP_SYQRXJGwQx_1iJkZW2xigiIAAh5_AAIfZsFIrD_WSDwRAAE8NgQ",  # kod: 17
    "95": "BAACAgIAAxkBAANraEPs62uiWD1WQGdo3LgXrMZleMEAAv1qAAJfWSFI6v3M5_hUfYo2BA",  # kod: 18
    "97": "BAACAgIAAxkBAAOVaEP_rmVt_TRgjLAniyG-zcQwlpAAAih_AAIfZsFIdrDHziGNmDI2BA",  # kod: 19
    "99": "BAACAgIAAxkBAAOWaEP_rv-Q7Zv4Ivhy15p5xN8-Rp4AAjN_AAIfZsFInn0uX9xmGMY2BA",  # kod: 20
    "71": "BAACAgIAAxkBAAOXaEP_rk8m82rGyRWkYA_q5b7gYHoAAkAtAAJHOahIzVR_-RDo0882BA",  # kod: 21
    "74": "BAACAgIAAxkBAAOYaEP_rlsX5LQnWY3X2vLxdo_Ug-sAAspPAAK4hAFJpMnCm2xeD_Q2BA",  # kod: 22
    "76": "BAACAgIAAxkBAAOZaEP_rlU8tqociU5ewrAaL0PD6lEAAnBAAAIy7fBLn88wjdSy7KI2BA",  # kod: 23
    "79": "BAACAgIAAxkBAAOfaEQAAR5XQHgG6xsJrxWAEmR_eS_bAAIxNwAC_h-ZSnOP34kR0fV-NgQ",  # kod: 24
    "83": "BAACAgIAAxkBAAOgaEQAAR6nAhN07RMg9YSLRJLapp1bAAIzcQACcs-QSGfVqSLB3mSdNgQ",  # kod: 25
    "86": "BAACAgIAAxkBAAOhaEQAAR4NcZLhqxHKWBjch7HUy5bwAAJ6XgACIA9hSPEYyf9nbYbxNgQ",  # kod: 26
    "89": "BAACAgIAAxkBAAOiaEQAAR6c263eBMaHgL-pj2NpAt7SAAIadQACcQtQSRBLlc4g-04rNgQ",  # kod: 27
    "70": "BAACAgIAAxkBAAOjaEQAAR5NrRmk1Z-vWaEM-u1LM9tUAAIodQACcQtQSRkUUb95kyvNNgQ",  # kod: 28
    "50": "BAACAgIAAxkBAAOkaEQAAR4-ColdViGd_lpZ_-ahFDXBAALeagACGZmpSejqA-FWjDZWNgQ",  # kod: 29
    "52": "BAACAgIAAxkBAAOlaEQAAR7O8dyRcuf1vvjAF91xhoE-AAKzGwACA9fRSqd-NIIY9t6sNgQ",  # kod: 30
    "55": "BAACAgQAAxkBAAOmaEQAAR5InDyHvj3RCgQ-i8bgzF04AAJgAgACPYjsUrWLRdY_LJioNgQ",  # kod: 31
    "57": "BAACAgIAAxkBAAOnaEQAAR539O1skT-lbQMVzuFKcsh-AAIYbwACSEeQSagN2HoxxZAyNgQ",  # kod: 32
    "59": "BAACAgIAAxkBAAOoaEQAAR5MCln5Vzr2UG7XKStu2_f2AALAawACZXbZSlLieZtl0DGPNgQ",  # kod: 33
    "17": "BAACAgIAAxkBAAOpaEQAAR7X-aK3-EwTHk3LmonKUQXoAAK5CQACAnIBSPf5XgPVN1ALNgQ",  # kod: 34
    "21": "BAACAgIAAxkBAAOqaEQAAR5BuDsctUaIxrg_o-w8F8IGAAIWZAACHI7hSj0JZNlqE5n5NgQ",  # kod: 35
    "36": "BAACAgIAAxkBAAOraEQAAR5Jb26EH0XMYHl0jPXu9Wb7AALwdQACQz2wSpbdD2t2vkGdNgQ",  # kod: 36
    "60": "BAACAgIAAxkBAAPsaEfBc76w6p47AAETwmcUlFjuei1vAAIoXAACvW7YS15PhwUT1frSNgQ",  # kod: 37
    "62": "BAACAgIAAxkBAAPtaEfBc2L9DteV7gPfBcA0AAFb2yYLAAJtRQACdcVISuvjNfxCzvhYNgQ",  # kod: 38
    "64": "BAACAgUAAxkBAAPuaEfBc2IPk83ggVZXZmwJ0QaEofEAAp0MAAJaiUBW9qc5vw_f8YE2BA",  # kod: 39
    "66": "BAACAgIAAxkBAANuaEPs66Hdc4MQ7y_7NI1QkbHD40EAAmRrAAImQrhImklLg8FfcBo2BA",  # kod: 40
    "69": "BAACAgIAAxkBAAPwaEfBc1pDPUhXk1E4YmtIhVKihc0AAvJ3AAImQsBIeEsC1VFvMRw2BA",  # kod: 41
    "40": "BAACAgIAAxkBAAPxaEfBc7Dxtek2SGug0xEf_iD7KckAAlhqAALctZhK_36rMLpbu442BA",  # kod: 42
    "42": "BAACAgIAAxkBAAPyaEfBc0IPccrniwfnaSn-VgABK4-GAAIvSQACpFSJSW0jt5z3UhAyNgQ",  # kod: 43
    "45": "BAACAgIAAxkBAAPzaEfBc9MUqKm__ASYo448KUyEsKEAAtp7AAIsTulJGxZlJRjyL-Y2BA",  # kod: 44
    "47": "BAACAgUAAxkBAAP0aEfBc4mNzDne5c63gVJq9tmJAtcAAvsTAAJ6e4lU3t5SFldRTWw2BA",  # kod: 45
    "49": "BAACAgIAAxkBAAP1aEfBcxRCG2VPXd46rJWSGDOUzwIAAsM5AAIoeAhJJFIv95akIzs2BA",  # kod: 46
    "31": "BAACAgIAAxkBAAP2aEfBc4plEtqOOzjpKHHAiZiqzkYAAgFSAALa0UBKbtoMXiDCPdc2BA",  # kod: 47
    "33": "BAACAgIAAxkBAAP3aEfBc8BcaXGql_TSpGVoerq_lTMAAqhHAAKuyLhKNOkiJw4Er_02BA",  # kod: 48
    "39": "BAACAgIAAxkBAAP4aEfBc1rKTLU_B8GKOkOCPjCxgE8AAplwAALctZhK2ewDV5m6BDI2BA",  # kod: 49
    "37": "BAACAgIAAxkBAAP5aEfBc4Y0CM856SPWSJyAkrsVLHAAAj1vAALEjcBIIgyzU_2KCpE2BA",  # kod: 50

    "100": "BAACAgIAAxkBAAJB3WjKpKHxJcl0Yppkm5Tfgbf_4wGvAAKHLwACsfqhS8-ica-cLxzJNgQ",  # kod: 51
    "103": "BAACAgIAAxkBAAJB32jKpKxlBDXydckDWhYdX-jgE7TNAALXXgACRnAISAIlSd0pdHLpNgQ",  # kod: 52
    "107": "BAACAgIAAxkBAAJB4WjKpL334b4IwgABC1KXfxAxAe1YdwACNHgAAiAm0UgEVeGJDZTRIzYE",  # kod: 53
    "107": "BAACAgIAAxkBAAJB42jKpMJssZsPyheh8139ftjd14-HAAL-fwACDqYAAUuTTbuOOl1jHDYE",  # kod: 53
    "107": "BAACAgIAAxkBAAJB5WjKpMxK2yUWc1sZvPQ4wjGrSLK5AAJXZAAC3ssRSPNT0gXPwEFkNgQ",  # kod: 53
    "110": "BAACAgIAAxkBAAJB52jKpNIjyqlyzxLnibFUW78QQHZ4AAIWZAACI0whSPV6Si5oUrdFNgQ",  # kod: 54
    "129": "BAACAgIAAxkBAAJB6WjKpNuHUZtj8vGRb9LkSwJShFSDAAIHagACdv6xSl9gn3RSwajPNgQ",  # kod: 55
    "115": "BAACAgIAAxkBAAJB62jKpOGFbAm8ASdKOkSiDgb65uQsAAKZcAAC6NgRS1XBDseKyfZVNgQ",  # kod: 56
    "118": "BAACAgIAAxkBAAJB7WjKpOa-bqY9-unGVONzkzAUPCh_AAKFZwACYsXRSDjsZ0YMwi5wNgQ",  # kod: 57
    "120": "BAACAgIAAxkBAAJB72jKpOvkG8-wJbqMREA2t10K_VKFAAItCwAClB1YS9cddiJiiitpNgQ",  # kod: 58
    "122": "BAACAgIAAxkBAAJB8WjKpPDcbs0O3Z45b_h65Kpg3Hw0AALRUQACjj9gSGu6_9w7zjnLNgQ",  # kod: 59
    "124": "BAACAgIAAxkBAAJB82jKpPf9v1a3jl-CPCiLj-16h4EvAAJ8QwAC1Y3YS0nGM_-BMTreNgQ",  # kod: 60
    "127": "BAACAgQAAxkBAAJB9WjKpP2WcSK9KyLA0LSjNY7Ydz6wAAJxAwAC-B5tUGac-MkrX5ENNgQ",  # kod: 61
    "130": "BAACAgIAAxkBAAJB92jKpQSNHVXh1x_lb7366K7jXoZXAAJGKQACFrnZSJp8s1TlyPPANgQ",  # kod: 62
    "133": "BAACAgEAAxkBAAJB-WjKpSxP6iuna1S5QwHwVDojv2AZAALuAAP8BshEC81_ZiDaV2w2BA",  # kod: 63
    "136": "BAACAgIAAxkBAAJB-2jKpTFP6BGuAAFfceHrA7QoKLqpfwAClmAAAifPqEg32UJgpl__SzYE",  # kod: 64
    "138": "BAACAgIAAxkBAAJB_WjKpTWNzUIl8eX3DY6HlNqTjfsuAAKRKQACjb7pSuxj8HaBDjZ8NgQ",  # kod: 65
    "140": "BAACAgQAAxkBAAJB_2jKpTt_N4Xvt80QZJ_BL5vzUwt2AAJwEgACMJWpUOfv02UB3_rSNgQ",  # kod: 66
    "144": "BAACAgIAAxkBAAJCAWjKpUFNAQ4-r0PsQTK2eZWpDtZfAAKpMwACq7FJSBC3muJJDKd-NgQ",  # kod: 67
    "147": "BAACAgIAAxkBAAJCA2jKpUf-0G1YGc9nTL1bqbcdDEQ6AAJbagACZ7TJSc5i1N9Xllg9NgQ",  # kod: 68
    "149": "BAACAgIAAxkBAAJCBWjKpVFyXszewH273NvHeqG2IXb-AAKgQwACF5mxSzyxe1C0IoX9NgQ",  # kod: 50
    "150": "BAACAgIAAxkBAAJCB2jKpWF2FXzzgnEqIJOBtVtAl-9xAAJ6egACwWAJS4bh1Wy6GZMGNgQ",  # kod: 50


#                ddddddddddddddddddddddddddddddddddddddddddddddddddddd
    "900": "BAACAgIAAxkBAAODaEP-07n6KNosK3xhDraCC1cQ3voAAhRYAAJr3VBKtWrD-K_P5rU2BA",  # kod: 100
    "904": "BAACAgIAAxkBAAIBCWhHxde-5MsUMrVHyM9GDqk0r1p-AAI3XgACtK0ISuGTnujRAcElNgQ",  # kod: 101
    "909": "BAACAgIAAxkBAAOHaEP-_TONNPwyuOoQoEurp1tFYD8AArddAAKEC_BLeFteYqE6XJo2BA",  # kod: 102
    "932": "BAACAgIAAxkBAAOWaEP_rv-Q7Zv4Ivhy15p5xN8-Rp4AAjN_AAIfZsFInn0uX9xmGMY2BA",  # kod: 103
    "964": "BAACAgIAAxkBAAIBDGhHxdePCEiIOeaCb3HnBYHTEE9bAAJPPwACpe9xSvtVFS0snd6eNgQ",  # kod: 104
    "976": "BAACAgIAAxkBAAIBDWhHxdfrcTHtQJkGUCvtIwwC--9tAAKoKwACRpQZSZUyicZk6ZRwNgQ",  # kod: 105
    "912": "BAACAgIAAxkBAAIBDmhHxddk2e-s0JUAAfTq1Tc_7hQ65gAC8FQAAsznMUpIW114NZzSdzYE",  # kod: 106
    "988": "BAACAgIAAxkBAAIBD2hHxdcvyhByfnjH0yz7tPmim90UAAI_WgACnHvhSP3ravrZtR8kNgQ",  # kod: 107
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


# founder tg: @mr_xac