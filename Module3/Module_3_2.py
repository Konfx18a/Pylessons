def need_sbls(adress):
    need_symbols = '.com', '.ru', '.net'
    ns = False
    for i in need_symbols:
        if adress.endswith(i):
            ns = True
            break
    return ns and adress.find('@') + 1
def send_mail(message, recipient, sender='university.help@gmail.com'):
    if not need_sbls(recipient) or not need_sbls(sender) :
        print('Невозможно отправить письмо с адреса ' + sender + ' на адрес ' + recipient)
        return
    if ( recipient == sender) :
        print(' Нельзя отправить письмо самому себе! ')
        return
    if sender == 'university.help@gmail.com':
        print(' Письмо успешно отправленно с адреса ' + sender + ' на адрес ' + recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправленно с адреса ' + sender + ' на адрес ' + recipient)

send_mail('Привет', 'ab@cd.ru', 'qwerty@g.ru')
send_mail('Привет', 'ab@cd.ru')
send_mail('Привет', 'ab@cd.ru', 'ab@cd.ru')
send_mail('Привет', 'abcd.ru', 'ab@cd.ru')
send_mail('Привет', 'ab@cd.ru', 'ab@cd.tv')
