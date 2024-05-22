from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

from root import start
from support_btn import support
from order_btn import order, order_button,photo,admin_accept_btn


def main() -> None:
    application = Application.builder().token('6651453486:AAElaeNKNxpQqq8eDGC3nOcC7k9hBOwKHnA').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('پشتیبانی 💁‍♀️'), support))
    application.add_handler(MessageHandler(filters.Regex('خرید سرویس  💰'), order))
    application.add_handler(CallbackQueryHandler(order_button))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
    application.add_handler(CallbackQueryHandler(admin_accept_btn))
    application.run_polling()


if __name__ == '__main__':
    main()
