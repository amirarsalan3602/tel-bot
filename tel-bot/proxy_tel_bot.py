import os
import subprocess

import uuid
import re
import socket
import json
from time import sleep

from urllib.parse import unquote

import redis

redis = redis.Redis(host="103.216.61.88", port=6379, password="SMVlq?cp3h99kj", db=0)


def generate_uuid_v5(user_uuid: str, namespace=uuid.NAMESPACE_URL):
    try:
        uuid_obj = uuid.UUID(user_uuid)
        if uuid_obj.hex == user_uuid.replace('-', ''):
            return user_uuid
    except ValueError:
        root_namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
        return str(uuid.uuid5(root_namespace, user_uuid))


def convert_vless(url: str):
    try:
        result = subprocess.run(['python3', 'tel-bot/v2ray2json/v2ray2json.py', url], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip()
        json_data = json.loads(output)
        json_data['inbounds'][0]["port"] = 2080
        user_uuid = generate_uuid_v5(re.search(r'vless://(.*?)@', url).group(1))
        if user_uuid:
            json_data["outbounds"][0]['settings']['vnext'][0]["users"][0]["id"] = user_uuid

        with open('tel-bot/config.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except:
        print(f"filed = {url}")

    return "successfully"


def run_v2ray(url):
    if convert_vless(url=url) == "successfully":
        process = subprocess.Popen(["v2ray", "run", "-c", "tel-bot/config.json"])
        return process.pid


if __name__ == '__main__':
    while True:
        url = redis.lindex("accepted", -1)
        pid = run_v2ray(url=url.decode("utf-8"))
        sleep(20)
        os.system(f"kill {pid}")
        