import smtplib

def main(content='password.txt'):
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
    text = open(content, 'r').read()

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

if __name__ == '__main__':
    main()