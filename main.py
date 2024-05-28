from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

from root import start
from support_btn import support
from order_btn import order, order_button, photo, admin_accept_btn
from free_btn import free_acc, check_membership_callback


def main() -> None:
    application = Application.builder().token('6651453486:AAFC4Ff5Vr56XeuSSviG-WfazSOhNUYSiMc').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('پشتیبانی 💁‍♀️'), support))
    application.add_handler(MessageHandler(filters.Regex('خرید سرویس  💰'), order))
    application.add_handler(CommandHandler("freetrial", free_acc))
    application.add_handler(MessageHandler(filters.Regex('سرویس رایگان 🤩'), free_acc))
    application.add_handler(CallbackQueryHandler(order_button, pattern='^(3 month|6 month|1 year|CardShift_3month|CardShift_6month|CardShift_1year|send_image_pyment_3month|send_image_pyment_6month|send_image_pyment_1year)$'))
    application.add_handler(CallbackQueryHandler(admin_accept_btn, pattern='^(ok_|fail_)\\d+$'))
    application.add_handler(CallbackQueryHandler(check_membership_callback, pattern='check_membership'))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
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
# run https_proxy=socks5://127.0.0.1:2080 python main.py
