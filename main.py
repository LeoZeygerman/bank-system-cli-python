from storage import save_data, load_data

while True:
    data = load_data()
    if len(data) == 0:
        print('Регистрация')
        name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        number = int(input('Введите номер телефона: '))
        login = input('Введите ваш логин: ')
        password = input('Введите пароль: ')
        break
    
    else:
        print('Войти')
        break