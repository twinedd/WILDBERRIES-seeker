import random,webbrowser
import requests
import threading
from dhooks import Webhook


def feedback():
    return random.randint(10_000_000, 999_999_999)


hosts = ('05', '04', '03', '02', '01')
hook = Webhook('https://discord.com/api/webhooks/1201086934462763038/dwin_1dGa0ugJtlc65n0yucOTHaPCqlU-1yTwWXKERH2SI8tKslC5L0sC86Kci9czm1f')


def carnage_finder():
    while True:
        id_1 = str(feedback())
        for i in hosts:
            photo = requests.get(f'https://feedback{i}.wbbasket.ru/vol{id_1[:4] if len(id_1) > 8 else id_1[:3]}/part{id_1[:6] if len(id_1) > 8 else id_1[:5]}/{id_1}/photos/fs.webp')
            if photo.status_code != 404:
                print(photo.url)

def start(times: int = 1):
    for i in range(times):
        threading.Thread(target=carnage_finder).start()


start(times=10)
