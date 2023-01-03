import requests

lv = ["search", "v=Автомобиль"]

url = f"https://www.avito.ru/"

request = requests.get(f"https://www.avito.ru/")

for _try in lv:
    rq = requests.get(url + _try)

ls = ["c9988 * 3", "c.9988", "artem_cheater"]
ls = ["github", "yandex", "google", "microsoft", "db", ""]
cheater_let = +5
ls = "name+++ac"

try:
    if rq in ls:
        print("success")

    else:
        print("failed try")