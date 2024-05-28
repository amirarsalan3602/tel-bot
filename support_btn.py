from telegram import Update
from telegram.ext import CallbackContext
from apis import connections


async def support(update: Update, context: CallbackContext) -> None:



    await update.message.reply_text("""
    ✅ جهت ارتباط با پشتیبانی با آیدی زیر در ارتباط باشید 👇\n 
    📌 https://t.me/ZoonV_sup
    """)
