from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackContext
from telegram.error import BadRequest

from apis import connections



async def check_membership(user_id: int, bot, channel_id: str) -> bool:
    try:
        member_status = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        if member_status.status in ['member', 'administrator', 'creator']:
            return True
    except BadRequest as e:
        print(f"Error checking membership: {e}")
    return False


async def free_acc(update: Update, context: CallbackContext, user_id: int = None) -> None:
    if user_id is None:
        user_id = update.message.from_user.id
        message = update.message
    else:
        message = update.callback_query.message

    # بررسی عضویت کاربر در کانال
    channel_id = '-1002049534507'  # آی‌دی عددی کانال خود را وارد کنید
    is_member = await check_membership(user_id, context.bot, channel_id)

    if not is_member:
        await message.reply_text(
            "برای دریافت اکانت رایگان باید عضو کانال ما شوید. لطفا عضو کانال شوید و دوباره تلاش کنید.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/zoonv")],
                    [InlineKeyboardButton("بررسی عضویت", callback_data='check_membership')]
                ]
            )
        )
        return

    token = connections.free_account(uuid=str(user_id), EXP="3d")
    if token != "There is":
        await context.bot.send_message(chat_id=message.chat.id, text=f"""
            \nسلام رفیق ! 🎉 خبر خوبی دارم واسه تو ! تست سه روزه‌ی رایگانت آماده‌س ! 🚀
            \nفقط کافیه روی لینک زیر کلیک کنی و از سرویس‌هامون لذت ببری :
            <code><a href="http://{connections.server}/get_active_configs/{token}">http://{connections.server}/get_active_configs/{token}</a></code>
            یادت نره که دستورالعمل‌ها رو با دقت بخونی که بتونی بهترین استفاده رو ببری! 📖\n
            و اگه سوالی داشتی، ما همیشه اینجاییم واسه کمک :\n
            <a href="https://t.me/ZoonV_sup">📌 پشتیبانی ZoonV</a>
            <a href="https://t.me/ZoonV">📌 کانال ما </a>
            """, parse_mode='HTML')
    else:
        await context.bot.send_message(chat_id=message.chat.id, text=f"""
            دوست عزیزم شما یک بار از سرویس رایگان ما استفاده کردید. متاسفانه بخاطر هزینه بالای سرویس‌ها برای ما ممکن نیست که دوباره سرویس رایگان در اختیارتون بزاریم. ازتون دعوت می‌کنیم که اگر از سرویس‌های ما رضایت داشتید سرویس VIP ما را تهیه کنید ❤️
            📌 <a href="https://t.me/ZoonV_sup">پشتیبانی ZoonV</a>
            """, parse_mode='HTML')


async def check_membership_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = query.from_user.id
    channel_id = '-1002049534507'  # آی‌دی عددی کانال خود را وارد کنید

    await query.answer()

    is_member = await check_membership(user_id, context.bot, channel_id)

    if is_member:
        await free_acc(update, context, user_id=user_id)
    else:
        await query.edit_message_text(
            "شما هنوز عضو کانال ما نشده‌اید. لطفا عضو کانال شوید و دوباره تلاش کنید.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/zoonv")],
                    [InlineKeyboardButton("بررسی عضویت", callback_data='check_membership')]
                ]
            )
        )
