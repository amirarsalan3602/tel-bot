# import datetime
#
# import requests
# import re
# import time
#
# from dateutil.relativedelta import relativedelta
#
#
# def convert_base64(name: str):
#     import base64
#     encoded_data = base64.b64encode(name.encode('utf-8'))
#     return encoded_data.decode("utf-8")

#
# def repair_config(exp: int = 3, name: str = "@ZoonV | ارائه دهنده VPN پرسرعت در ایران", repo: int = 1):
#     res = requests.get(f"https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt")
#     res = res.text.split("\n")
#     with open("sub.txt", "w", encoding="utf-8") as f:
#         i = f"# profile-title: base64:{convert_base64(name)}\n# profile-update-interval: 1\n# subscription-userinfo: upload=3500; download=600000; total=625000000; expire={datetime.datetime.now() + relativedelta(months=exp)}\n\n"
#         f.write(i)
#         for response in res:
#             if response[:5] == "vless" or response[:6] == "trojan":
#                 response = response.replace(response[response.find("#") + 1:], f"{name}")
#                 if response.find("serviceName=") != -1:
#                     response = re.sub(r'(serviceName=)[^&]*', rf'\{name}', response)
#                 f.write(response + "\n")
#
#
# if __name__ == "__main__":
#     repair_config()
#
# a = "زحمت بکش به شماره کارت\n`1252012658914562` بنام رضا رضایی \n مبلغ 195,000 تومان واریز کن ! \n"


import json
import subprocess
import requests
import time
import threading


def run_v2ray():
    # تبدیل کانفیگ VLESS به فرمت JSON
    vless_config = {
        "inbounds": [
            {
                "port": 1080,  # پورت محلی برای گوش دادن
                "protocol": "socks",
                "settings": {
                    "udp": True
                }
            }
        ],
        "outbounds": [
            {
                "protocol": "vless",
                "settings": {
                    "vnext": [
                        {
                            "address": "51.75.30.8",  # آدرس سرور VLESS
                            "port": 80,  # پورت سرور VLESS
                            "users": [
                                {
                                    "id": "1949f066-bcb0-49be-88e9-74abd940f80e",  # UUID
                                    "encryption": "none"
                                }
                            ]
                        }
                    ]
                },
                "streamSettings": {
                    "network": "ws",
                    "wsSettings": {
                        "path": "/http"  # مسیر WebSocket
                    }
                }
            }
        ]
    }

    # ذخیره کانفیگ در یک فایل
    with open('config.json', 'w') as config_file:
        json.dump(vless_config, config_file)

    # اجرای v2ray-core با کانفیگ جدید
    subprocess.run(["v2ray", "run", "-c", "config.json"], shell=False)


def download_file():
    # آدرس فایلی که می‌خواهید دانلود کنید
    url = 'https://edge10.85.ir.cdn.ir/2024/Software/AnyDesk.8.0.9_YasDL.com.rar?az5'

    # شروع زمان دانلود
    start_time = time.time()

    # دانلود فایل
    response = requests.get(url, stream=True, proxies={
        'http': 'socks5://127.0.0.1:1080',
        'https': 'socks5://127.0.0.1:1080',
    })

    # محاسبه اندازه فایل
    total_length = response.headers.get('content-length')

    # اگر اندازه فایل موجود است، سرعت دانلود را محاسبه می‌کنیم
    if total_length is not None:
        total_length = int(total_length)
        downloaded = 0
        with open('file.zip', 'wb') as f:
            for data in response.iter_content(chunk_size=4096):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total_length)
                elapsed_time = time.time() - start_time
                speed = downloaded / elapsed_time if elapsed_time > 0 else 0
                print(f"\r[{'=' * done}{' ' * (50 - done)}] {done * 2}% {speed:.2f} bytes/sec", end='')

    print('\nDownload completed!')


# ایجاد نخ‌ها
thread_v2ray = threading.Thread(target=run_v2ray)
thread_download = threading.Thread(target=download_file)

# شروع نخ‌ها
thread_v2ray.start()
time.sleep(5)
thread_download.start()

# انتظار برای پایان نخ‌ها
thread_v2ray.join()
thread_download.join()
