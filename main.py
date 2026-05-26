from storage import save_data, load_data
from models import Bank

while True:
    try:
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
            user_object = Bank(name, last_name, number, login, password)
            user_object.get_info()
            break
        
        else:
            print('Войти')
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            break
    except ValueError:
        print('Ошибка!')