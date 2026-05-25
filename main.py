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
        user = {
            'name': name,
            'last_name': last_name,
            'number': number,
            'login': login,
            'password': password
        }
        data.append(user)
        save_data(data)
        break
    
    else:
        print('Войти')
        break