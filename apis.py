import datetime
import re

import pytz
import jdatetime

import requests

import re


def extract_numbers(input_string):
    # الگوی regex برای استخراج اعداد از رشته
    pattern = r'\d+'
    # جستجوی الگو در رشته
    numbers = re.findall(pattern, input_string)
    # اتصال اعداد به صورت یک رشته و تبدیل به عدد صحیح
    result = ''.join(numbers)
    return result


def send_sms(phone: str = "09999052068"):
    totob = requests.get(url=f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={phone}")
    digikala = requests.post(url=f"https://api.digikala.com/v1/user/authenticate/",
                             json={"backUrl": "/", "username": phone, "otp_call": "false"})
    return "success"


class Connections:
    def __init__(self):
        self.server = "103.216.61.88"

    def free_account(self, uuid: str = None, token: str = None, EXP: str = None):
        response = requests.post(url=f"http://{self.server}/Free_acc/{uuid}/{EXP}")
        if response.status_code == 404:
            return "There is"
        elif response.status_code == 200:
            return response.json()[-1]

    def vip(self, uuid, EXP: str):
        EXP = extract_numbers(EXP)

        if EXP == "195000":
            EXP = "90d"
        elif EXP == "780000":
            EXP = "180d"
        elif EXP == "1700000":
            EXP = "360d"
        response = requests.post(url=f"http://{self.server}/vip/{uuid}/{EXP}")
        response = response.json()
        gregorian_datetime = datetime.datetime.fromisoformat(response['created_date'].replace("Z", "+00:00"))
        tehran_tz = pytz.timezone('Asia/Tehran')
        tehran_datetime = gregorian_datetime.astimezone(tehran_tz)
        response['created_date'] = jdatetime.datetime.fromgregorian(datetime=tehran_datetime)

        gregorian_datetime = datetime.datetime.fromisoformat(response['expired_date'].replace("Z", "+00:00"))
        tehran_tz = pytz.timezone('Asia/Tehran')
        tehran_datetime = gregorian_datetime.astimezone(tehran_tz)
        response['expired_date'] = jdatetime.datetime.fromgregorian(datetime=tehran_datetime)
        return response


connections = Connections()
# a = Connections()
# a = a.vip(uuid="32432394", EXP="یکساله 1,700,000 تومان")
# print(a["created_date"])
