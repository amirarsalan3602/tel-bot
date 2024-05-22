from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext
from apis import connections


async def free_acc(update: Update, context: CallbackContext) -> None:
    connections.free_account(uuid="3243234", EXP="3d")
    await update.message.reply_text("""
        ✅ جهت ارتباط با پشتیبانی با آیدی زیر در ارتباط باشید 👇\n 
        📌 https://t.me/ZoonVPN_sup
        """)
