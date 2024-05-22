from telegram import Update
from telegram.ext import CallbackContext
from apis import connections


async def support(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    print(user_id)
    await update.message.reply_text("""
    ✅ جهت ارتباط با پشتیبانی با آیدی زیر در ارتباط باشید 👇\n 
    📌 https://t.me/ZoonVPN_sup
    """)
