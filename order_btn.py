from cgitb import text

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext


async def order(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("سه ماهه 195,000 تومان", callback_data='3 month')],
        [InlineKeyboardButton("شش ماهه 780,000 تومان", callback_data='6 month')],
        [InlineKeyboardButton("یکساله 1,700,000 تومان", callback_data='1 year')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("مدت اعتبار سرویس رو انتخاب کن !\n تمام سرویس ها بدونه محدودیت حجم و یوز هستن 😎",
                                    reply_markup=reply_markup)


async def order_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == '3 month':
        keyboard = [
            [InlineKeyboardButton("کارت به کارت 💳", callback_data='CardShift')],
            [InlineKeyboardButton("پرداخت آنلاین 🔄", callback_data='online_payment')],  # TODO : تابع بازگشت
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="لطفا روش پرداختت رو انتخاب کن !", reply_markup=reply_markup)
    elif query.data == "CardShift":
        keyboad = [
            [InlineKeyboardButton("ارسال فیش واریز", callback_data="send_image_pyment")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboad)
        await query.edit_message_text(  # TODO : اصلاح قیمت گزاری
            text="""
            زحمت بکش به شماره کارت 
            
            `1827364890927461`
            
            'محسن یگانه'
            
            واریز مبلغ 195 تمن واریز کن و بعدش از طریق دکمه ارسال فیش واریز عکس فیش رو برای ادمین ارسال کن !
            """,
            reply_markup=reply_markup, parse_mode='Markdown', )
    elif query.data == '6 month':
        await query.edit_message_text(text="hello worlddddddddddddddddddddddddddd")
    elif query.data == '1 year':
        await query.edit_message_text(text="hello worlddddddddddddddddddddddddddd")
    elif query.data == 'send_image_pyment':
        await query.edit_message_text(text="لطفا عکس فیش واریز خود را ارسال کنید :")


async def photo(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    photo_file = await update.message.photo[-1].get_file()
    await photo_file.download_to_drive(f'user_{user_id}.jpg')
    await update.message.reply_text('عکس شما به ادمین ارسال شد. \n لطفا منتظر تایید ادمین باشید \n ادمین های ما تا در اولین فرصت درخواست شمارا برسی میکنند !' )


    # اینجا ID ادمین را قرار دهید
    admin_id = '492443372'
    await context.bot.send_photo(chat_id=admin_id, photo=open(f'user_{user_id}.jpg', 'rb'),
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("OK", callback_data=f'ok_{user_id}'),
                                      InlineKeyboardButton("Fail", callback_data=f'fail_{user_id}')],
                                 ]))


async def admin_accept_btn(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.data.split('_')[1]

    if query.data == 'ok':
        await  context.bot.send_message(chat_id=user_id, text='OK')
    elif 'fail' in query.data:
        await context.bot.send_message(chat_id=user_id, text='Fail')
