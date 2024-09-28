import random
import requests
import threading
from dhooks import Webhook

hook = Webhook('discord webhook url here')

def feedback():
    return random.randint(10_000_000, 999_999_999)

hosts = ('05', '04', '03', '02', '01')

def carnage_finder():
    while True:
        id_1 = str(feedback())
        for i in hosts:
            try:
                photo = requests.get(f'https://feedback{i}.wbbasket.ru/vol{id_1[:4] if len(id_1) > 8 else id_1[:3]}/part{id_1[:6] if len(id_1) > 8 else id_1[:5]}/{id_1}/photos/fs.webp')
                if photo.status_code != 404:
                    hook.send(photo.url)
                print(photo.url)
            except:
                pass

def start(times: int = 1):
    for i in range(times):
        threading.Thread(target=carnage_finder).start()

start(times=10)


