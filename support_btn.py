from telegram import Update
from telegram.ext import CallbackContext


async def support(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
    ✅ جهت ارتباط با پشتیبانی با آیدی زیر در ارتباط باشید 👇\n 
    📌 https://t.me/ZoonVPN_sup
    """)