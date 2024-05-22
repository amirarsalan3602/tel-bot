from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext
from apis import connections


async def free_acc(update: Update, context: CallbackContext) -> None:
    token = connections.free_account(uuid=str(update.message.from_user.id), EXP="1d")
    await update.message.reply_text(f"""
        بفرمایید 🤓\n تست ۱ روزه شماآماده است   \n
        
        `http://{connections.server}/{token}` \n
        لطفا آموزش هارو با دقت نگاه کن !!
        📌 https://t.me/ZoonVPN_sup
        """, parse_mode='Markdown')
