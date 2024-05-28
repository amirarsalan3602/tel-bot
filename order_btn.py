from cgitb import text

from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext

from apis import send_sms, connections


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
    user_id = str(query.from_user.id)
    if query.data == '3 month':
        context.bot_data[user_id] = {'selected_plan': 'سه ماهه 195,000 تومان'}
        keyboard = [
            [InlineKeyboardButton("کارت به کارت 💳", callback_data='CardShift_3month')],
            [InlineKeyboardButton("پرداخت آنلاین 🔄", callback_data='online_payment')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="لطفا روش پرداختت رو انتخاب کن !", reply_markup=reply_markup)
    elif query.data == "CardShift_3month":
        if user_id in context.bot_data:
            context.bot_data[user_id]['selected_payment'] = 'کارت به کارت 💳'
        keyboard = [
            [InlineKeyboardButton("ارسال فیش واریز", callback_data="send_image_pyment_3month")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="""
            زحمت بکش به شماره کارت 

            `6219861934364661`

            'امیرارسلان قاسم نیانفوتی'

             مبلغ 195,000 تومان واریز کن و بعدش از طریق دکمه ارسال فیش واریز عکس فیش رو برای ادمین ارسال کن !
            """,
            reply_markup=reply_markup, parse_mode='Markdown')
    elif query.data == '6 month':
        context.bot_data[user_id] = {'selected_plan': 'شش ماهه 780,000 تومان'}
        keyboard = [
            [InlineKeyboardButton("کارت به کارت 💳", callback_data='CardShift_6month')],
            [InlineKeyboardButton("پرداخت آنلاین 🔄", callback_data='online_payment')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="لطفا روش پرداختت رو انتخاب کن !", reply_markup=reply_markup)
    elif query.data == "CardShift_6month":
        if user_id in context.bot_data:
            context.bot_data[user_id]['selected_payment'] = 'کارت به کارت 💳'
        keyboard = [
            [InlineKeyboardButton("ارسال فیش واریز", callback_data="send_image_pyment_6month")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="""
            زحمت بکش به شماره کارت 

            `6219861934364661`

            'امیرارسلان قاسم نیانفوتی'

             مبلغ 780,000 تومان واریز کن و بعدش از طریق دکمه ارسال فیش واریز عکس فیش رو برای ادمین ارسال کن !
            """,
            reply_markup=reply_markup, parse_mode='Markdown')
    elif query.data == '1 year':
        context.bot_data[user_id] = {'selected_plan': 'یکساله 1,700,000 تومان'}
        keyboard = [
            [InlineKeyboardButton("کارت به کارت 💳", callback_data='CardShift_1year')],
            [InlineKeyboardButton("پرداخت آنلاین 🔄", callback_data='online_payment')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="لطفا روش پرداختت رو انتخاب کن !", reply_markup=reply_markup)
    elif query.data == "CardShift_1year":
        if user_id in context.bot_data:
            context.bot_data[user_id]['selected_payment'] = 'کارت به کارت 💳'
        keyboard = [
            [InlineKeyboardButton("ارسال فیش واریز", callback_data="send_image_pyment_1year")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="""
            زحمت بکش به شماره کارت 

            `6219861934364661`

            'امیرارسلان قاسم نیانفوتی'

             مبلغ 1,700,000 تومان واریز کن و بعدش از طریق دکمه ارسال فیش واریز عکس فیش رو برای ادمین ارسال کن !
            """,
            reply_markup=reply_markup, parse_mode='Markdown')
    elif 'send_image_pyment' in query.data:
        if user_id in context.bot_data:
            context.bot_data[user_id]['selected_payment'] = 'ارسال فیش واریز'
        await query.edit_message_text(text="لطفا عکس فیش واریز خود را ارسال کنید :")


async def photo(update: Update, context: CallbackContext) -> None:
    user_id = str(update.message.from_user.id)
    photo_file = await update.message.photo[-1].get_file()
    file_path = f'user_{user_id}.jpg'
    await photo_file.download_to_drive(file_path)
    await update.message.reply_text(
        'عکس شما به ادمین ارسال شد. \n لطفا منتظر تایید ادمین باشید \n ادمین های ما تا در اولین فرصت درخواست شمارا برسی میکنند !')

    admin_id = '492443372'
    send_sms()  # اطمینان حاصل کنید که این تابع به درستی کار می‌کند

    selected_plan = context.bot_data.get(user_id, {}).get('selected_plan', 'N/A')
    selected_payment = context.bot_data.get(user_id, {}).get('selected_payment', 'N/A')
    caption = f"User ID: {user_id}, Selected Plan: {selected_plan}, Selected Payment: {selected_payment}"

    try:
        with open(file_path, 'rb') as photo:
            await context.bot.send_photo(chat_id=admin_id, photo=photo, caption=caption,
                                         reply_markup=InlineKeyboardMarkup([
                                             [InlineKeyboardButton("OK", callback_data=f'ok_{user_id}'),
                                              InlineKeyboardButton("Fail", callback_data=f'fail_{user_id}')],
                                         ]))
    except Exception as e:
        print(f"Error sending photo: {e}")


async def admin_accept_btn(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    user_id = query.data.split('_')[1]
    selected_plan = context.bot_data.get(user_id, {}).get('selected_plan', 'N/A')
    selected_payment = context.bot_data.get(user_id, {}).get('selected_payment', 'N/A')
    if query.data.startswith('ok_'):
        result = connections.vip(uuid=user_id, EXP=selected_plan)
        text = f"""
        پرداخت شما تایید شد ✅\n
        خیلی ممنون از خریدتون 🙏🏻\n 
         لینک اتصال :\n
        \n<code><a href="http://{connections.server}/get_active_configs/{result['config_code']}">http://{connections.server}/get_active_configs/{result['config_code']}</a></code>
         تاریخ و زمان فعال سازی  :{result["created_date"].year}/{result["created_date"].month}/{result["created_date"].day} {result["created_date"].hour}:{result["created_date"].minute} \n
        تاریخ و زمان انقضای سرویس  : {result["expired_date"].year}/{result["expired_date"].month}/{result["expired_date"].day} {result["expired_date"].hour}:{result["expired_date"].minute} \n
        {result["expire_days"]}روز تا انقضاء سرویس !\n
        اگر مشکلی بود به ادمین پیام بدید !! \n
        <a href="https://t.me/ZoonV_sup">📌 پشتیبانی ZoonV</a> \n     
        """
        await context.bot.send_message(chat_id=user_id,
                                       text=text, parse_mode='HTML')
    elif query.data.startswith('fail_'):
        await context.bot.send_message(chat_id=user_id, text='پرداخت شما تایید نشد. لطفاً دوباره تلاش کنید.')
