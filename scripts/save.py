def save_user_data(file_direction='users.txt', command='massage.from_user'):
    import datetime
    now = datetime.datetime.now()
    with open(file_direction, 'a', encoding='utf-8') as userdata:
        t = command
        userdata.write(f'{str(t)}' + now.strftime("%d-%m-%Y %H:%M"))
    '''Сохранение данных пользователей для дальнейшей работы с клиентами '''