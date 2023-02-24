#Given a string containing one or several emails, replacemail.ruwithgmail.com,yahoo.comwithoutlook.com, bk.ruwithkbtu.kz.
import re

string = "info@mail.ru, support@yahoo.org, help@bk.ru"

patterns = {"mail.ru": "gmail.com", "yahoo.com": "outlook.com", "bk.ru": "kbtu.kz"}

for pattern, replacement in patterns.items():
    string = re.sub(fr"\b[A-Za-z0-9._%+-]+@{pattern}\b", fr"\g<0>".replace(pattern, replacement), string)

print(string)