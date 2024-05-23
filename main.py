import httpx
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

from root import start
from support_btn import support
from order_btn import order, order_button, photo, admin_accept_btn
from free_btn import free_acc

proxies = {"http://": "socks5://127.0.0.1:2080", "https://": "socks5://127.0.0.1:2080"}



def main() -> None:
    application = Application.builder().token('6651453486:AAFC4Ff5Vr56XeuSSviG-WfazSOhNUYSiMc').proxy(
        proxy=proxies).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('پشتیبانی 💁‍♀️'), support))
    application.add_handler(MessageHandler(filters.Regex('خرید سرویس  💰'), order))
    application.add_handler(MessageHandler(filters.Regex('سرویس رایگان 🤩'), free_acc))
    application.add_handler(CallbackQueryHandler(order_button))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
    application.add_handler(CallbackQueryHandler(admin_accept_btn))
    application.run_polling()


if __name__ == '__main__':
    main()

# urlpatterns = [
#     path('test222', views.Core.as_view()),
#     path('Free_acc/<str:telegram_uuid>/<str:config>', views.CreateUserAndFreeConfig.as_view()),
#     path('vip/<str:telegram_uuid>/<str:config>', views.CreateVipConfig.as_view()),
#     path('get_configs/<str:telegram_uuid>', views.UserConfigsView.as_view()),
#     path('get_redis', views.GetDataFromRedis.as_view())
# ]
