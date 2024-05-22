from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[KeyboardButton(" پشتیبانی 💁‍♀️ "), KeyboardButton("خرید سرویس  💰")],
                [KeyboardButton("سرویس های من 🚀")]]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text('به زون وی پی ان خوش اومدی ! 😎', reply_markup=reply_markup)


